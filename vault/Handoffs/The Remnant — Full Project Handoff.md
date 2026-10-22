

_Last updated: October 11, 2026. For a new claude.ai chat session._

> **What changed since the June 24 version (design-focused update):**
> 
> - New narrative pillar: **there is no single true history — the protagonist authors it.** Recording is an act of power. (See World & Lore → The Authorship Layer, and Protagonist.)
> - **The ending is now designed:** the protagonist dies and becomes record; an epilogue shows what became of each NPC she touched. Mechanic decided: **accumulate silently, witness at the end — no drag-and-drop arranging.** (See The Ending.)
> - **Production framing:** the project is in **pre-production**, and the single **vertical slice is the opening.**(See Production Status.)
> - **Team structure:** solo dev running six studio-role "hats," now documented in a Role Charter. (See Team Structure.)
> - **Build status updated:** linger detection and the mother's back-rub beat are now **built**, not just designed. Known bugs noted.

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

## Production Status

The project is in **pre-production**. The job of this phase is to remove uncertainty — not only what the game is, but how it gets built — and to finish **one vertical slice** that proves the pipeline end to end.

**The vertical slice is the opening:** player wakes in the hut → meets the Mother → the linger-to-back-rub beat works, with a real sprite, grounded in the age-9 backstory. One room, one NPC, one complete emotional moment at near-final quality.

**Parked until production** (deliberately out of the slice): the ending mechanic, the other three factions, the belief graph, and the Observe/internal-thought verb. These are designed or sketched, not built, and building them now would be horizontal drift against an empty dataset.

---

## Team Structure

The Remnant is a solo project run as if it had a studio team, with Phoebe time-slicing six roles ("hats"), one per work block: **Producer/PM, Game Designer, Writer/Narrative Designer, Gameplay Programmer (Claude Code), Artist, QA.** Each role has a fixed identity and a running per-session log, documented in a Google Drive **Role Charter** and per-role folders. The **Producer hat** opens and closes every session, picks the one task, and holds veto power over scope — it is the discipline that keeps the project moving forward instead of sideways.

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

### The Authorship Layer (new)

There is no single true history. No one alive knows what actually happened; people believe what they choose to believe, and the factions each hold incompatible versions precisely because the truth was never recorded. Into that vacuum steps the protagonist — the first record-keeper the world has had. She does not **uncover** the truth. She **authors** it. What she chooses to write down becomes what happened, and therefore shapes what happens next. Recording is not neutral preservation; it is an act of power, the single most consequential act in a world built to prevent exactly that.

This reframes the whole arc. The player is not solving a mystery toward one correct answer. The player is deciding what is remembered — and living with the weight of that authority. History becomes the way the dead are honored and the living are bound.

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

A Duskfield woman. The player character. Currently lacks a distinct voice — this is the most significant creative gap, and it now carries extra weight: her voice is the instrument of authorship. How she notices, names, and records is the game's central act.

**Timeline:**

- Age 4: Brother born. She describes him as the most wonderful creature she had ever seen.
- Age 9: **[UNWRITTEN — CRITICAL GAP]** Inciting incident. Her brother (age 5) dies in a preventable way that hinges on absence of recorded knowledge. Something that could have been written down and wasn't, because Duskfield doesn't record things.
- Age 9-10: Doesn't process grief immediately — no vocabulary for it. Duskfield culture has no language for loss.
- Age 13: A child in a nearby village dies of the **same preventable cause**. She snaps. Becomes specifically angry: there's no record of her brother's death, nothing was learned, a second child paid for the same absence.
- Age 13-15: **[UNRESOLVED]** Sits with the anger. Possibly tests edges of silence. Relationship with parents during this period unclear. Does one parent almost reveal they understand exactly what she's feeling?
- Age 15+: Leaves Duskfield. Mechanism for departure still undetermined — a plot question, not just character.

**The through-line (authorship):** she arrives, through the dead brother and the second dead child, at the conviction that the unrecorded must be recorded. She becomes the first record-keeper not out of philosophy but out of grief. The philosophy follows the loss — she does not start with it.

**Open story questions (all unresolved):**

