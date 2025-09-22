"""
SEVEN-FUNCTION CALCULATOR V9.8

Features:
- Menu-driven interface for selecting operations.
- Handles basic arithmetic operations (+, -, *, /, ^).
- Supports common trigonometric functions (sine, cosine, tangent) and their
  inverse counterparts (arcsin, arccos, arctan), accepting input in degrees.
- Calculates the nth root of a number.
- Simplifies algebraic expressions
- Includes basic input validation to prevent common errors like division by zero
  and non-numeric input.
- Provides an option for more precision in radical and trigonometric results.
- Allows the user to perform multiple calculations consecutively.

Usage:
Run the script from your terminal. Follow the on-screen prompts to select an
operation and enter the required values.

Notes: Refactored and added helper functions print_args() and get_argument()

Author: Aidan McMillan
Date: 9/18/25
"""

import time
import math
import os
from sympy.solvers import solve
from sympy import Symbol
import sympy
from awmfrmt import Color, Markings

left_arguments = {}
right_arguments = {}
inputs = [None, None]

def clear_terminal():
    """
    ### Clear Terminal
    Clears user command prompt

    * **Args:**
        * None
    * **Returns:**
        * None
    """
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Unix
    elif os.name == 'posix':
        _ = os.system('clear')
      
def main_menu_prompt():
    """
    ### Main Menu Prompt
    Prints main menu and gets operation to perform

    * **Args:**
        * None
    * **Returns:**
        * Operation to perform
    """
    clear_terminal()
    print(f"{Color.green}***{Markings.bold}SELECT OPERATION{Markings.clear}{Color.green}***{Markings.clear}")
    print(f"{Color.green}*                    *{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}+ = ADD            {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}- = SUBTRACT       {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}* = MULTIPLY       {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}/ = DIVIDE         {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}^ = EXPONENTIATE   {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}t = TRIGONOMETRY   {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}r = RADICAL        {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}p = POLYNOMIAL     {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}q = QUIT           {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*                    *{Markings.clear}")
    print(f"{Color.green}**********************{Markings.clear}")
    
    command = input().strip().lower()
    clear_terminal()
    return command # return the input


def trig_menu():
    """
    ### Trig menu
    Prints menu and gets input for trig expression

    * **Args:**
        * None
    * **Returns:**
        * Trig command (command)
    """
    clear_terminal()
    print(f"{Color.green}***{Markings.bold}TRIGONOMETRY{Markings.clear}{Color.green}***{Markings.clear}")
    print(f"{Color.green}*                *{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}s  = SINE      {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}c  = COSINE    {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}t  = TANGENT   {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}a_ = INVERSE   {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}*                *{Markings.clear}")
    print(f"{Color.green}******************{Markings.clear}")
    
    command = input().strip().lower()
    clear_terminal()
    return command

