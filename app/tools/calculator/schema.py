SCHEMA = {
    "type": "function",
    "function":{
        "name": "calculate",
        "description": "A tool that can be used to do arithematic calculations",
        "parameters":{
            "type": "object",
            "properties":{
                "number1": {
                    "type": "number",
                    "description": "First number"
                },
                "number2" : {
                    "type" : "number",
                    "description" : "Second number"
                },
                "operator_in" : {
                    "type" : "string",
                    "description" : "The operator used to evaluate the expressions",
                    "enum" : ["+","-","/","*"]
                }
            },
            "required": ["number1", "number2", "operator"]
        }
    }
}