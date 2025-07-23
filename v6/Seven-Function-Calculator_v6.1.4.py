"""
SEVEN-FUNCTION CALCULATOR V6.1.4

A command-line calculator application providing seven core mathematical functions:
addition, subtraction, multiplication, division, exponentiation, trigonometry,
and radical (nth root) calculations.

Features:
- Menu-driven interface for selecting operations.
- Handles basic arithmetic operations (+, -, *, /, ^).
- Supports common trigonometric functions (sine, cosine, tangent) and their
  inverse counterparts (arcsin, arccos, arctan), accepting input in degrees.
- Calculates the nth root of a number.
- Includes basic input validation to prevent common errors like division by zero
  and non-numeric input.
- Provides an option for more precision in radical and trigonometric results.
- Allows the user to perform multiple calculations consecutively.

Usage:
Run the script from your terminal. Follow the on-screen prompts to select an
operation and enter the required values.

Notes: Updated UI with colored and bold text

Author: Aidan McMillan
Date: 7/23/25
"""

import time
import math
GREEN = "\033[92m"
RED = "\033[31m"
BOLD = "\033[1m"
CLEAR = "\033[0m"
first_time = True
operation = None
inputs = [0, 0]

def get_inputs(operation) -> None:
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"{GREEN}{BOLD}____{CLEAR} {operation} ____") # All other computations
    print("ENTER VALUE           ")
    inputs[0] = input("1st Value: ")
    
    print(f"{inputs[0]} {operation} {GREEN}{BOLD}____{CLEAR}")
    print("ENTER VALUE")
    inputs[1] = input("2nd Value: ")
    
    
class Calculate:
    
    def __init__(self):
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    class Arithmetic:
        
        def __init__(self):
            
            pass
        
        def add(self):
            
            try:
                get_inputs('+')
                answer = int(inputs[0]) + int(inputs[1])
                print(f"The sum of {str(inputs[0])} and {str(inputs[1])} is {str(answer)}")
            except ValueError:
                print(f"{RED}ERROR: Invalid inputs!{CLEAR}")
                return 1
        
        def subtract(self):
            
            try:
                get_inputs('-')
                answer = int(inputs[0]) - int(inputs[1])
                print(f"The difference between {str(inputs[0])} and {str(inputs[1])} is {str(answer)}")
            except ValueError:
                print(f"{RED}ERROR: Invalid inputs!{CLEAR}")
                return 1
        
        def multiply(self):
            
            try:
                get_inputs('*')
                answer = int(inputs[0]) * int(inputs[1])
                print(f"The product of {str(inputs[0])} and {str(inputs[1])} is {str(answer)}")
            except ValueError:
                print(f"{RED}ERROR: Invalid inputs!{CLEAR}")
                return 1
        
        def divide(self):
            
            get_inputs('/')
            answer = 0.0
            try:
                answer = int(inputs[0]) / int(inputs[1])
            except ZeroDivisionError:
                print(f"{RED}ERROR: Cannot divide by zero!{CLEAR}")
                return 1
            except ValueError:
                print(f"{RED}ERROR: Invalid inputs!{CLEAR}")
                return 1
            if answer.is_integer():
                ans_int = int(answer)
            print(f"The quotient of {str(inputs[0])} and {str(inputs[1])} is {str(ans_int)}")
        
        def exponent(self):
            
            try:
                get_inputs('^')
                answer = int(inputs[0]) ** int(inputs[1])
                print(f"{str(inputs[0])} to the power of {str(inputs[1])} equals {str(answer)}")
            except ValueError:
                print(f"{RED}ERROR: Invalid inputs!{CLEAR}")
                return 1
    
    class Trig:
        
        def __init__(self):
            
            trigvalue  = None
            
        def arcsin(self):
            
            print("arcsin(___) ")
            print("       ^^^  ")
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.asin(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The arc sine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The arc sine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR} ").strip().lower() == 'y':
                    print(f"The arc sine of {trigvalue} is {answer} degrees.")
            
        def arccos(self):
            
            print("arccos(___) ")
            print("       ^^^  ")
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.acos(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The arc cosine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The arc cosine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR} ").strip().lower() == 'y':
                    print(f"The arc cosine of {trigvalue} is {answer} degrees.")
        
        def arctan(self):
            
            print("arctan(___) ")
            print("       ^^^  ")
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.atan(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The arc tangent of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The arc tangent of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR} ").strip().lower() == 'y':
                    print(f"The arc tangent of {trigvalue} is {answer} degrees.")
                    
        def sin(self):
            
            print("sin(___) ")
            print("    ^^^  ")
            print("ENTER VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.sin(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The sine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The sine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR} ").strip().lower() == 'y':
                    print(f"The sine of {trigvalue} is {answer} degrees.")
            
            
        def cos(self):
            
            print("cos(___) ")
            print("    ^^^  ")
            print("ENTER VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.cos(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The cosine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The cosine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR} ").strip().lower() == 'y':
                    print(f"The cosine of {trigvalue} is {answer} degrees.")
            
        def tan(self):
            
            print("tan(___) ")
            print("    ^^^  ")
            print("SELECT VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.tan(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The tangent of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The tangent of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR} ").strip().lower() == 'y':
                    print(f"The tangent of {trigvalue} is {answer} degrees.")
            
    def radical(self):
        
        print("____th root of ____")
        print("^^^^             ")
        print("ENTER VALUE      ")
        inputs[0] = input()
        
        suffix = "th"
        if int(inputs[0]) % 10 == 1:
            suffix = "st"
        elif int(inputs[0]) % 10 == 2:
            suffix = "nd"
        elif int(inputs[0]) % 10 == 3:
            suffix = "rd"
        
        print(f"{inputs[0].zfill(2)}{suffix} root of ____")
        print("             ^^^^")
        print("ENTER VALUE HERE")
        inputs[1] = input()
        
        answer = float(inputs[1]) ** (1 / float(inputs[0])) # Radical in exponent form
        
        ans_int = 0
        if answer.is_integer():
            
            ans_int = int(answer)
            print(f"The {inputs[0]}{suffix} root of {inputs[1]} is {str(round(ans_int, 3))}")
        
        if ans_int:
            
            return 0
        
        if input(f"Would you like more precision? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR}") == 'y':
            
            print(f"The {inputs[0]}{suffix} root of {inputs[1]} is {str(answer)}")
        
        return 0
    