def old_poly():
    """
    ### Polynomial
    Gets input, simplifies and solves algebraic expression

    * **Args:**
        * None
    * **Returns:**
        * None
    """
    alg_restart = None
    left_arguments = {}
    right_arguments = {}
    
    while alg_restart != 'e':
        alg_restart = 'z'
        
        arg = get_argument()

        try:
            left_arguments[arg[0]] = left_arguments.get(arg[0], 0) + arg[1]
        except Exception as e:
            print(f"{Color.red}ERROR: {e}{Markings.clear}")
        
        clear_terminal()
        print("Current arguments: ", end='')
        first_term = True
        print_base = ''
        left_arguments = dict(sorted(left_arguments.items(), reverse=True))
        print_args(left_arguments)
        
        print("\nEnter 'e' to enter an equals sign and 'a' to add another argument.")   
        while alg_restart != 'e' and alg_restart != 'a':   
            alg_restart = input().strip().lower()
            if alg_restart != 'e' and alg_restart != 'a':
                print(f"{Color.red}ERROR: Invalid input! Please enter 'e' or 'a'.{Markings.clear}")
                
    
    while alg_restart != 'f':
        alg_restart = 'z'
        
        arg = get_argument()
      
        try:
            right_arguments[arg_power] = right_arguments.get(arg_power, 0) + arg_base
        except Exception as e:
            print(f"{Color.red}ERROR: {e}{Markings.clear}")
        
        clear_terminal()
        
        print("Current arguments: ", end='')
        first_term = True
        print_base = ''
        left_arguments = dict(sorted(left_arguments.items(), reverse=True))
        print_args(left_arguments)
        
        print(" = ", end = '')
        
        first_term = True
        print_base = ''
        right_arguments = dict(sorted(right_arguments.items(), reverse=True))
        print_args(right_arguments)
        
        if first_term:
            print("0", end = '')
        
        print("\nEnter 'f' to finish and simplify and 'a' to add another argument.")   
        while alg_restart != 'f' and alg_restart != 'a':   
            alg_restart = input().strip().lower()
            if alg_restart != 'f' and alg_restart != 'a':
                print(f"{Color.red}ERROR: Invalid input! Please enter 'f' or 'a'.{Markings.clear}")
                
    for power, base in right_arguments.items():
        if left_arguments.get(power):
            left_arguments[power] -= right_arguments[power]
        else:
            left_arguments[power] = 0 - right_arguments[power]
        if left_arguments.get(power) == 0:
            del(left_arguments[power])
    
    print("The simplified expression is:")
    first_term = True
    left_arguments = dict(sorted(left_arguments.items(), reverse=True))
    print_args(left_arguments)
    
    if not left_arguments:
        print("0", end = '')
        
    print(" = 0")
    
    solve_poly(left_arguments)
    
    input("\nPress ENTER to continue.")

def print_args(arguments):
    """
    ### Print Arguments
    Prints arguments from a dict

    * **Args:**
        * Arguments: A dict formatted {power : base}
    * **Returns:**
        * None
    """
    first_term = True
    for power, base in arguments.items():
        if not float(base) == 0:
            print(format_arg(base, power, first_term), end = '')
            first_term = False

def polynomial():
    """
    ### Poly
    """
    print(f"Enter equation (Use ^ for exponents and parentheses for multiplication. Use x for a variable. The equation will be set equal to 0, so do not include equal signs.")
    equation = input()
    equation = equation.replace(" ", "").replace("^", "**")
    sympy_eq = sympy.simplify(sympy.parsing.sympy_parser.parse_expr(equation), Symbol('x'))
    print("The simplified equation is:")

    print(sympy_eq)
    
    if solve(sympy_eq) == "0":
        print("0", end = '')
        
    print(" = 0")
    
    solve_poly(arguments)
    
    input("\nPress ENTER to continue.")

def get_argument():
    """
    ### Get Argument
    Gets an argument for polynomial

    * **Args:**
        * None
    * **Returns:**
        * Power
        * Base
    """
    
    print(f"Enter argument base: {Color.green}_{Markings.clear}x^_{Markings.clear}")
    
    try:
        arg_base = float(input())
    except ValueError:
        print(f"{Color.red}ERROR: Invalid argument! Please enter a number.{Markings.clear}")
    except Exception as e:
        print(f"{Color.red}ERROR: {e}")
    print(f"Enter argument exponent: {arg_base}x^{Color.green}_{Markings.clear}")
    
    try:
        arg_power = float(input())
    except ValueError:
        print(f"{Color.red}ERROR: Invalid argument! Please enter a number.{Markings.clear}")
    except Exception as e:
        print(f"{Color.red}ERROR: {e}{Markings.clear}")
    return arg_power, arg_base

def format_arg(base, power, first_arg):
    """
    ### Print Arguments
    * **Args:**
        * Base: The base of the argument to be printed
        * Power: The exponent of the argument to be printed
        * First Argument: Whether or not the argument is the first
    * **Returns:*
        * Print Argument: The printable, formatted argument with the leading sign
    """
    
    print_arg = ''
    sign = ' + '
    base = float(base)
    power = float(power)
    
    if base == int(base):
        base = int(base)
        
    if power == int(power):
        power = int(power)
    
    if str(power) == '0':
        print_arg = str(abs(base))
        
    elif str(power) == '1' and str(abs(base)) == '1':
        print_arg = "x"
    
    elif str(base) == '1':
        print_arg = "x^" + str(power)
    
    elif str(power) == '1':
        print_arg = str(abs(base)) + "x"
        
    else:
        print_arg = str(abs(base)) + "x^" + str(power)
    
    if not base == abs(base):
        if first_arg == True:
            sign = '-'
            
        else:
            sign = ' - '
            
    else:
        if first_arg == True:
            sign = ''
    
    return sign + print_arg
    

