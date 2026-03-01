from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from inputs import run_inputs_mode

app = FastAPI()

# ---- Request Model ----

class InputsRequest(BaseModel):
    player_input: str
    solution: str

# ---- Endpoint ----

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