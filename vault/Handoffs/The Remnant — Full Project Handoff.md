

_Last updated: June 24, 2026. For a new claude.ai chat session._

---

## Who You Are Talking To

Phoebe Zhang (GitHub: KPhoebeZhang), CS student at Virginia Tech, graduating May 2027. F-1 visa, planning to use OPT + STEM OPT (up to 3 years) for industry experience before law school. Primary career target: **Thatgamecompany (TGC)** — specifically their AI-focused Full Stack Engineer role (Shanghai-posted but Phoebe wants US remote). Bilingual English/Mandarin is a genuine differentiator. The game project IS the OPT strategy — demonstrating AI engineering skills in a game context is the portfolio play.

Law school is deferred — not cancelled. If TGC or a similar role materializes, law school pushes to 2029-2030. LSAT is on hold. Job-first is the current priority.

---

## The Project: The Remnant

A 2D isometric narrative game with a custom RAG/agent backend. The AI system is used as a **development tool and dialogue infrastructure**, not at runtime. Zero runtime LLM cost. Fully deterministic dialogue via pre-written tier-gated pools. The game is being built in Godot 4.7 (isometric 2D, 64x32 tiles). The backend is Python/FastAPI/LangChain/ChromaDB.

**Repo:** github.com/KPhoebeZhang/faction-archive  
**Local path:** ~/Desktop/Unspeakable/  
**Godot project:** ~/Desktop/Unspeakable/game/  
**Obsidian vault:** ~/Desktop/Unspeakable/vault/ (read-only from Claude Code)

---

## Career Strategy

**Target role:** TGC Full Stack Engineer (AI focus) — US remote  
**Timeline:** Reach out to TGC by Spring 2027 with working demo  
**Why it fits:** Python ✓, Git ✓, LLM/AI experience ✓, bilingual ✓, game context ✓, RAG/LangChain ✓  
**Gap:** 2+ years production experience — offset by project sophistication and AI collaboration workflow  
**Portfolio pitch:** "Built a RAG pipeline over a custom lore corpus with LangGraph orchestration, faction-gated retrieval, and a FastAPI bridge to Godot 4 — zero runtime LLM cost, fully deterministic at scale"

**GitHub story:** Not yet built. Needs devlogs, meaningful commit history, and a strong README. Start this soon — recruiters look at commit history.

---

## World & Lore

### Core Thesis

Civilization's recursive learning is also its destruction mechanism. An unknown group prevented catastrophe not by stopping a specific event but by **designing a civilization structurally incapable of assembling dangerous knowledge**. The faction system is not the aftermath of collapse — it IS the containment device.

_"Becoming great will end us. Learning from our history will make us great, yet makes our mistakes harder to untangle and solve. Eventually it will be unsalvageable."_

### The Four Factions

**Ashkeep — The Record-Keepers** Snobbish, fragmented internally by clan — each family holds a different version of history and distrusts the others. Every 5 years, select Fornholt individuals are secretly observed to extract fragments closer to truth than Ashkeep's own records. Needs Fornholt to maintain superiority but won't admit it.

- Faction value: `certainty` (0-1, confidence in own records)
- High certainty: condescending, closed. Low certainty: paradoxically more revealing.

**Tidewall — The Traders** Must marry outsiders; refusal means exile to Duskfield. Once yearly, all Tidewall gather in masks never reused — exchange information, assign trade routes, then disperse. No persistent relationships. Profoundly lonely. Envious of Fornholt elder-youngling bonds.

- Faction value: `isolation` (0-1, time since genuinely recognized as individual)
- High isolation: unusually responsive to being treated as a person.

**Fornholt — The Fractured** Carry ancestral trauma directly — nonlinear, fragmented memory. Their "fortune telling" is pattern recognition through trauma, not mysticism. Some resent Ashkeep deeply and see through the extraction disguised as education.

- Faction value: `coherence` (0-1, clarity of pattern-recognition)
- High coherence: sharp and uncanny. Low coherence: fragmented, poetic, hard to parse.

