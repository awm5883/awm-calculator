"""
SEVEN-FUNCTION CALCULATOR V7.3

A command-line calculator application providing seven core mathematical functions:
addition, subtraction, multiplication, division, exponentiation, trigonometry,
and radical (nth root) calculations.

This version is intended to be used with the custom 'awmfrmt' module for text
formatting in the terminal.

Features:
- Menu-driven interface for selecting operations.
- Handles basic arithmetic operations (+, -, *, /, ^) with floating-point numbers.
- Supports common trigonometric functions (sine, cosine, tangent) and their
  inverse counterparts (arcsin, arccos, arctan), correctly handling degrees.
- Calculates the nth root of a number.
- Includes robust input validation to prevent common errors like division by zero
  and non-numeric input.
- Provides an option for more precision in results.
- Allows the user to perform multiple calculations consecutively in a stable loop.

Usage:
Run the script from your terminal. Ensure the 'awmfrmt.py' module is in the
same directory. Follow the on-screen prompts to select an
operation and enter the required values.

Notes: Stopped early reverts to main menu.

Author: Aidan McMillan
Date: 8/8/25
"""

import os
import math
import time
from awmfrmt import Color, Markings

def clear_terminal():
<<<<<<< HEAD
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
=======
    # Clears Terminal
    # For Windows
    if os.name == 'nt':
        import os  
        _ = os.system('cls')
    # For Unix-like systems (Linux, macOS)
    elif os.name == 'posix':
        import os  
        _ = os.system('clear')
    # For TI (because calculator^2)
    else:
        import ti_system
        ti_system.clear_history()
<<<<<<< HEAD
>>>>>>> parent of 0c4645a (Update awm-calculator-final.py)
=======
>>>>>>> parent of 0c4645a (Update awm-calculator-final.py)

def prompt_main_menu_return():
    """Waits for the user to press 'y' to return to the menu."""
    response = input(f"Press {Color.green}y{Markings.clear} to return to the main menu.")
    while response.lower() != 'y':
        response = input("ERROR: Invalid input. Please press 'y' to return to the main menu.")
    return

def get_numeric_input(prompt: str) -> str:
    """Continuously prompts for a valid numeric input and returns it as a string."""
    while True:
        value = input(prompt)
        try:
            # Check if it can be converted to a float, but return the original string
            float(value)
            return value
        except ValueError:
            print(f"{Color.red}ERROR: Invalid input. Please enter a number.{Markings.clear}")

def get_inputs(operation: str) -> tuple[str, str]:
    """Gets two numeric inputs from the user, following the original UI flow."""
    clear_terminal()
    print(f"{Color.green}{Markings.bold}____{Markings.clear} {operation} ____")
    print("ENTER VALUE             ")
    num1 = get_numeric_input("1st Value: ")

    clear_terminal()
    print(f"{num1} {operation} {Color.green}{Markings.bold}____{Markings.clear}")
    print("ENTER VALUE")
    num2 = get_numeric_input("2nd Value: ")
    
    clear_terminal()
    return num1, num2

def calculate_add():
    try:
        inputs = get_inputs('+')
        answer = float(inputs[0]) + float(inputs[1])
        print(f"The sum of {inputs[0]} and {inputs[1]} is {answer}")
        prompt_main_menu_return()
    except ValueError:
        print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
        time.sleep(2)

def calculate_subtract():
    try:
        inputs = get_inputs('-')
        answer = float(inputs[0]) - float(inputs[1])
        print(f"The difference between {inputs[0]} and {inputs[1]} is {answer}")
        prompt_main_menu_return()
    except ValueError:
        print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
        time.sleep(2)

def calculate_multiply():
    try:
        inputs = get_inputs('*')
        answer = float(inputs[0]) * float(inputs[1])
        print(f"The product of {inputs[0]} and {inputs[1]} is {answer}")
        prompt_main_menu_return()
    except ValueError:
        print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
        time.sleep(2)

def calculate_divide():
    try:
        inputs = get_inputs('/')
        if float(inputs[1]) == 0:
            print(f"{Color.red}ERROR: Cannot divide by zero!{Markings.clear}")
            time.sleep(2)
            return
        answer = float(inputs[0]) / float(inputs[1])
        ans_to_print = answer
        if answer.is_integer():
            ans_to_print = int(answer)
        print(f"The quotient of {inputs[0]} and {inputs[1]} is {ans_to_print}")
        prompt_main_menu_return()
    except ValueError:
        print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
        time.sleep(2)

def calculate_exponent():
    try:
        inputs = get_inputs('^')
        answer = float(inputs[0]) ** float(inputs[1])
        print(f"{inputs[0]} to the power of {inputs[1]} equals {answer}")
        prompt_main_menu_return()
    except ValueError:
        print(f"{Color.red}ERROR: Invalid inputs!{Markings.clear}")
        time.sleep(2)

