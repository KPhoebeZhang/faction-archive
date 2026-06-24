
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

## June 24, 2026

### Done
- Full backend pipeline confirmed working end to end
- Fragment ingestion, NPC tier gating, trust progression 
  all verified
- FastAPI server with /interact and /health endpoints
- Godot 4.7 project with isometric 64x32 stone floor tiles
- Player CharacterBody2D with WASD isometric movement
- Camera2D following player
- MotherNPC Area2D with proximity detection
- DialogueUI box displaying backend response
- First in-game dialogue line displayed:
  "She shifts slightly, making room beside her."
- BackendManager autoload connecting Godot to FastAPI
- PixelLab MCP installed and generating tiles

### Current state (honest)
- One NPC, one dialogue pool, one scene
- No player sprite (red rectangle placeholder)
- No NPC sprite (tan rectangle placeholder)
- No ambient/automatic trust accumulation (only E key)
- No linger detection (4-second stillness mechanic unbuilt)
- No internal thought system (Observe verb unbuilt)
- No Offer verb UI
- No Interact verb UI
- No player_knowledge accumulation in game
- No topic triggers wired to save file
- No father NPC
- No opening hut interior (currently outdoors floor)
- No camera bounds (player can walk off floor)
- Floor grid hardcoded, not a proper map
- Dialogue box unstyled (placeholder panel)
- No sound, no music
- No main menu or game loop

### Next priorities
1. Linger detection — 4 second stillness → trust gain
2. Automatic approach trust (proximity, not just E key)
3. Father NPC placeholder with own dialogue pool
4. Camera bounds so player can't walk off floor
5. Basic interaction UI (Offer, Interact, Observe buttons)
6. Player sprite via PixelLab MCP
7. Mother/Father NPC sprites via PixelLab MCP

### Blocked on
- Nothing currently — all systems have a clear next step