import json
import random
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
SAVES_DIR = DATA_DIR / "saves"

with open(DATA_DIR / "npc_definitions.json") as f:
    npc_definitions = json.load(f)

with open(DATA_DIR / "save_template.json") as f:
    template = json.load(f)

save = json.loads(json.dumps(template))

duskfield_exile_count = 0

for npc_id, npc_def in npc_definitions.items():
    basic_pool = npc_def.get("eligible_basic_traits", [])
    addon_pool = npc_def.get("eligible_addon_traits", [])

    if duskfield_exile_count >= 2:
        basic_pool = [t for t in basic_pool if t != "duskfield_exile"]

    basic_assigned = random.sample(basic_pool, min(4, len(basic_pool)))

    if "almost_voice" in basic_assigned and "pattern_sensitive" not in basic_assigned:
        if random.random() < 0.70:
            basic_assigned.append("pattern_sensitive")

    if "duskfield_exile" in basic_assigned and duskfield_exile_count < 2:
        if random.random() >= 0.15:
            basic_assigned.remove("duskfield_exile")
        else:
            duskfield_exile_count += 1
    elif "duskfield_exile" in basic_assigned:
        basic_assigned.remove("duskfield_exile")

    addon_assigned = random.sample(addon_pool, min(2, len(addon_pool)))

    nature_pool = npc_def.get("eligible_nature_traits", [])
    nature_assigned = random.sample(nature_pool, 1) if nature_pool else []

    assigned_traits = basic_assigned + addon_assigned + nature_assigned

    faction_value_key = npc_def.get("faction_value", "faction_value")

    save["npc_states"][npc_id] = {
        "trust": 0.0,
        "reputation": 0.5,
        faction_value_key: 0.5,
        "assigned_traits": assigned_traits,
        "tier": 0,
        "met_player": False,
        "topics_revealed": [],
        "last_interaction": "",
        "triggered": [],
    }

SAVES_DIR.mkdir(parents=True, exist_ok=True)
save_path = SAVES_DIR / "save_01.json"

with open(save_path, "w") as f:
    json.dump(save, f, indent=2)

print(json.dumps(save, indent=2))
