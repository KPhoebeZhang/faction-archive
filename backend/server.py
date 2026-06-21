import sys
from pathlib import Path

# Allow sibling imports (process_interaction, select_dialogue) when
# invoked as `uvicorn backend.server:app` from the project root.
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from process_interaction import process_interaction
from select_dialogue import select_dialogue

app = FastAPI()


class InteractRequest(BaseModel):
    npc_id: str
    interaction_type: str


@app.post("/interact")
def interact(req: InteractRequest):
    try:
        npc = process_interaction(req.npc_id, req.interaction_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    dialogue = select_dialogue(req.npc_id, "ambient")
    return {
        "npc_id": req.npc_id,
        "dialogue": dialogue,
        "trust": npc["trust"],
        "tier": npc["tier"],
    }


@app.get("/health")
def health():
    return {"status": "ok"}
