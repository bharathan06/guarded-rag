SCHEMA = {
    "type": "function",
    "function":{
        "name": "get_weather",
        "description": "A tool that can be used to check the weather of any given city",
        "parameters":{
            "type": "object",
            "properties":{
                "city": {
                    "type": "string",
                    "description": "Name of the city for which the weather needs to be checked for."
                }
            },
            "required": ["city"]
        }
    }
}