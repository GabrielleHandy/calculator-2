"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
while True:
    answer = input("Enter your equation >>> ")

    tokens = answer.split(" ")

    if tokens[0] == "q":
        print("You ended the game")
        quit() 
    
# Replace this with your code
