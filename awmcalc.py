# PYTHON CALCULATOR (TI-84 Version)
# Author: Aidan McMillan

import time
import math
from awmfrmt import Color, Markings
import ti_system

# --- Utility Functions ---
def clear():
    ti_system.clear_history()

def get_input(prompt):
    while True:
        val = input(prompt)
        try:
            float(val)
            return val
        except ValueError:
            print("{0}ERROR: Invalid input.{1}".format(Color.red, Markings.clear))

def prompt_return():
    input("Press Enter to return to the menu...")

# --- Calculation Functions ---
def add():
    clear()
    print("Addition")
    num1 = float(get_input("1st Value: "))
    num2 = float(get_input("2nd Value: "))
    print("Result: {0}".format(num1 + num2))
    prompt_return()

def subtract():
    clear()
    print("Subtraction")
    num1 = float(get_input("1st Value: "))
    num2 = float(get_input("2nd Value: "))
    print("Result: {0}".format(num1 - num2))
    prompt_return()

def multiply():
    clear()
    print("Multiplication")
    num1 = float(get_input("1st Value: "))
    num2 = float(get_input("2nd Value: "))
    print("Result: {0}".format(num1 * num2))
    prompt_return()

def divide():
    clear()
    print("Division")
    num1 = float(get_input("1st Value: "))
    num2 = float(get_input("2nd Value: "))
    if num2 == 0:
        print("{0}ERROR: Cannot divide by zero.{1}".format(Color.red, Markings.clear))
    else:
        print("Result: {0}".format(num1 / num2))
    prompt_return()

def exponent():
    clear()
    print("Exponentiation")
    base = float(get_input("Base: "))
    power = float(get_input("Power: "))
    print("Result: {0}".format(base ** power))
    prompt_return()

def radical():
    clear()
    print("Radical (nth root)")
    n = float(get_input("Enter the root (e.g., 2 for square root): "))
    num = float(get_input("Enter the number: "))
    if num < 0 and n % 2 == 0:
        print("{0}ERROR: Invalid operation.{1}".format(Color.red, Markings.clear))
    else:
        print("Result: {0}".format(num ** (1/n)))
    prompt_return()

def trig():
    clear()
    print("Trigonometry Menu")
    print("s) sin  c) cos  t) tan")
    print("as) asin ac) acos at) atan")
    op = input("Select: ").lower()

    func_map = {'s': math.sin, 'c': math.cos, 't': math.tan,
                'as': math.asin, 'ac': math.acos, 'at': math.atan}
    
    if op not in func_map:
        print("{0}ERROR: Invalid selection.{1}".format(Color.red, Markings.clear))
        prompt_return()
        return

    is_inverse = op.startswith('a')
    if is_inverse:
        val = float(get_input("Value (-1 to 1): "))
        if val < -1 or val > 1:
            print("{0}ERROR: Value out of range.{1}".format(Color.red, Markings.clear))
            prompt_return()
            return
        # Convert result from radians to degrees
        result = math.degrees(func_map[op](val))
    else:
        val = float(get_input("Value (in degrees): "))
        # Convert input from degrees to radians
        result = func_map[op](math.radians(val))
    
    print("Result: {0}".format(result))
    prompt_return()

# --- Main Application Loop ---
def main():
    op_map = {'+': add, '-': subtract, '*': multiply, '/': divide,
              '^': exponent, 'r': radical, 't': trig}
    
    while True:
        clear()
        print("--- Calculator ---")
        print("+ Addition    - Subtraction")
        print("* Multiply    / Divide")
        print("^ Exponent    r Radical")
        print("t Trigonometry")
        print("q Quit")
        choice = input("Choose operation: ").lower()

        if choice == 'q':
            print("Goodbye!")
            break
        
        if choice in op_map:
            op_map[choice]()
        else:
            print("{0}ERROR: Invalid operation.{1}".format(Color.red, Markings.clear))
            time.sleep(1)

main()