**Duskfield — The Silenced** Formed from exiled Tidewall. Spread across small villages. Core values: kindness to all strangers, near-total discouragement of speech. The kindness rule ensures exiles are absorbed quietly. The silence rule ensures no one asks why. At 15, a Duskfield person may leave — rare, undocumented, quietly discouraged.

Duskfield bloodlines cross every faction, making them the only population with raw material to piece together true history. **This is why they cannot speak.** Their silence is load-bearing for the fiction that the other three factions are distinct peoples.

New Duskfield villages somehow already know how to function — unexplained, likely tied to deeper history.

- Faction value: `restraint` (0-1, proximity to breaking silence)

---

## The Protagonist

A Duskfield woman. The player character. Currently lacks a distinct voice — this is the most significant creative gap.

**Timeline:**

- Age 4: Brother born. She describes him as the most wonderful creature she had ever seen.
- Age 9: **[UNWRITTEN — CRITICAL GAP]** Inciting incident. Her brother (age 5) dies in a preventable way that hinges on absence of recorded knowledge. Something that could have been written down and wasn't, because Duskfield doesn't record things.
- Age 9-10: Doesn't process grief immediately — no vocabulary for it. Duskfield culture has no language for loss.
- Age 13: A child in a nearby village dies of the **same preventable cause**. She snaps. Becomes specifically angry: there's no record of her brother's death, nothing was learned, a second child paid for the same absence.
- Age 13-15: **[UNRESOLVED]** Sits with the anger. Possibly tests edges of silence. Relationship with parents during this period unclear. Does one parent almost reveal they understand exactly what she's feeling?
- Age 15+: Leaves Duskfield. Mechanism for departure still undetermined — a plot question, not just character.

**Open story questions (all unresolved):**

1. The age-9 incident — specific sensory detail, what happened, what knowledge would have prevented it
2. The ages 13-15 gap — parent relationship during this period
3. The departure mechanism at 15
4. Her voice — what is specific, contradictory, unmistakable about how she thinks
5. A secondary relationship with real friction — someone whose safety depends on the silence remaining intact (suggested: a Duskfield person who would lose everything if she succeeds)
6. The architects of the containment system — still active or self-perpetuating?
7. Why new Duskfield villages already know how to function

**Identified strengths to protect:**

- The antagonist's logic is airtight, not villainous — don't soften it
- Faction systems are mechanically elegant AND thematically load-bearing
- Protagonist's incentive must stay personal and specific (dead brother, second dead child) — she arrives at the philosophy, doesn't start with it

---

## NPC System Design

Three layers per NPC:

### Layer 1 — Identity (fixed, authored)

- `id`, `name`, `faction`, `generation` (first/second), `role`

### Layer 2 — States (dynamic, 0-1 scale)

**Universal:**

- `trust` — willingness to reveal lore
- `reputation` — how NPC perceives player's standing (starts 0.5)

**Faction-specific (one per NPC):**

- Duskfield: `restraint`
- Ashkeep: `certainty`
- Tidewall: `isolation`
- Fornholt: `coherence`

**Memory (structured log):**

- `met_player`: bool
- `topics_revealed`: list of strings
- `last_interaction`: string
- `triggered`: list of event IDs
- `tier`: int (0, 1, 2)

### Layer 3 — Traits (fixed at save creation, revealed over time)

**Basic traits — nurture (4 drawn from faction pool):**

_Duskfield pool:_

- `voluntary_keeper` — first generation, silence as daily choice
- `involuntary_keeper` — second generation, silence became nature
- `threshold_memory` — one specific unspeakable moment held intact
- `trauma_coping` — grief channeled into specific creative expression
- `pattern_sensitive` — notices cycles, shared with Fornholt, often precedes almost_voice
- `almost_voice` — nearly broke silence once, quieter ever since
- `duskfield_exile` — rare (15% chance, hard cap 2 per save), has seen outside

**Assignment rules:**

- If `almost_voice` assigned: 70% chance to also assign `pattern_sensitive`
- `duskfield_exile`: 15% chance, maximum 2 per save

**Nature traits — universal (1 drawn from pool of 5):**

- `tender`, `suspicious`, `curious`, `withdrawn`, `fierce`
- Affect behavioral expression and dialogue tells only — never affect trust/reputation math

**Depth tiers:**

