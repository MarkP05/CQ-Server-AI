import os
from groq import Groq

# ---- INITIALIZE GROQ CLIENT ----
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---- PARSONS PROMPT ----
def build_prompt(player_input, sample_solution):
    return f"""
You are an AI tutor for a young beginner (age 8–12).

This is a PARSONS PROBLEM. The student reorders shuffled lines of code.

PLAYER INPUT (student’s chosen order of lines):
=====================
{player_input}
=====================

SAMPLE SOLUTION (contains the problem description AND correct order):
=====================
{sample_solution}
=====================

TASK:
You MUST follow these rules exactly:

1. Output ONLY these three sections, in this exact order:
   Problem:
   Your Code:
   Feedback:

2. Include NOTHING before, after, or between those sections.

3. Do NOT output the correct solution code.

4. Use the problem description found inside the sample solution.

5. Compare the student's code order to the correct order.

6. If correct:
   - Praise them briefly.
   - Explain why in simple words.

7. If incorrect:
   - Give short, simple hints
   - Explain what is out of order
   - Suggest what to try next
   - Do NOT reveal the correct order

8. Keep everything very short, friendly, and kid-safe.

You must ONLY produce the required three sections and nothing else.
"""

# ---- MAIN ENTRY POINT FOR SERVER ----
def run_parsons_mode(player_input: str, sample_solution: str) -> str:
    """
    Called by FastAPI server. No files. No CLI. Pure function.
    """
    prompt = build_prompt(player_input, sample_solution)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a middle school Python teacher."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"(AI Error: {e})"