import json
import sys
from pathlib import Path

SAVE_FILE = Path("backend/data/saves/save_01.json")

GAINS = {
    "approach":      {"trust": 0.03},
    "linger":        {"trust": 0.05},
    "topic_trigger": {"trust": 0.08, "reputation": 0.05},
    "easter_egg":    {"trust": 0.15, "reputation": 0.10},
}


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
    if len(sys.argv) != 3:
        raise SystemExit("Usage: process_interaction.py <npc_id> <interaction_type>")

    npc_id, interaction_type = sys.argv[1], sys.argv[2]

    if interaction_type not in GAINS:
        raise SystemExit(f"Unknown interaction type '{interaction_type}'. "
                         f"Valid: {', '.join(GAINS)}")

    save = json.loads(SAVE_FILE.read_text())
    if npc_id not in save["npc_states"]:
        raise SystemExit(f"NPC '{npc_id}' not found in save file.")
    npc = save["npc_states"][npc_id]

    for field, amount in GAINS[interaction_type].items():
        npc[field] = min(1.0, npc.get(field, 0.0) + amount)

    old_tier = npc["tier"]
    if check_tier_promotion(npc):
        print(f"Tier promoted: {npc_id} {old_tier} → {npc['tier']}")

    SAVE_FILE.write_text(json.dumps(save, indent=2))
    print(json.dumps(npc, indent=2))


if __name__ == "__main__":
    main()
