import logging
import azure.functions as func

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    operation = req.params.get('operation')
    num1 = float(req.params.get('num1'))
    num2 = float(req.params.get('num2'))

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        return func.HttpResponse(
             "Invalid operation. Please provide a valid operation (add, subtract, multiply, divide).",
             status_code=400
        )

    return func.HttpResponse(str(result))
