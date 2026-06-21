# NPC System Design

## Overview
Each NPC has three distinct layers that work together:
- Identity: fixed, authored, never changes
- Traits: assigned at save creation, revealed over time
- States: dynamic, change during play

## Layer 1 — Identity (fixed)
Fields:
- id: unique string e.g. "mother_npc"
- name: display name
- faction: "duskfield" / "ashkeep" / "tidewall" / "fornholt"
- generation: "first" (chose silence) or "second" (born into it)
- role: their function in the world e.g. "parent", "elder", "trader"

## Layer 2 — Traits (fixed at save creation)

### Basic traits (4 drawn from faction pool — nurture)
Duskfield pool:
- voluntary_keeper: first generation, silence as daily choice
- involuntary_keeper: second generation, silence became nature
- threshold_memory: one specific unspeakable moment held intact
- trauma_coping: grief channeled into specific creative expression
- pattern_sensitive: notices cycles, shared with Fornholt, 
  often precedes almost_voice
- almost_voice: nearly broke silence once, quieter ever since
- duskfield_exile: rare, has seen outside, exists between worlds

### Add-on traits (2 drawn from universal pool — nature)
Faction-agnostic personality traits, examples:
- stubborn, tender, suspicious, curious, withdrawn, fierce
These make two NPCs with identical basic traits feel like 
different people.

### Trait assignment rules
- 4 basic traits drawn randomly from faction pool at save creation
- If almost_voice is assigned, weight toward also assigning 
  pattern_sensitive (not guaranteed, just more likely)
- duskfield_exile assigned to maximum 1-2 NPCs per save
- 2 add-on traits drawn from universal pool, fully random
- All traits latent at tier 0 — behaviorally inert until unlocked
- duskfield_exile: 15% assignment chance, hard cap of 2 per save

## Layer 3 — States (dynamic)

### Shared states (all NPCs, 0.0 to 1.0 scale)
- trust: willingness to reveal lore to player
- awareness: felt sense something is wrong with the world

### Faction-specific states (0.0 to 1.0 scale)
- Duskfield: restraint (proximity to breaking silence)
- Ashkeep: certainty (confidence in own records)
- Tidewall: isolation (time since genuinely recognized)
- Fornholt: coherence (clarity of pattern-recognition)

### Memory (structured log, not a scale)
- met_player: bool
- topics_revealed: list of strings
- last_interaction: string description
- triggered: list of triggered event ids

## Depth Tiers
NPCs unlock deeper content as relationship develops:
- Tier 0: name, faction, 3-5 ambient lines, no traits visible
- Tier 1: trust > 0.3 + 3 interactions → 1 trait begins 
  showing behavioral tells, 5-8 lines
- Tier 2: trust > 0.6 + 8 interactions → second trait 
  activates, memory flags start mattering
- Tier 3: trust > 0.8 + specific flags → full depth, 
  rare, maximum 2-3 NPCs per faction written to this level

## Belief Graph (coming later)
Fragment selection system — see vault/Technical/Belief Graph.md
when ready.
