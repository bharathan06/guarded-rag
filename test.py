import os
from openrouter import OpenRouter
from dotenv import load_dotenv

load_dotenv()


with OpenRouter(
    os.getenv("OPENROUTER_API_KEY")
) as open_router: 
    messages=[
        {"content" : "What is the weather in bangalore today?", "role" : "user"}
    ]
    res = open_router.chat.send(
        messages=messages,
        stream = False,
        model="liquid/lfm-2.5-2.6b:free"
    )
    print(res) 