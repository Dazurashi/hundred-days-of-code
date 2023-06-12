'''
    It's a calculator.
    Woah!!
'''

from art import logo
print(logo)

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

dict = {"+": add, "-" : substract, "*" : multiply, "/" : divide}

def calcultor():
    number1 = float(input("Give me a number: "))
    for operation in dict:
        print(operation)

    while True:
        symbol = input("Pick an operator to manipulate your numbers: ")
        number2 = float(input("Give me another number: "))
        calculation_function = dict[symbol]
        answer = calculation_function(number1, number2)
        print(f"{number1} {symbol} {number2} = {answer}")
        keepGoing = input("Would you like to operate that answer, reset the calculator or quit?\nTo operate type y\nTo reset type r\nTo exit type q : ").lower()

        if keepGoing == "y":
            number1 = answer
        elif keepGoing == "r":
            calcultor()
        else:
            return

calcultor()