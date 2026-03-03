import os
from getpass import getpass

KEY_NAME = "GROQ_API_KEY"
KEY_FILE = ".api_key"

def get_api_key():
    # 1.Environment variable
    key = os.getenv(KEY_NAME)
    if key:
        return key.strip()

    # 2.Local key file
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()

    # 3.Prompt user
    print("Groq API key not found.")
    key = getpass("Enter your Groq API key (input hidden): ").strip()

    if not key:
        raise RuntimeError("API key is required.")

    # 4.Save for next time
    with open(KEY_FILE, "w", encoding="utf-8") as f:
        f.write(key)

    print("API key saved locally.")
    return key