def calculate_radical():
    """Calculates the nth root using the original UI."""
    clear_terminal()
    print(f"{Color.green}{Markings.bold}____{Markings.clear}th root of ____")
    print("ENTER VALUE      ")
    val1 = get_numeric_input("")
    
    n = int(float(val1))
    suffix = "th"
    if n % 10 == 1 and n % 100 != 11:
        suffix = "st"
    elif n % 10 == 2 and n % 100 != 12:
        suffix = "nd"
    elif n % 10 == 3 and n % 100 != 13:
        suffix = "rd"
    
    clear_terminal()
    print(f"{n}{suffix} root of {Color.green}{Markings.bold}____{Markings.clear}")
    print("ENTER VALUE")
    val2 = get_numeric_input("")

    if float(val2) < 0 and n % 2 == 0:
        print(f"{Color.red}ERROR: Cannot calculate an even root of a negative number.{Markings.clear}")
        time.sleep(2)
        return

    answer = float(val2) ** (1/n)
    display_answer = answer
    if answer.is_integer():
        display_answer = int(answer)
    else:
        display_answer = round(answer, 3)

    print(f"The {n}{suffix} root of {val2} is {display_answer}")
    
    if not answer.is_integer():
        if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear})").strip().lower() == 'y':
            print(f"The {n}{suffix} root of {val2} is {answer}")
    
    prompt_main_menu_return()


def run_trig_menu():
    """Handles the trigonometry sub-menu logic with original UI."""
    command = trig_menu_prompt()
    clear_terminal()
    
    trig_actions = {
        's': handle_trig_calc, 'c': handle_trig_calc, 't': handle_trig_calc,
        'as': handle_trig_calc, 'ac': handle_trig_calc, 'at': handle_trig_calc
    }

    if command in trig_actions:
        trig_actions[command](command)
    else:
        print(f"{Color.red}ERROR: Invalid trig operation!{Markings.clear}")
        time.sleep(2)

def handle_trig_calc(op):
    """Generic handler for all trig functions to restore original print logic."""
    func_map = {
        's': ('sin', 'sine', math.sin, False), 'c': ('cos', 'cosine', math.cos, False), 't': ('tan', 'tangent', math.tan, False),
        'as': ('arcsin', 'arc sine', math.asin, True), 'ac': ('arccos', 'arc cosine', math.acos, True), 'at': ('arctan', 'arc tangent', math.atan, True)
    }
    
    func_name, long_name, math_func, is_inverse = func_map[op]
    
    print(f"{func_name}({Color.green}{Markings.bold}___{Markings.clear}) ")
    if is_inverse:
        print("ENTER VALUE (-1 to 1)\n")
    else:
        print("ENTER VALUE (IN DEGREES)\n")
    
    trigvalue_str = get_numeric_input("")
    trigvalue = float(trigvalue_str)

    if is_inverse and (trigvalue < -1 or trigvalue > 1):
        print(f"{Color.red}ERROR: Input must be between -1 and 1.{Markings.clear}")
        time.sleep(2)
        return
        
    if is_inverse:
        answer_rad = math_func(trigvalue)
        answer = math.degrees(answer_rad)
    else:
        answer = math_func(math.radians(trigvalue))

    if answer.is_integer():
        ans_int = int(answer)
        print(f"The {long_name} of {trigvalue_str} is {ans_int} degrees.")
    else:
        print(f"The {long_name} of {trigvalue_str} is {round(answer, 3)} degrees.")
        if input(f"Would you like more precision? ({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear}) ").strip().lower() == 'y':
            print(f"The {long_name} of {trigvalue_str} is {answer} degrees.")
    prompt_main_menu_return()

def main_menu_prompt():
    """Displays the main menu and returns the user's choice."""
    clear_terminal()
    print(f"{Color.green}***{Markings.bold}SELECT OPERATION{Markings.clear}{Color.green}***{Markings.clear}")
    print(f"{Color.green}* *{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}+ = ADD          {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}- = SUBTRACT     {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}* = MULTIPLY     {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}/ = DIVIDE       {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}^ = EXPONENTIATE {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}t = TRIGONOMETRY {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}r = RADICAL      {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* {Markings.bold}q = QUIT         {Markings.clear}{Color.green}*{Markings.clear}")
    print(f"{Color.green}* *{Markings.clear}")
    print(f"{Color.green}**********************{Markings.clear}")
    return input().strip().lower()

def trig_menu_prompt():
    """Displays the trigonometry menu and returns the user's choice."""
    clear_terminal()
    print(f"{Color.green}***{Markings.bold}TRIGONOMETRY{Markings.clear}{Color.green}***")
    print(f"{Color.green}* {Color.green}*")
    print(f"{Color.green}* {Markings.bold}s  = SINE     {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}c  = COSINE   {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}t  = TANGENT  {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}as = ARCSIN   {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}ac = ARCCOS   {Markings.clear}{Color.green}*")
    print(f"{Color.green}* {Markings.bold}at = ARCTAN   {Markings.clear}{Color.green}*")
    print(f"{Color.green}* *{Markings.clear}")
    print(f"{Color.green}******************{Markings.clear}")
    return input().strip().lower()

def main():
    """The main function to run the calculator application."""
    while True:
        operation = main_menu_prompt()
        
        if operation == '+':
            calculate_add()
        elif operation == '-':
            calculate_subtract()
        elif operation == '*':
            calculate_multiply()
        elif operation == '/':
            calculate_divide()
        elif operation == '^':
            calculate_exponent()
        elif operation == 'r':
            calculate_radical()
        elif operation == 't':
            run_trig_menu()
        elif operation == 'q':
            quit_in = input(f"{Color.red}{Markings.bold}ARE YOU SURE YOU WANT TO QUIT? {Markings.clear}({Color.green}y{Markings.clear}/{Color.red}n{Markings.clear})")
            if quit_in.lower() == 'y':
                clear_terminal()
                print("Calculator closed. Goodbye!")
                break
        else:
            print(f"{Color.red}ERROR: Invalid operation!{Markings.clear}")
            time.sleep(2)

if __name__ == "__main__":
    main()