def solve_poly(expression):
    """
    ### Solve Polynomial
    
    * **Args:**
        * Expression: An expression to solve, set equal to 0.
    * **Returns:**
        * None
    """
    
    solutions_ary = solve(sympy.sympify(expression), x)
    for value in solutions_ary:
        if value == value.replace(" ", ""):
            solutions[value] = 0
        else:
            solutions[value] = value.split()[2].rstrip("i")
    
    if first_term:
        print("The equation has infinite solutions.")
    
    elif str(solutions) == "[]":
        print("The equation has no solutions.")
    
    else:
        print(f"The solutions to the expression are {solutions}.")

def arithmetic(operation) -> None:
    """
    ### Arithmetic
    Gets input and performs an arithmetic operation (+, -, /, *, ^)

    * **Args:**
        * Operation to perform
    * **Returns:**
        * None
    """
    clear_terminal()
    print(f"{Color.green}{Markings.bold}_____{Markings.clear} {operation} ____")
    print("ENTER VALUE")
    inputs[0] = float(input("1st Value: "))
    
    if inputs[0] == int(inputs[0]):
        inputs[0] = int(inputs[0])
    
    print(f"{inputs[0]} {operation} {Color.green}{Markings.bold}_____{Markings.clear}")
    print("ENTER VALUE")
    inputs[1] = float(input("2nd Value: "))
    clear_terminal()
    
    if inputs[1] == int(inputs[1]):
        inputs[1] = int(inputs[1])
    
    operation_str = {
        '+' : "sum of",
        '-' : "difference between",
        '*' : "product of",
        '/' : "quotient of"
        }
    
    try:
        if operation == '+':
            answer = inputs[0] + inputs[1]
        
        elif operation == '-':
            answer = inputs[0] - inputs[1]
            
        elif operation == '*':
            answer = inputs[0] * inputs[1]
        
        elif operation == '/':
            answer = float(inputs[0]) / float(inputs[1])
        elif operation == '^':
            answer = inputs[0] ** inputs[1]
            print(f"{inputs[0]} to the power of {inputs[1]} equals {answer}")
            
        if answer == int(answer):
            answer = int(answer)     
            
        if operation_str:
            print(f"The {operation_str[operation]} {str(inputs[0])} and {str(inputs[1])} is {str(round(answer, 3))}")
        
        if answer != round(answer, 3):    
            if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
                print(f"The {operation_str[operation]} {str(inputs[0])} and {str(inputs[1])} is {answer}")
        
        input("Press ENTER to return to the main menu.")
    except ValueError:
        print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
        input("Press ENTER to return to the main menu.")
    except Exception as e:
        print(f"{Color.red}ERROR: {e}{Markings.clear}")
        input("Press ENTER to return to the main menu.")

