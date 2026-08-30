import os
import json
from dotenv import load_dotenv

load_dotenv()

json_filename = os.getenv("PROMPT_VERSION")

def loader():

    prompt_data = None
    try:
        if json_filename:

            file_path = os.path.join(os.path.dirname(__file__), json_filename)

            with open(file_path, "r", encoding="utf-8") as file:
                prompt_data = json.load(file)
    except (OSError, json.JSONDecodeError):
        return [{"role": "system", "content": "Error: could not load system prompt"}]

    if prompt_data is None:
        return []

    return [{"role": "system", "content": json.dumps(prompt_data)}]
