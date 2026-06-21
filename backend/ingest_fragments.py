import re
from pathlib import Path
import chromadb

SOURCE = Path("vault/Duskfield Opening Fragments.md")

def parse_fragments(text: str) -> list[dict]:
    blocks = text.split("---")
    fragments = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        id_match = re.search(r"\*\*(fragment_\d+)\*\*", block)
        if not id_match:
            continue

        # Metadata line: find the line containing "topic:" and "tier:"
        lines = block.splitlines()
        meta_line_idx = next(
            (i for i, l in enumerate(lines) if "topic:" in l and "tier:" in l),
            None,
        )
        if meta_line_idx is None:
            continue

        meta_line = lines[meta_line_idx].strip("_ ")
        topic_match = re.search(r"topic:\s*(\S+?)\s*\|", meta_line)
        tier_match = re.search(r"tier:\s*(\d)", meta_line)
        if not topic_match or not tier_match:
            continue

        fragment_id = id_match.group(1)
        topic = topic_match.group(1)
        tier = int(tier_match.group(1))

        # Prose is every line after the metadata line
        prose = "\n".join(lines[meta_line_idx + 1:]).strip()

        fragments.append({
            "id": fragment_id,
            "topic": topic,
            "tier": tier,
            "prose": prose,
        })
    return fragments


def main():
    text = SOURCE.read_text()
    fragments = parse_fragments(text)
    print(f"Parsed {len(fragments)} fragments.")

    client = chromadb.Client()
    collection = client.get_or_create_collection("duskfield_opening")

    collection.add(
        documents=[f["prose"] for f in fragments],
        ids=[f["id"] for f in fragments],
        metadatas=[{"topic": f["topic"], "tier": f["tier"]} for f in fragments],
    )
    print(f"Stored {len(fragments)} fragments in 'duskfield_opening'.")

    query = "what does grief look like in Duskfield"
    results = collection.query(query_texts=[query], n_results=2)

    print(f"\nQuery: '{query}'\n")
    for doc_id, doc in zip(results["ids"][0], results["documents"][0]):
        print(f"[{doc_id}]")
        print(doc)
        print()


if __name__ == "__main__":
    main()
