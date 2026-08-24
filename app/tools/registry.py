#registry.py
import os
import importlib

tools_mapping = {}
tools_schema = []

tools_dir = os.path.dirname(__file__)

#function that calls tools and does the mappings
def register():
    for tools_folder in os.listdir(tools_dir):
        if tools_folder.startswith("_"):
            continue
        if not os.path.isdir(os.path.join(tools_dir, tools_folder)):
            continue

        #tool_module is the tools.py of each tool_folder
        tool_module = importlib.import_module(f"tools.{tools_folder}.tool")

        #func is the execute function of each tools_module
        func = getattr(tool_module, "execute")

        #get the schema from schema module, add to tools_schema
        schema_module = importlib.import_module(f"tools.{tools_folder}.schema")
        schema = getattr(schema_module, "SCHEMA")
        tools_schema.append(schema)

        #map the schema to the respective tool
        tools_mapping[schema["function"]["name"]] = func
        
    return tools_schema, tools_mapping


    