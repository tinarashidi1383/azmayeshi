import math
def welcome():
    print('''
    Welcome to Calculator
    ''')
def calculate():
    number1 = int(input("Enter your num1:"))
    number2 = int(input("Enter your num2:"))
    operation = input("Entre_operator:") 
    if operation == '+':
        number = number1 + number2
        print(f"{number1} + {number2} = {number}")
    elif operation == '-':
        number = number1 - number2
        print(f"{number1} - {number2} = {number}")
    elif operation == '*':
        number = number1 * number2
        print(f"{number1} * {number2} = {number}")
    elif operation == '/':
        try:
            number = number1 / number2
            print(f"{number1} / {number2} = {number}")
        except ZeroDivisionError:
            print("Dont enter zero in the denominator")
    elif operation == "jazr":
        number11 = math.sqrt(number1)
        number22 = math.sqrt(number2) 
        print(f" sqrt number {number1}:{number11} va sqrt number {number2}:{number22}")          
    else:
        print("invalid choose...!")   
    again()    
def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper()== "N":
        print('See you later.')
    else:
        again()
welcome()
calculate()           



              