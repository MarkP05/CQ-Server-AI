from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from inputs import run_inputs_mode
from parsons import run_parsons_mode

app = FastAPI()

# ---------- Request Models ----------

class InputsRequest(BaseModel):
    player_input: str
    solution: str

class ParsonsRequest(BaseModel):
    player_input: str
    solution: str

# ---------- Endpoints ----------

@app.post("/inputs")
def inputs_endpoint(data: InputsRequest):
    try:
        feedback = run_inputs_mode(
            player_input=data.player_input,
            sample_solution=data.solution
        )
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/parsons")
def parsons_endpoint(data: ParsonsRequest):
    try:
        feedback = run_parsons_mode(
            player_input=data.player_input,
            sample_solution=data.solution
        )
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))