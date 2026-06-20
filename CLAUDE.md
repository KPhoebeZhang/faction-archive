# The Remnant

A RAG/agent system grounded in original fantasy lore, built as a 
portfolio project targeting AI engineering roles. Demonstrates 
retrieval-augmented generation, LangGraph orchestration, and 
faction-based knowledge architecture.

## Stack
- Python 3.12.4
- LangChain, LangGraph, ChromaDB
- Anthropic API (not yet configured — API key pending)

## Godot
- Engine: Godot 4 only — never Godot 3 syntax
- Skill: read skills/godot-claude-skills/SKILL.md 
  before any GDScript or .tscn work
- Project: game/ (not created yet — do not create)
- Setup details: see docs/godot-setup.md

## Structure
- vault/        Lore, story notes, progress log — READ ONLY
                Never edit vault/ files unless explicitly asked
- backend/      Python RAG/agent code — all technical work goes here
- game/         Godot project — does not exist yet, do not create
- requirements.txt  Source of truth for dependencies
- .venv/        Local virtual environment — never commit

## Commands
- Activate environment: source .venv/bin/activate
- Install dependencies: pip install -r requirements.txt
- Verify environment: python -c "import langchain, langgraph, 
  chromadb; print('ok')"

## Architecture (as built so far)
Two-layer AI system:
- Layer 1 (traditional game AI): hidden NPC values + 
  JSON save system. See backend/docs/npc_values.md
- Layer 2 (LLM synthesis): triggered only when value thresholds 
  are crossed. Reserved for revelation moments and ending generation.

Game ↔ backend connection: one API call (FastAPI). 
Game sends question + player state. Backend returns generated text.

## Conventions
- Small commits, one unit of work per commit
- Backend code lives in backend/ only
- vault/ is creative/lore content — edited in Obsidian, not here
- No application code outside backend/ until game/ phase begins

## Current milestone
Retrieval-only script: backend/test_rag.py
Load vault/Lore/Factions/Duskfield.md → chunk → embed → 
store in ChromaDB → retrieve top match for a test question → 
print result. No LLM call yet.
