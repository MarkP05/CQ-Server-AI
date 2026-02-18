# ai_pipeline.py
from inputs import run_evaluator
import os

PLAYER_INPUT_FILE = os.path.join(os.path.dirname(__file__), "player_input.txt")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "ai_feedback.txt")

def process_text(input_text: str) -> str:
    with open(PLAYER_INPUT_FILE, "w", encoding="utf-8") as f:
        f.write(input_text)

    run_evaluator()

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        return f.read()
