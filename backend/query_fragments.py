import json
import sys
from pathlib import Path

import chromadb

from ingest_fragments import SOURCE, parse_fragments

SAVE_FILE = Path("backend/data/saves/save_01.json")


def load_collection() -> tuple[chromadb.Collection, list[dict]]:
    fragments = parse_fragments(SOURCE.read_text())
    client = chromadb.Client()
    collection = client.get_or_create_collection("duskfield_opening")
    collection.add(
        documents=[f["prose"] for f in fragments],
        ids=[f["id"] for f in fragments],
        metadatas=[{"topic": f["topic"], "tier": f["tier"]} for f in fragments],
    )
    return collection, fragments


def get_npc_tier(npc_id: str) -> int:
    save = json.loads(SAVE_FILE.read_text())
    npc_states = save.get("npc_states", {})
    if npc_id not in npc_states:
        raise SystemExit(f"NPC '{npc_id}' not found in save file.")
    return npc_states[npc_id]["tier"]


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: query_fragments.py <npc_id> <query string>")

    npc_id = sys.argv[1]
    query = sys.argv[2]

    npc_tier = get_npc_tier(npc_id)
    collection, fragments = load_collection()

    # Count how many fragments pass the tier gate to avoid n_results > index size
    eligible_count = sum(1 for f in fragments if f["tier"] <= npc_tier)
    if eligible_count == 0:
        print(f"No fragments available for {npc_id} at tier {npc_tier}.")
        return

    n = min(2, eligible_count)
    results = collection.query(
        query_texts=[query],
        n_results=n,
        where={"tier": {"$lte": npc_tier}},
    )

    print(f"NPC: {npc_id}  |  tier gate: <= {npc_tier}")
    print(f"Query: '{query}'\n")
    for doc_id, doc, meta in zip(
        results["ids"][0], results["documents"][0], results["metadatas"][0]
    ):
        print(f"[{doc_id}]  topic: {meta['topic']}  tier: {meta['tier']}")
        print(doc)
        print()


if __name__ == "__main__":
    main()
