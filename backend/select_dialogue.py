import json
import random
import sys
from pathlib import Path

SAVE_FILE = Path("backend/data/saves/save_01.json")
DIALOGUE_DIR = Path("backend/data/dialogue")


def main() -> None:
    npc_id, context = sys.argv[1], sys.argv[2]

    save = json.loads(SAVE_FILE.read_text())
    tier = save["npc_states"][npc_id]["tier"]

    dialogue = json.loads((DIALOGUE_DIR / f"{npc_id}.json").read_text())
    pool = dialogue[npc_id][f"tier_{tier}"][context]

    print(random.choice(pool))


if __name__ == "__main__":
    main()
