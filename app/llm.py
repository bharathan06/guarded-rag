#llm.py
import os
from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()


def call_llm(
        message : list, 
        tool_schema : list, 
        model_provider : str
    ) : 
        open_router = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) 
        res = open_router.chat.send(
            messages=message,
            stream = False,
            model= model_provider,
            tools=tool_schema
        )
        return res 