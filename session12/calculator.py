#Make a simple calculator application using functions.
opr = ['+', '-', '*', '/']

def calc(num1, num2, opr):
#Perform the calculation based on the given operation
    if opr == '+':
        return num1 + num2
    elif opr == '-':
        return num1 - num2
    elif opr == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    elif opr == '*':
        return num1 * num2
    else:
        return "Invalid operation."
