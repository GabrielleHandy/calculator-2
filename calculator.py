"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    answer = input("Enter your equation >>> ")

    tokens = answer.split(" ")
    
    if len(tokens) <= 3:
        num1 = tokens[1]
        num2 = tokens[2]
        if num1.isdigit() is False or num2.isdigit() is False:
            print("Please enter numbers")
    else:
        print("Only accepts up to 2 numbers")

    if tokens[0] == "q":
        print("You ended the game")
        quit() 
    else:
        if tokens[0] == 'add':
            print(add(float(num1), float(num2)))
        elif tokens[0] == 'subtract':
            print(subtract(float(num1), float(num2)))
        elif tokens[0] == 'multiply':
            print(multiply(float(num1), float(num2)))
        elif tokens[0] == 'divide':
            print(divide(float(num1), float(num2)))
        elif tokens[0] == 'square':
            print(square(float(num1)))
        elif tokens[0] == 'cube':
            print(cube(float(num1)))        
        elif tokens[0] == 'power':
            print(power(float(num1), float(num2)))
        elif tokens[0] == 'mod':
            print(mod(float(num1), float(num2)))
        else:
            print("""Please enter: add, subtract, multiply, 
            divide, square, cube, power, mod followed by two numbers""" )
# Replace this with your code
 