#agent.py
import os
import json
from tools.registry import *
from dotenv import load_dotenv
from llm import call_llm


load_dotenv()
model_provider = os.getenv("MODEL_PROVIDER")
max_calls=0


def get_tool_response(resp : any):
    tool_call  = resp.choices[0].message.tool_calls[0]
    tool_name = tool_call.function.name
    tool_args = json.loads(tool_call.function.arguments)

    tool_result = tools_mapping[tool_name](**tool_args)
    return {
        "role" : "tool",
        "tool_call_id" : tool_call.id,
        "content" : json.dumps(tool_result)
    }


messages_input = [
    {"role": "user", "content": "What is the weather like in bangalore?"}
]

tool_schema, tools_mapping = register()



while (max_calls < 10):
    max_calls+=1
    result = call_llm(messages_input, tool_schema, model_provider)
    if (result.choices[0].message.tool_calls):
        messages_input.append(result.choices[0].message)
        messages_input.append(get_tool_response(result))
    else: 
        break
    

print(result.choices[0].message.content)