1. The age-9 incident — specific sensory detail, what happened, what knowledge would have prevented it
2. The ages 13-15 gap — parent relationship during this period
3. The departure mechanism at 15
4. Her voice — what is specific, contradictory, unmistakable about how she thinks (now doubly important: it is the voice of the record)
5. A secondary relationship with real friction — someone whose safety depends on the silence remaining intact (suggested: a Duskfield person who would lose everything if she succeeds)
6. The architects of the containment system — still active or self-perpetuating?
7. Why new Duskfield villages already know how to function

**Identified strengths to protect:**

- The antagonist's logic is airtight, not villainous — don't soften it
- Faction systems are mechanically elegant AND thematically load-bearing
- Protagonist's incentive must stay personal and specific (dead brother, second dead child) — she arrives at the philosophy, doesn't start with it

---

## The Ending (newly designed)

The protagonist dies, and in dying **becomes record** — she is now remembered through the history she authored. This closes the loop: the one who spent her life recording others is finally recorded herself.

**The epilogue:** a small window with music and a rolling script/credits sequence showing the people the player interacted with, and how their histories play out after she is gone. It is proof that her recording mattered — the lives she touched continue along paths her authorship helped set.

**Mechanic decision — witness, don't arrange.** Earlier designs imagined the player actively arranging knowledge fragments to assemble history (a drag-and-drop "Knowledge Synthesis" UI). That is now set aside, because hands-on arranging breaks the quiet, immersive Rain World feeling the game is built around. Instead:

- **Accumulate silently underneath.** As the player interacts, `player_knowledge` builds in the background, Dwarf Fortress / Rain World style — a substrate the player never manipulates directly.
- **Witness at the end.** The accumulated record resolves into the epilogue. The player watches what their play produced; they do not assemble it on a board.
- **Authored prose, not template-stitching.** The history and the characters' fates read as written prose rather than mechanically stitched template fragments. (Open: exactly how the authored text is produced and how the final still-frames are presented — leaning toward still-frames + text + music rather than full animation.)

**Status: designed, not built.** Do not build the ending during the opening slice.

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

### Fragment schema & the belief graph (build discipline)

The fragment schema is **locked**: `id`, `topic`, `tier`, `faction`, `trait_affinity`, `text`, with `compatible_beliefs` and `excludes` reserved (left empty for now). `trait_affinity` weights retrieval toward the fragment matching an NPC's trait, giving character-appropriate behavior without per-NPC authoring — and it works with no belief graph required.

