import os
from groq import Groq

# ---- INITIALIZE GROQ CLIENT ----
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---- PROMPT ----
def build_prompt(player_input, sample_solution):
    return f"""
You are an AI tutor for a young beginner (age 8–12).

The game provides two text sections:

PLAYER INPUT:
(Problem + student's code)
=====================
{player_input}
=====================

SAMPLE SOLUTION:
(Problem + correct code)
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

3. Do not output the sample solution code.

4. Compare the student's code to the problem and the sample solution.

5. Decide if the student solved the problem correctly.

6. If correct:
   - Praise them briefly.
   - Explain why in simple words.

7. If incorrect:
   - Give short, simple hints.
   - Explain every incorrect piece.
   - Suggest what to try next.
   - Do NOT reveal the correct answer.

8. Keep feedback VERY short, friendly, and kid-safe.

9. Do NOT use the sample solution code in your response.

10. With numbers, use approximate terms like "more" or "less".

You must ONLY produce the required three sections and nothing else.
"""

# ---- MAIN ENTRY POINT FOR SERVER ----
def run_inputs_mode(player_input: str, sample_solution: str) -> str:
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