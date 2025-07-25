"""
SEVEN-FUNCTION CALCULATOR V7.2

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

Notes: Streamlined quitting process for easier use.

Author: Aidan McMillan
Date: 7/25/25
"""

import os
import time
import math
from awmformat import Color, Markings
first_time = True
operation = None
inputs = [0, 0]


def clear_terminal():
    # Clears Terminal
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-like systems (Linux, macOS)
    else:
        _ = os.system('clear')

def get_inputs(operation) -> None:
    
    clear_terminal()
    print(f"{Color.green}{Markings.bold}____{Markings.clear} {operation} ____") # All other computations
    print("ENTER VALUE           ")
    inputs[0] = input("1st Value: ")
    
    print(f"{inputs[0]} {operation} {Color.green}{Markings.bold}____{Markings.clear}")
    print("ENTER VALUE")
    inputs[1] = input("2nd Value: ")
    clear_terminal()
    
    
class Calculate:
    
    def __init__(self):
        
        clear_terminal()
    
    class Arithmetic:
        
        def __init__(self):
            
            pass
        
        def add(self):
            
            try:
                get_inputs('+')
                answer = int(inputs[0]) + int(inputs[1])
                print(f"The sum of {str(inputs[0])} and {str(inputs[1])} is {str(answer)}")
            except ValueError:
                print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
                return 1
        
        def subtract(self):
            
            try:
                get_inputs('-')
                answer = int(inputs[0]) - int(inputs[1])
                print(f"The difference between {str(inputs[0])} and {str(inputs[1])} is {str(answer)}")
            except ValueError:
                print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
                return 1
        
        def multiply(self):
            
            try:
                get_inputs('*')
                answer = int(inputs[0]) * int(inputs[1])
                print(f"The product of {str(inputs[0])} and {str(inputs[1])} is {str(answer)}")
            except ValueError:
                print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
                return 1
        
        def divide(self):
            
            get_inputs('/')
            answer = 0.0
            try:
                answer = int(inputs[0]) / int(inputs[1])
            except ZeroDivisionError:
                print(f"{Color.red}ERROR: Cannot divide by zero!{Markings.clear}")
                return 1
            except ValueError:
                print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
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
                print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
                return 1
    
    class Trig:
        
        def __init__(self):
            
            trigvalue  = None
            
        def arcsin(self):
            
            print(f"arcsin({Color.green}{Markings.bold}___{Markings.clear}) ")
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.asin(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The arc sine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The arc sine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
                    print(f"The arc sine of {trigvalue} is {answer} degrees.")
            
        def arccos(self):
            
            print(f"arccos({Color.green}{Markings.bold}___{Markings.clear}) ")
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.acos(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The arc cosine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The arc cosine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
                    print(f"The arc cosine of {trigvalue} is {answer} degrees.")
        
        def arctan(self):
            
            print(f"arctan({Color.green}{Markings.bold}___{Markings.clear}) ")
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.atan(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The arc tangent of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The arc tangent of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
                    print(f"The arc tangent of {trigvalue} is {answer} degrees.")
                    
        def sin(self):
            
            print(f"sin({Color.green}{Markings.bold}___{Markings.clear}) ")
            print("ENTER VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.sin(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The sine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The sine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
                    print(f"The sine of {trigvalue} is {answer} degrees.")
            
            
        def cos(self):
            
            print(f"cos({Color.green}{Markings.bold}___{Markings.clear}) ")
            print("ENTER VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.cos(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The cosine of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The cosine of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
                    print(f"The cosine of {trigvalue} is {answer} degrees.")
            
        def tan(self):
            
            print(f"tan({Color.green}{Markings.bold}___{Markings.clear}) ")
            print("SELECT VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.tan(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print(f"The tangent of {trigvalue} is {ans_int} degrees.")
                return None
                
            print(f"The tangent of {trigvalue} is {round(answer, 3)} degrees.")
            if not answer.is_integer():
                if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
                    print(f"The tangent of {trigvalue} is {answer} degrees.")
            
    def radical(self):
        
        print(f"{Color.green}{Markings.bold}____{Markings.clear}th root of ____")
        print("ENTER VALUE      ")
        inputs[0] = input()
        
        suffix = "th"
        if int(inputs[0]) % 10 == 1:
            suffix = "st"
        elif int(inputs[0]) % 10 == 2:
            suffix = "nd"
        elif int(inputs[0]) % 10 == 3:
            suffix = "rd"
        
        print(f"{inputs[0]}{suffix} root of {Color.green}{Markings.bold}____{Markings.clear}")
        print("ENTER VALUE")
        inputs[1] = input()
        
        answer = float(inputs[1]) ** (1 / float(inputs[0])) # Radical in exponent form
        
        display_answer = 0
        if answer.is_integer():            
            display_answer = int(answer)
        else:
            display_answer = round(answer, 3)
            
        print(f"The {inputs[0]}{suffix} root of {inputs[1]} is {str(display_answer)}")

        if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear}") == 'y':            
            print(f"The {inputs[0]}{suffix} root of {inputs[1]} is {str(answer)}")
        
        return 0

def main_menu_prompt(): # Print main menu and recieve operation 
    
    clear_terminal()
    print(f"{Color.green}***{Markings.bold}SELECT OPERATION{Markings.clear}{Color.green}***{Markings.clear}")
    print(f"{Color.green}*                    *{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}+ = ADD           {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}- = SUBTRACT      {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}* = MULTIPLY      {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}/ = DIVIDE        {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}^ = EXPONENTIATE  {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}t = TRIGONOMETRY  {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}r = RADICAL       {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*  {Markings.bold}q = QUIT          {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*                    *{Markings.clear}")
    print(f"{Color.green}**********************{Markings.clear}")
    
    command = input().strip().lower()
    clear_terminal()
    return command # return the input


def trig_menu(): # Trig menu (also returns input)
    
    clear_terminal()
    print(f"{Color.green}***{Markings.bold}TRIGONOMETRY{Markings.clear}{Color.green}***")
    print(f"{Color.green}*                {Color.green}*")
    print(f"{Color.green}* {Markings.bold}s  = SINE      {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}c  = COSINE    {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}t  = TANGENT   {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}a_ = INVERSE   {Markings.clear}{Color.green}*")
    print(f"{Color.green}*                *{Markings.clear}")
    print(f"{Color.green}******************{Markings.clear}")
    
    command = input().strip().lower()
    clear_terminal()
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

        case 'q':
            quit_in = input(f"{Color.red}{Markings.bold}ARE YOU SURE YOU WANT TO QUIT? {Markings.clear}({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear})")
            if quit_in == 'y':
                quit()
            elif quit_in == 'n':
                main_menu_prompt()
            else:
                time_left = 3
                while time_left >= 0:
                    print(f"ERROR: Invalid input. Reverting to main menu in {str(round(time_left, 3)).zfill(3)} seconds.", end = '\r')
                    time.sleep(0.01)
                    time_left -= 0.01
                clear_terminal()    
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
                    print(f"{Color.red}ERROR: Invalid trig operation!{Markings.clear}")
        case _:
            print(f"{Color.red}ERROR: Invalid operation!{Markings.clear}")

while True: # Loop forever, "Go again?" and sleep logic.
        main()
            