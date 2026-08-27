import operator

SUPPORTED_OPERATORS = {
    "+" : operator.add,
    "-" : operator.sub,
    "/" : operator.truediv,
    "*" : operator.mul
}

def execute(number1, number2, operator_in):
    error_message = {}

    if operator_in not in SUPPORTED_OPERATORS:
        error_message.update({"error_type" : "Invalid Operator" })
        return error_message

    try:
        num1 = float(number1)
        num2 = float(number2)
    except (ValueError, TypeError):
        error_message.update({"error_type" : "Error : Invalid Operands" })
        return error_message

    if operator_in == '/' and num2==0.0 : 
        error_message.update({"error_type" : "Error : Division By Zero"})
        return error_message

    



    