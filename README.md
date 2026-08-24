frequently used commands : 

1. uv run app/agent.py

-------------------------------------------------
Folder structure : 

app - entry point 
tools - any new tool should be added here 
schema.py - any tools schema msut be mtneioned here. tools format goes here 
tool.py - actual python code which will have the logic that needs to be called my llm 
registry.py - reads both tool.py and schema.py and prepares them for llm usage 
llm.py - takes any message, all tool_schema, calls openrouter with model


-------------------------------------------------
schema for any new tool format : 

SCHEMA = {
    "type": "function",
    "function":{
        "name": "function_name",
        "description": "function desc",
        "parameters":{
            "type": "object",
            "properties":{
                "parameter_name": {
                    "type": "string",
                    "description": "parameter description"
                }
            },
            "required": ["city"]
        }
    }
}


--------------------------------------------------