- Tier 0: 3-5 ambient lines, no traits visible
- Tier 1: trust > 0.3 + topics_revealed ≥ 1 → 1 trait begins showing
- Tier 2: trust > 0.6 + topics_revealed ≥ 3 → second trait activates
- Tier 3: trust > 0.8 + specific flags → full depth (2-3 NPCs per faction max)

### Trust Mechanics

Universal trust gains (same for every NPC, no trait modifiers on math):

- `approach`: +0.03
- `linger`: +0.05
- `topic_trigger`: +0.08, reputation +0.05
- `easter_egg`: +0.15, reputation +0.10

---

## Interaction System Design

### Layer 1 — Ambient/Passive (no UI, automatic)

- Proximity detection — being near NPC affects state
- Companionship — cumulative time near NPC builds relationship
- Linger — staying still 4+ seconds triggers warmth response
- Receive — NPC gives something, player takes automatically

### Layer 2 — Universal UI (three buttons, always same)

- `Offer` — give something (presence in Duskfield, info in Tidewall, object in Ashkeep)
- `Interact` — two-way exchange (listen at low trust, converse at high trust)
- `Observe` — triggers protagonist's internal thought box; language sophistication progression lives here

### Layer 3 — Faction-Specific Mechanics (full-game feature, not yet built)

**Knowledge Synthesis UI (Fornholt + Ashkeep):** Two-panel drag-and-drop. Left: player's knowledge cards. Right: NPC's space. Player drags 1-2 cards in. Response shaped by faction value (coherence/certainty), trust, and which cards offered.

- Fornholt: sees _pattern_ across fragments
- Ashkeep: sees _contradiction or confirmation_ in records
- Status: **designed, not built**

### Language Sophistication Progression

Internal thought boxes evolve as protagonist travels:

- Duskfield (start): sparse, physical, pre-verbal. Sometimes music instead of text.
- After Ashkeep: categorical, record-keeping vocabulary
- After Tidewall: relational, transactional vocabulary
- After Fornholt: pattern language, nonlinear connections
- Status: **designed, not built**

---

## Dialogue Architecture

**No runtime LLM calls.** All dialogue is pre-written, stored in JSON, selected by the system.

**Fragment database** (`vault/Lore/Factions/Duskfield Opening Fragments.md`): 10 fragments written for opening scene — prose tagged with topic, tier, and faction. Ingested into ChromaDB. Used as RAG development tool for consistency checking, not at runtime.

**Dialogue pools** (`backend/data/dialogue/mother_npc.json`): Pre-written lines organized by NPC, tier, and context (ambient, on_approach). Randomly selected from matching pool.

**History synthesis (ending):** Dwarf Fortress-style template assembly from `player_knowledge` flags. No LLM. Status: **designed, not built**.

---

## Technical Architecture

### Backend Stack

- Python 3.12.4
- LangChain + langchain-text-splitters
- LangGraph (installed, not yet used for routing)
- ChromaDB (local, no API key)
- FastAPI + Uvicorn

### Backend Scripts

