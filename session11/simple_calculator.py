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

while True:
    print('\nSimple Calculator')
    print('1. Start calculator')
    print('2. Exit')
    
    try:
        choice = int(input('\nSelect menu: '))
        
        if choice == 1:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input('Choose the operation (+ - / *): ')
            
            if operation not in opr:
                print('Invalid operation.')
            else:
                result = calc(num1, num2, operation)
                print(f'\n{num1} {operation} {num2} = {result}')
                
        elif choice == 2:
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print('Wrong input. Please select 1 or 2.')
    
    except ValueError:
        print('Wrong input. Please enter a number.')
