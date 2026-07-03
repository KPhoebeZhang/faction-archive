# The Remnant

A 2D isometric narrative game (Godot 4) with a custom RAG/agent 
backend, built as a portfolio project targeting AI engineering 
roles. Zero runtime LLM cost — dialogue is pre-written and 
tier-gated, selected via trust/relationship state. RAG is a 
development tool for lore consistency, not a runtime component.

## Environments
- Mac (primary): everything — Godot, Aseprite, backend, 
  visual testing. Path: ~/Desktop/Unspeakable
- VPS (backup, used when away from home): backend/Python 
  work only. Cannot run Godot editor or test the game 
  visually — do not attempt GUI tasks there.

Session discipline (critical with two machines):
- ALWAYS start with: git pull origin main
- ALWAYS end with: git push origin main

## Stack
- Python 3.12.4, FastAPI, Uvicorn
- LangChain, LangGraph, ChromaDB (local embeddings, no API key)
- Godot 4.7, GDScript
- Anthropic API (not yet configured — dev-tool use only)

## Structure
- vault/        Lore, story notes, progress log — READ ONLY
- backend/      Python RAG/agent/API code
- game/         Godot 4 project (EXISTS — isometric 2D)
- requirements.txt  Source of truth for Python dependencies

## Godot
- Engine: Godot 4.7 only — never Godot 3 syntax
- Skill: read skills/godot-claude-skills/SKILL.md before 
  any GDScript or .tscn work
- Mode: Isometric 2D pixel art, tile size 64x32
- Setup details: docs/godot-setup.md

## Running the stack
- Backend: source .venv/bin/activate && 
  uvicorn backend.server:app --reload --port 8000
- Godot: open game/project.godot in Godot editor, press F5
- Both must run simultaneously for the game to connect to backend

## Architecture
Three-layer NPC system — see vault/Technical/NPC System.md
Full pipeline (working): Godot player action → BackendManager.gd 
(HTTP) → FastAPI /interact → process_interaction → 
select_dialogue → JSON response → DialogueUI.gd displays line

## Conventions
- Small commits, one unit of work per commit
- vault/ edited in Obsidian only, never by Claude Code
- Full project state: vault/Handoffs/ (read for context on 
  a new session)

## Current milestone
Working: RAG pipeline, NPC trust/tier system, FastAPI server, 
Godot scene with player movement + mother NPC + dialogue UI.
Next: linger detection (4-second stillness trigger)
