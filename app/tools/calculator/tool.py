import operator

SUPPORTED_OPERATORS = {
    "+" : operator.add,
    "-" : operator.sub,
    "/" : operator.truediv,
    "*" : operator.mul
}

def execute(number1, number2, operator_in):
    error_message = {}

    #Operator checks 
    if operator_in not in SUPPORTED_OPERATORS:
        error_message.update({"error_type" : "Invalid Operator" })
        return error_message

    #Calculation block
    try:
        num1 = float(number1)
        num2 = float(number2)
        #Div by zero checks 
        if operator_in == '/' and abs(num2) < 1e-9: 
            error_message.update({"error_type" : "Error: Division By Zero"})
            return error_message
        ans = SUPPORTED_OPERATORS[operator_in](num1, num2)

    except (ValueError, TypeError):
        error_message.update({"error_type" : "Error: Invalid Operands"})
        return error_message
    except (OverflowError):
        error_message.update({"error_type" : "Error: Integer Overflow"})
        return  error_message

    #Happy path
    return {
        "result" : ans
    }

    



    