- `backend/ingest_fragments.py` — loads vault lore, chunks, embeds, stores in ChromaDB collection "duskfield_opening"
- `backend/query_fragments.py` — NPC-gated retrieval (filters by NPC's current tier)
- `backend/update_npc_state.py` — dev/debug tool, direct state manipulation
- `backend/process_interaction.py` — universal trust processor (approach/linger/topic_trigger/easter_egg)
- `backend/select_dialogue.py` — loads dialogue JSON, reads NPC tier, randomly selects line
- `backend/generate_save.py` — generates save_01.json with random trait assignment
- `backend/server.py` — FastAPI server, POST /interact and GET /health

### FastAPI Endpoint

```
POST /interact
Body: {"npc_id": "mother_npc", "interaction_type": "approach"}
Returns: {"npc_id": ..., "dialogue": ..., "trust": ..., "tier": ...}
```

To run: `cd ~/Desktop/Unspeakable && source .venv/bin/activate && uvicorn backend.server:app --reload --port 8000`

### Data Files

- `backend/data/npc_definitions.json` — fixed NPC identity + eligible traits
- `backend/data/save_template.json` — save file schema
- `backend/data/saves/save_01.json` — current test save (mother_npc at various trust levels depending on session)
- `backend/data/dialogue/mother_npc.json` — tier 0 and tier 1 dialogue pools
- `backend/docs/npc_values.md` — NPC value system spec
- `backend/docs/npc_traits.md` — trait pool (to be written)

### Godot Project

- Engine: Godot 4.7 stable
- Mode: Isometric 2D, tile size 64x32
- Skill: `skills/godot-claude-skills/SKILL.md` (must read before any GDScript/.tscn work)
- Scene: `game/scenes/duskfield_hut_interior.tscn`
- Scripts: `game/scripts/`
    - `BackendManager.gd` — autoload singleton, HTTP calls to FastAPI, emits `interaction_complete` signal
    - `PlayerController.gd` — CharacterBody2D, WASD isometric movement, E key interaction
    - `FloorPainter.gd` — programmatically paints 15x15 floor grid on ready
    - `NPCInteraction.gd` — Area2D proximity detection, wires to BackendManager
    - `DialogueUI.gd` — CanvasLayer UI box, shows dialogue 4 seconds then fades

### Currently Working End-to-End

```
Player presses E near MotherNPC
→ NPCInteraction detects proximity (Area2D, radius 80)
→ BackendManager.call_interact("mother_npc", "linger")
→ HTTP POST to localhost:8000/interact
→ FastAPI runs process_interaction (trust updates)
→ FastAPI runs select_dialogue (tier-gated line picked)
→ Returns JSON with dialogue, trust, tier
→ BackendManager emits interaction_complete signal
→ NPCInteraction receives signal
→ DialogueUI.show_dialogue("Mother", dialogue)
→ Dialogue box appears bottom of screen for 4 seconds
```

**First successful in-game dialogue:** "She shifts slightly, making room beside her." ✓

---

## Godot Scene Current State

Scene tree of `duskfield_hut_interior.tscn`:

```
DuskfieldHutInterior (Node2D) — root, FloorPainter.gd attached
├── Floor (TileMapLayer) — stone floor tiles, y_sort_enabled
│   └── TileSet: tile_stone_floor.png, 64x32 isometric
├── NPCs (Node2D)
│   └── MotherNPC (Area2D) — NPCInteraction.gd, z_index=10
│       ├── CollisionShape2D (CircleShape2D, radius 80)
│       ├── ColorRect (tan placeholder, 16x24)
│       └── Label ("Mother")
├── Player (CharacterBody2D) — PlayerController.gd, z_index=10
│   ├── Camera2D (follows player, zoom 2x)
│   ├── CollisionShape2D (RectangleShape2D 16x8)
│   └── ColorRect (red placeholder, 16x24)
└── UI (CanvasLayer) — DialogueUI.gd
```

---

## Art Pipeline

- **Tool:** Aseprite (purchased, installed at /Applications/Aseprite.app)
- **AI generation:** PixelLab MCP (installed in Claude Code)
- **Style:** Isometric pixel art, 64x32 tiles, muted cold palette, Little Nightmares-inspired dark/rainy/cozy
- **Current assets:** 4 PixelLab-generated placeholder tiles (tile_stone_floor, tile_stone_cracked, tile_earth_dark, tile_stone_mossy)
- **Workflow:** PixelLab MCP generates base → Aseprite cleanup → Godot import
- **Character sprites:** Not yet created. Plan: Phoebe draws protagonist idle pose in Aseprite, PixelLab generates walk/run animation frames, Phoebe cleans up
- **Art chat:** Separate claude.ai chat documents art direction decisions (cold ambient palette, firelight warmth, Fallout meets Rain World aesthetic, Duskfield restraint)

---

## Obsidian Vault Structure

```
vault/
├── Lore/
│   ├── Core Thesis.md — containment thesis, full detail
│   ├── Factions/
│   │   ├── Ashkeep.md
│   │   ├── Tidewall.md
│   │   ├── Fornholt.md
│   │   └── Duskfield.md
│   ├── Protagonist/ — overview and timeline
│   ├── Open Questions/ — 7 numbered unresolved story questions
│   └── Game Design/
│       └── Interaction System.md — full interaction design
├── Technical/
│   ├── NPC System.md — three-layer NPC architecture
│   ├── Belief Graph.md — (planned, not yet written)
│   └── Glossary.md — technical terms in plain language
├── Progress/
│   └── Progress Log.md — session-by-session log
└── Career/
    └── TGC Mapping.md — JD requirements vs project evidence
```

---

## What's Built vs Designed vs Unbuilt

### Built and Working ✓

- Python RAG pipeline (ChromaDB, LangChain)
- Fragment ingestion from vault lore
- NPC-gated retrieval (tier filtering)
- Trust + reputation + faction_value state system
- Interaction processor (universal trust gains)
- Dialogue selection (tier-gated pre-written pools)
- Save generation with random trait assignment
- FastAPI server (/interact, /health)
- Godot project (isometric, pixel art settings)
- Player movement (WASD isometric)
- Camera2D following player
- Mother NPC placeholder with proximity detection
- Dialogue UI box
- Full pipeline working: E key → backend → dialogue on screen

### Designed, Not Yet Built ⚙

- Linger detection (4-second stillness → trust gain, automatic)
- Automatic approach trust accumulation (proximity time, not just E key)
- Father NPC with dialogue pool
- Camera bounds (player can walk off floor)
- Interaction UI buttons (Offer, Interact, Observe)
- Player sprite (red rectangle placeholder)
- NPC sprites (rectangle placeholders)
- player_knowledge accumulation in game
- Topic triggers wired to in-game events
- Internal thought system (Observe verb)
- Language sophistication progression
- Knowledge Synthesis UI (Fornholt + Ashkeep drag-drop)
- Belief graph (fragment compatibility system)
- Template-based history assembly (ending)
- Opening hut interior scene (separate from outdoor floor)
- Main menu
- Sound and music

### Designed at High Level, Architecture TBD 📐

- Map structure: hub-and-spoke per faction
- Duskfield map: dense authored hub, 4 AI-populated surrounding chunks
- Wave function collapse for chunk population
- NPC trait expression through behavioral tells (not UI labels)
- Easter egg trust moments
- Save/load system
- Multiple NPCs per faction (target: 10 Duskfield, 20-30 full game)

---

## CLAUDE.md Summary

Key rules Claude Code follows:

- `vault/` is READ ONLY — never edit lore files
- Godot 4 only — never use Godot 3 syntax
- Read `skills/godot-claude-skills/SKILL.md` before any GDScript/.tscn work
- Backend code in `backend/` only
- `game/` folder for Godot only
- Small commits, one unit of work per commit
- Detailed specs in referenced docs, not inline in CLAUDE.md

---

## Immediate Next Priorities (in order)

1. **Linger detection** — 4-second stillness near NPC → `process_interaction("linger")` fires automatically. This is the opening scene's core mechanic (mother putting hand on back).
2. **Approach trust accumulation** — being in proximity range should slowly increment trust without E key. Rain World style.
3. **Father NPC** — second NPC with own dialogue pool, placed in hut interior.
4. **Camera bounds** — prevent player walking off floor grid.
5. **Interaction UI** — Offer/Interact/Observe buttons appearing near NPC.
6. **Player sprite via PixelLab** — replace red rectangle.
7. **Mother/Father sprites via PixelLab** — replace tan rectangles.
8. **Opening hut interior scene** — player wakes up inside, mother is outside, the actual opening moment designed months ago.

---

## Working Agreements & Preferences

- Progress before perfection — finish then polish, not perfect then move
- Small Claude Code prompts, one unit of work, verifiable output
- Research before building — always look up how comparable games solved it
- Phoebe handles: all lore/creative writing (in Obsidian), art direction, game design decisions
- Claude Code handles: technical scaffolding, GDScript, Python, JSON structures
- This chat (claude.ai) handles: design decisions, research synthesis, architecture, prompting strategy
- No diagrams unless explicitly requested
- When uncertain about implementation: research first, then ask Phoebe to decide
- Mode 2 available: Noor (warm, structured, motivating) and Alfred (blunt, risk-aware, research-first) personas on request

---

_End of handoff. Repo: github.com/KPhoebeZhang/faction-archive_