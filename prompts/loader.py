import os
import json
from dotenv import load_dotenv

load_dotenv()

json_filename = os.getenv("PROMPT_VERSION")

def loader():

    prompt_data=None
    try:
        if json_filename:

            file_path = os.path.join("prompts", json_filename)
            
            with open(file_path, "r", encoding="utf-8") as file:
                prompt_data = json.load(file)
            print(f"Successfully loaded: {file_path}")
    except (OSError):
        return {"error_type" : "Error: File not found"}
    return prompt_data