The **belief graph** (keeping an NPC's worldview coherent via `compatible_beliefs`/`excludes`) is **designed but unvalidated.** Firm decision: **do not build the belief-graph logic until ~30-50 real fragments exist** to test whether the tagging burden is tractable. Write content to the locked schema now; validate before building the system. (Full detail: Growth & Memory design doc.)

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

### Layer 3 — Faction-Specific Mechanics (reconsidered)

**Knowledge Synthesis UI (Fornholt + Ashkeep):** originally a two-panel drag-and-drop where the player drags knowledge cards into an NPC's space and gets a faction-shaped response.

- **Status: reconsidered, likely cut.** The hands-on arranging conflicts with the witness-don't-arrange decision behind the ending (see The Ending). Accumulation now happens silently; the player reads patterns through dialogue and observation rather than manipulating a board. Keep the _idea_ of faction-shaped reading (Fornholt sees pattern, Ashkeep sees contradiction/confirmation) but express it in-fiction, not as a drag-drop panel. Revisit only if a compelling, immersion-preserving form appears.

### Language Sophistication Progression

Internal thought boxes evolve as protagonist travels:

- Duskfield (start): sparse, physical, pre-verbal. Sometimes music instead of text.
- After Ashkeep: categorical, record-keeping vocabulary
- After Tidewall: relational, transactional vocabulary
- After Fornholt: pattern language, nonlinear connections
- Status: **intent only — mechanism undecided, Observe verb not built.** Do not spec until prototyped.

---

## Dialogue Architecture

**No runtime LLM calls.** All dialogue is pre-written, stored in JSON, selected by the system.

**Fragment database** (`vault/Lore/Factions/Duskfield Opening Fragments.md`): 10 fragments written for opening scene — prose tagged with topic, tier, and faction. Ingested into ChromaDB. Used as RAG development tool for consistency checking, not at runtime.

**Dialogue pools** (`backend/data/dialogue/mother_npc.json`): Pre-written lines organized by NPC, tier, and context (ambient, on_approach). Randomly selected from matching pool.

**History synthesis (ending):** authored prose over `player_knowledge`, accumulated silently and resolved into the epilogue (see The Ending). No LLM at runtime. Earlier Dwarf-Fortress-style pure template assembly is softened toward authored text. Status: **designed, not built**.

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
- `backend/generate_save.py` — generates save_01.json with random trait assignment (known bug: `tender` appears in two pools — fix pending)
- `backend/server.py` — FastAPI server, POST /interact and GET /health

### FastAPI Endpoint

```
POST /interact
Body: {"npc_id": "mother_npc", "interaction_type": "approach"}
Returns: {"npc_id": ..., "dialogue": ..., "trust": ..., "tier": ...}
```

To run: `cd ~/Desktop/Unspeakable && source .venv/bin/activate && uvicorn backend.server:app --reload --port 8000`

> **Note:** the server MUST be running or the in-game dialogue box fails silently (Godot HTTPRequest result:2, code:0 = can't connect). First debug step if dialogue stops appearing: is the server up?

### Data Files

- `backend/data/npc_definitions.json` — fixed NPC identity + eligible traits
- `backend/data/save_template.json` — save file schema
- `backend/data/saves/save_01.json` — current test save
- `backend/data/dialogue/mother_npc.json` — tier 0 and tier 1 dialogue pools
- `backend/docs/npc_values.md` — NPC value system spec
- `backend/docs/npc_traits.md` — trait pool (to be written)

### Godot Project

- Engine: Godot 4.7 stable
- Mode: Isometric 2D, tile size 64x32
- Skill: `skills/godot-claude-skills/SKILL.md` (must read before any GDScript/.tscn work)
- Scene: `game/scenes/duskfield_hut_interior.tscn`
- Scripts: `game/scripts/`
    - `BackendManager.gd` — autoload singleton, HTTP calls to FastAPI, emits `interaction_complete` signal. **Signal signature is load-bearing:** `interaction_complete(npc_id: String, dialogue: String, trust: float, tier: int)` — trust is float, tier is int. This typing has regressed before and broken the dialogue box; keep it exact.
    - `PlayerController.gd` — CharacterBody2D, WASD isometric movement (checks both `Input.is_key_pressed` and `ui_*` actions), E key interaction
    - `FloorPainter.gd` — programmatically paints floor grid on ready
    - `NPCInteraction.gd` — Area2D proximity (radius 80); linger logic and the back-rub beat live here
    - `DialogueUI.gd` — CanvasLayer UI box, shows dialogue ~4 seconds then fades. Debug print statements kept in the chain intentionally.

### Currently Working End-to-End

```
Player near MotherNPC (E key or linger)
→ NPCInteraction detects proximity (Area2D, radius 80)
→ BackendManager.call_interact("mother_npc", "linger")
→ HTTP POST to localhost:8000/interact
→ FastAPI runs process_interaction (trust updates)
→ FastAPI runs select_dialogue (tier-gated line picked)
→ Returns JSON with dialogue, trust, tier
→ BackendManager emits interaction_complete signal
→ DialogueUI.show_dialogue("Mother", dialogue)
→ Dialogue box appears for ~4 seconds
```

**First successful in-game dialogue:** "She shifts slightly, making room beside her." ✓  
**Built opening beat:** linger 1 → observation line; linger 2 → the mother's back-rub gesture ("Her hand finds your back. Just for a moment."). Committed (3c486c9).

---

## Godot Scene Current State

Scene tree of `duskfield_hut_interior.tscn`:

```
DuskfieldHutInterior (Node2D) — root, FloorPainter.gd attached
├── Floor (TileMapLayer) — stone floor tiles, y_sort_enabled
│   └── TileSet: tile_stone_floor.png, 64x32 isometric
├── NPCs (Node2D)
│   └── MotherNPC (Area2D) — NPCInteraction.gd, z_index=10, z_as_relative=false
│       ├── CollisionShape2D (CircleShape2D, radius 80)
│       ├── ColorRect (tan placeholder, 16x24)
│       └── Label ("Mother")   ← name currently hardcoded (known issue)
├── Player (CharacterBody2D) — PlayerController.gd, z_index=10, position (320,180)
│   ├── Camera2D (follows player, zoom 2x)
│   ├── CollisionShape2D (RectangleShape2D 16x8)
│   └── ColorRect (red placeholder, 16x24)
└── UI (CanvasLayer) — DialogueUI.gd
```

---

## Art Pipeline

- **Tool:** Aseprite (purchased, installed at /Applications/Aseprite.app)
- **AI generation:** PixelLab MCP (installed in Claude Code; the separate "pixel plugin" was dropped after config failures)
- **Style:** Isometric pixel art, 64x32 tiles, muted cold palette, Little Nightmares-inspired dark/rainy/cozy; Fallout-meets-Rain-World mood, firelight warmth against cold ambient
- **Current assets:** 4 PixelLab-generated placeholder tiles (tile_stone_floor, tile_stone_cracked, tile_earth_dark, tile_stone_mossy)
- **Workflow:** PixelLab MCP generates base → Aseprite cleanup → Godot import
- **Character sprites:** Not yet created. Plan: Phoebe draws protagonist idle pose in Aseprite, PixelLab generates walk/run frames, Phoebe cleans up
- **Discipline:** lock a 1-page style reference before generating, so assets stay consistent instead of drifting per asset

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
│   │   ├── Duskfield.md
│   │   └── Duskfield Opening Fragments.md — 10 opening RAG fragments
│   ├── Protagonist/ — overview and timeline
│   ├── Open Questions/ — numbered unresolved story questions
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

> **To write into the vault (not yet recorded):** the Authorship Layer, the death-and-epilogue Ending, and resolutions to the open protagonist questions. These were decided in conversation and still need to land in Obsidian.

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
- Full pipeline working: E key / linger → backend → dialogue on screen
- **Linger detection (4-second stillness → linger interaction)** — now built
- **Mother's back-rub beat (linger 1 observation, linger 2 gesture)** — now built, lightly tested

### Known Bugs / Rough Edges (QA log)

- Linger cooldown (30s) not holding reliably — can double-fire
- NPC name "Mother" hardcoded (should come from NPC data)
- `generate_save.py` double-assignment bug (`tender` in two pools)
- Tier promotion has a dead end past tier 1 in the current test flow
- README is a one-liner — needs the GitHub story

### Designed, Not Yet Built ⚙

- Automatic approach trust accumulation (proximity time, not just a discrete event) — Rain World style
- Father NPC with dialogue pool
- Camera bounds (player can walk off floor)
- Interaction UI buttons (Offer, Interact, Observe)
- Player sprite (red rectangle placeholder)
- NPC sprites (rectangle placeholders)
- player_knowledge accumulation in game (the silent substrate behind the ending)
- Topic triggers wired to in-game events
- The Ending: silent accumulation → epilogue (still-frames + text + music)
- Main menu, sound and music

### Designed but Unvalidated / Intent Only 📐

- Belief graph (fragment compatibility) — validate against ~30-50 real fragments before building
- Internal thought system (Observe verb) + language sophistication progression — intent only, mechanism undecided
- Map structure: hub-and-spoke per faction; Duskfield dense authored hub + AI-populated surrounding chunks; wave function collapse for chunk population
- NPC trait expression through behavioral tells (not UI labels)
- Save/load system
- Multiple NPCs per faction (target: ~10 Duskfield, 20-30 full game)

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

> **Note:** CLAUDE.md is out of date — it still says `game/` does not exist and describes an old two-layer "LLM synthesis" architecture. It needs a rewrite to match the current zero-runtime-LLM design and the existing Godot project.

---

## Immediate Next Priorities (vertical slice first)

The slice is the opening. Finish it before anything in production scope.

1. **Fix the linger double-fire** — make the 30s cooldown hold, so the back-rub beat fires once and cleanly.
2. **De-hardcode the NPC name** — pull "Mother" from NPC data.
3. **Player sprite via PixelLab** — replace the red rectangle with a real protagonist idle pose.
4. **Mother sprite via PixelLab** — replace the tan rectangle.
5. **Opening hut interior polish** — the wake-up moment, grounded in the age-9 backstory, as the complete emotional beat.
6. **Write the new pillars into the vault** — Authorship Layer, the Ending, and the resolved protagonist questions.

Parked for production (do not start during the slice): approach-time trust, Father NPC, interaction UI buttons, the ending build, belief graph, Observe verb, other factions.

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
- Six-hat role structure with a Producer hat that holds veto over scope (see Team Structure)
- Mode 2 available: Noor (warm, structured, motivating) and Alfred (blunt, risk-aware, research-first) personas on request

---

_End of handoff. Repo: github.com/KPhoebeZhang/faction-archive_