
## June 2026 (Session 2)
### Done
- NPC system design doc written
- npc_definitions.json and save_template.json created
- generate_save.py working — trait assignment with 
  almost_voice weighting rule

### Blocked
- Nothing currently

### Next
- Write first 10-15 Duskfield fragments
- Build fragment database structure

### Layer 1 — Faction-specific traits (nurture)
What Duskfield shaped them into. Assigned randomly at save creation from the faction pool. Revealed gradually through tier progression. For Duskfield: `voluntary_keeper`, `involuntary_keeper`, `threshold_memory`, `trauma_coping`, `pattern_sensitive`, `almost_voice`, `duskfield_exile`. Other factions will have their own pools.
### Layer 2 — Shared Mechanic Values (all factions, dynamic)

#### Universal (all NPCs, 0-1 scale)

- `trust` — willingness to reveal lore to player
- `reputation` — how this NPC perceives the player's standing in the world. Starts neutral (0.5). Actions that align with faction values raise it, actions that violate them lower it.

#### Faction-specific (0-1 scale, one per faction)

- Duskfield: `restraint`
- Ashkeep: `certainty`
- Tidewall: `isolation`
- Fornholt: `coherence`

#### Memory (structured log, not a scale)

- `met_player`: bool
- `topics_revealed`: list of strings
- `last_interaction`: string
- `triggered`: list of triggered event ids

### Layer 3 — Nature Traits (all factions, fixed)

Universal pool of 5, same across every faction.  
Assigned at save creation, never change.  
Affect behavioral expression and dialogue tells only —  
never affect trust/reputation math directly.

- `tender`
- `suspicious`
- `curious`
- `withdrawn`
- `fierce`

## June 2026 (Session 2 continued)
### Done
- Fragment ingestion working on real lore
- NPC tier gating confirmed
- Trust + reputation + faction_value structure finalized
- Nature traits (5 universal) added to definitions
- process_interaction.py — universal trust system
- FastAPI server running — /interact endpoint working
- Full pipeline: interaction → trust → dialogue → JSON

### Next
- Connect Godot to FastAPI via HTTP request
- Player character placeholder in opening scene