def prompt_restart(first_time): # Perform another calculation message and surrounding computation.
    
    if first_time == True:
        
        first_time = False
        return 2
    
    else:
        
        prompt_restartStr = input(f"Do you want to perform another calculation? ({GREEN}y{CLEAR}/{RED}n{CLEAR}){CLEAR}")
        
        if prompt_restartStr == 'y':
            
            prompt_restartVar = True
            return 2
        
        elif prompt_restartStr == 'n':
            
            prompt_restartVar = False
            return 0 # Success
        
        else:
            
            print("{RED}ERROR: Invalid input recieved when asking to restart{CLEAR}")
            return 1


def main_menu_prompt(): # Print main menu and recieve operation 
    
    print(f"\n\n\n\n\n\n\n\n\n\n\n")
    print(f"{GREEN}***{BOLD}SELECT OPERATION{CLEAR}{GREEN}***{CLEAR}")
    print(f"{GREEN}*                    *{CLEAR}")
    print(f"{GREEN}*  {BOLD}+ = ADD           {CLEAR}{GREEN}*{CLEAR}")
    print(f"{GREEN}*  {BOLD}- = SUBTRACT      {CLEAR}{GREEN}*{CLEAR}")
    print(f"{GREEN}*  {BOLD}* = MULTIPLY      {CLEAR}{GREEN}*{CLEAR}")
    print(f"{GREEN}*  {BOLD}/ = DIVIDE        {CLEAR}{GREEN}*{CLEAR}")
    print(f"{GREEN}*  {BOLD}^ = EXPONENTIATE  {CLEAR}{GREEN}*{CLEAR}")
    print(f"{GREEN}*  {BOLD}t = TRIGONOMETRY  {CLEAR}{GREEN}*{CLEAR}")
    print(f"{GREEN}*  {BOLD}r = RADICAL       {CLEAR}{GREEN}*{CLEAR}")
    print(f"{GREEN}*                    *{CLEAR}")
    print(f"{GREEN}**********************{CLEAR}")
    
    command = input().strip().lower()
    return command # return the input


def trig_menu(): # Trig menu (also returns input)
    
    print("\n\n\n\n\n\n\n\n\n")
    print(f"{GREEN}***{BOLD}TRIGONOMETRY{CLEAR}{GREEN}***")
    print(f"{GREEN}*                {GREEN}*")
    print(f"{GREEN}* {BOLD}s  = SINE      {CLEAR}{GREEN}*")
    print(f"{GREEN}* {BOLD}c  = COSINE    {CLEAR}{GREEN}*")
    print(f"{GREEN}* {BOLD}t  = TANGENT   {CLEAR}{GREEN}*")
    print(f"{GREEN}* {BOLD}a_ = INVERSE   {CLEAR}{GREEN}*")
    print(f"{GREEN}*                *{CLEAR}")
    print(f"{GREEN}******************{CLEAR}")
    
    command = input().strip().lower()
    return command


def main():

    arithmetic_instance = Calculate.Arithmetic()
    radical_instance = Calculate()
    trig_instance = Calculate.Trig()
    operation = main_menu_prompt()

    match operation:
        
        case '+':
            
            arithmetic_instance.add()
            
        case '-':
            
            arithmetic_instance.subtract()
            
        case '*':
            
            arithmetic_instance.multiply()
            
        case '/':
            
            arithmetic_instance.divide()
            
        case '^':
            
            arithmetic_instance.exponent()
        
        case 'r':
            
            radical_instance.radical()
            
        case 't':
            
            match trig_menu():
                
                case 'as':
                    
                    trig_instance.arcsin()
                    
                case 'ac':
                    
                    trig_instance.arccos()
                    
                case 'at':
                    
                    trig_instance.arctan()
                    
                case 's':
                    
                    trig_instance.sin()
                    
                case 'c':
                    
                    trig_instance.cos()
                    
                case 't':
                    
                    trig_instance.tan()
                
                case _:
                    
                    print(f"{RED}ERROR: Invalid trig operation!{CLEAR}")
        case _:
            
            print(f"{RED}ERROR: Invalid operation!{CLEAR}")

while True: # Loop forever, "Go again?" and sleep logic.
    if prompt_restart(first_time):
        first_time = False
        main()
    else:
        print("Exiting calculation", end = "")
        time.sleep(0.5)
        print(".", end = "")
        time.sleep(0.5)
        print(".", end = "")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("Calculation Exited")
        time.sleep(1)
        print("Press ENTER to restart, Press q to quit")
        if input() != 'q':
            print("Restarting", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            first_time = True
        else:
            exit()
            