def trig(operation):
    """
    ### Trigonometry
    Gets inputs for and calculates a trigonometric expression

    * **Args:**
        * None
    * **Returns:**
        * None
    """
    operation_str = {
      'as' : "arc sine",
      'ac' : "arc cosine",
      'at' : "arc tangent",
      's'  : "sine",
      'c'  : "cosine",
      't'  : "tangent"
    }
    
    function = {
      'as' : "arcsin",
      'ac' : "arccos",
      'at' : "arctan",
      's'  : "sin",
      'c'  : "cos",
      't'  : "tan"
    }
    
    print(f"{function[operation]}({Color.green}{Markings.bold}____{Markings.clear}) ")
    
    if operation == 's' or operation == 'c' or operation == 't':
        trigvalue = input("ENTER VALUE (IN DEGREES)\n").strip().lower()
    else:
        trigvalue = input("ENTER VALUE (-1 to 1)\n").strip().lower()
    
    if operation == 'as':
        answer = math.degrees(math.asin(float(trigvalue)))
        
    elif operation == 'ac':
        answer = math.degrees(math.acos(float(trigvalue)))
        
    elif operation == 'at':
        answer = math.degrees(math.atan(float(trigvalue)))
        
    elif operation == 's':
        answer = math.sin(math.radians(float(trigvalue)))
        
    elif operation == 'c':
        answer = math.cos(math.radians(float(trigvalue)))
        
    elif operation == 't':
        answer = math.tan(math.radians(float(trigvalue)))
    
    if answer == int(answer):
        answer = int(answer)
    print(f"The {operation_str[operation]} of {trigvalue} degrees is {round(answer, 3)}", end = '')
    if operation in ('as', 'ac', 'at'):
        print("degrees.")
    elif operation in ('s', 'c', 't'):
        print(".")

    if not float(answer).is_integer():
        if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear} ").strip().lower() == 'y':
            print(f"The {operation_str[operation]} of {trigvalue} degrees is {answer}", end = '')
            if operation in ('as', 'ac', 'at'):
                print("degrees.")
            elif operation in ('s', 'c', 't'):
                print(".")
    
    input("Press ENTER to return to the main menu.")

def radical():
    """
    ### Radical
    Gets input and calculates nth root of a number

    * **Args:**
        * None
    * **Returns:**
        * None
    """
    print(f"{Color.green}{Markings.bold}_____{Markings.clear}th root of ____")
    print("ENTER VALUE     ")
    inputs[0] = input()
    
    suffix = "th"
    if int(inputs[0]) % 10 == 1:
        suffix = "st"
    elif int(inputs[0]) % 10 == 2:
        suffix = "nd"
    elif int(inputs[0]) % 10 == 3:
        suffix = "rd"
    
    print(f"{inputs[0]}{suffix} root of {Color.green}{Markings.bold}_____{Markings.clear}")
    print("ENTER VALUE")
    inputs[1] = input()
    
    answer = float(inputs[1]) ** (1 / float(inputs[0])) # Radical in exponent form
    
    display_answer = 0
    if answer == int(answer):                
        display_answer = int(answer)
    else:
        display_answer = round(answer, 3)
        
    print(f"The {inputs[0]}{suffix} root of {inputs[1]} is {str(display_answer)}")

    if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}){Markings.clear}") == 'y':                
        print(f"The {inputs[0]}{suffix} root of {inputs[1]} is {str(answer)}")

def main():
    """
    ### Main function
    Main body of code

    * **Args:**
        * None
    * **Returns:**
        * None
    """
    operation = main_menu_prompt()

    if operation in ('+', '-', '*', '/', '^'):
        arithmetic(operation)
  
    elif operation == 'r':
        radical()
            
    elif operation == 'p':
        polynomial()

    elif operation == 'q':
        quit_input = input(f"{Color.red}{Markings.bold}ARE YOU SURE YOU WANT TO QUIT? {Markings.clear}({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear})")
        if quit_input == 'y':
            quit()
        elif quit_input == 'n':
            main_menu_prompt()
        else:
            time_left = 3
            while time_left >= 0:
                print(f"{Color.red}ERROR: Invalid input. Reverting to main menu in {str(round(time_left, 3)).zfill(3)} seconds.{Markings.clear}", end = '\r')
                time.sleep(0.01)
                time_left -= 0.01
            clear_terminal()
          
    elif operation == 't':
            trig_operation = trig_menu()

            if operation in ('as', 'ac', 'at', 's', 'c', 't'):
                trig(trig_operation)
            
            else:
                print(f"{Color.red}ERROR: Invalid trig operation!{Markings.clear}")
    else:
        print(f"{Color.red}ERROR: Invalid operation!{Markings.clear}")
while True: # Main loops forever
    try:
        main()
    except Exception as e:
        print(f"{Color.red}ERROR: {e}{Markings.clear}")
        input("Press ENTER to return to the main menu.")
