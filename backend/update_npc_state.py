import json
import sys
from pathlib import Path

SAVE_FILE = Path("backend/data/saves/save_01.json")
FLOAT_FIELDS = {"trust", "awareness", "restraint"}


def check_tier_promotion(npc: dict) -> bool:
    tier = npc["tier"]
    trust = npc["trust"]
    revealed = npc["topics_revealed"]
    if tier == 0 and trust > 0.3 and len(revealed) >= 1:
        npc["tier"] = 1
        return True
    if tier == 1 and trust > 0.6 and len(revealed) >= 3:
        npc["tier"] = 2
        return True
    return False


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("Usage: update_npc_state.py <npc_id> <field> <value>")

    npc_id, field, value = sys.argv[1], sys.argv[2], sys.argv[3]

    save = json.loads(SAVE_FILE.read_text())
    npc_states = save.get("npc_states", {})
    if npc_id not in npc_states:
        raise SystemExit(f"NPC '{npc_id}' not found in save file.")
    npc = npc_states[npc_id]

    if field in FLOAT_FIELDS:
        npc[field] = float(value)
        old_tier = npc["tier"]
        if check_tier_promotion(npc):
            print(f"Tier promoted: {npc_id} {old_tier} → {npc['tier']}")
    elif field == "met_player":
        npc["met_player"] = True
    elif field == "topics_revealed":
        if value not in npc["topics_revealed"]:
            npc["topics_revealed"].append(value)
        old_tier = npc["tier"]
        if check_tier_promotion(npc):
            print(f"Tier promoted: {npc_id} {old_tier} → {npc['tier']}")
    else:
        raise SystemExit(f"Unknown field '{field}'.")

    SAVE_FILE.write_text(json.dumps(save, indent=2))
    print(json.dumps(npc, indent=2))


if __name__ == "__main__":
    main()
