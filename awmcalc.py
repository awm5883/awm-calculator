# Python Calculator
# Author: Aidan McMillan

import ti_system
import time
import math
from awmfrmt import Color, Markings
first_time = True
operation = None
inputs = [0, 0]

def get_inputs(operation) -> None:
    
    ti_system.clear_history()
    print("{0}{1}____{2} {3} ____".format(Color.green, Markings.bold, Markings.clear, operation)) # All other computations
    print("ENTER VALUE             ")
    inputs[0] = input("1st Value: ")
    
    ti_system.clear_history()
    print("{0} {1} {2}{3}____{4}".format(inputs[0], operation, Color.green, Markings.bold, Markings.clear))
    print("ENTER VALUE")
    inputs[1] = input("2nd Value: ")
    ti_system.clear_history()
    

def prompt_main_menu_return() -> None:
    input_val = input("Press {0}y{1} to return to the main menu.".format(Color.green, Markings.clear))
    while not input_val == 'y':
        input_val = input("ERROR: Invalid input. Please press 'y' to return to the main menu.")
    return

class Calculate:

    def __init__(self):
        ti_system.clear_history()
    
    class Arithmetic:
        
        def __init__(self):
            
            pass
        
        def add(self):
            
            try:
                get_inputs('+')
                answer = int(inputs[0]) + int(inputs[1])
                print("The sum of {0} and {1} is {2}".format(str(inputs[0]), str(inputs[1]), str(answer)))
                prompt_main_menu_return()
            except ValueError:
                print("{0}ERROR: Invalid inputs!{1}".format(Color.red, Markings.clear))
                return 1
        
        def subtract(self):
            
            try:
                get_inputs('-')
                answer = int(inputs[0]) - int(inputs[1])
                print("The difference between {0} and {1} is {2}".format(str(inputs[0]), str(inputs[1]), str(answer)))
            except ValueError:
                print("{0}ERROR: Invalid inputs!{1}".format(Color.red, Markings.clear))
                return 1
        
        def multiply(self):
            
            try:
                get_inputs('*')
                answer = int(inputs[0]) * int(inputs[1])
                print("The product of {0} and {1} is {2}".format(str(inputs[0]), str(inputs[1]), str(answer)))
            except ValueError:
                print("{0}ERROR: Invalid inputs!{1}".format(Color.red, Markings.clear))
                return 1
        
        def divide(self):
            
            get_inputs('/')
            answer = 0.0
            try:
                answer = int(inputs[0]) / int(inputs[1])
            except ZeroDivisionError:
                print("{0}ERROR: Cannot divide by zero!{1}".format(Color.red, Markings.clear))
                return 1
            except ValueError:
                print("{0}ERROR: Invalid inputs!{1}".format(Color.red, Markings.clear))
                return 1
            if answer.is_integer():
                ans_int = int(answer)
            print("The quotient of {0} and {1} is {2}".format(str(inputs[0]), str(inputs[1]), str(ans_int)))
        
        def exponent(self):
            
            try:
                get_inputs('^')
                answer = int(inputs[0]) ** int(inputs[1])
                print("{0} to the power of {1} equals {2}".format(str(inputs[0]), str(inputs[1]), str(answer)))
            except ValueError:
                print("{0}ERROR: Invalid inputs!{1}".format(Color.red, Markings.clear))
                return 1
    
    class Trig:
        
        def __init__(self):
            pass

        def arcsin(self):
            
            print("arcsin({0}{1}___{2}) ".format(Color.green, Markings.bold, Markings.clear))
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.asin(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print("The arc sine of {0} is {1} degrees.".format(trigvalue, ans_int))
                return
                
            print("The arc sine of {0} is {1} degrees.".format(trigvalue, round(answer, 3)))
            if not answer.is_integer():
                if input("Would you like more precision? ({0}y{1}/{2}n{1}){1} ".format(Color.green, Markings.clear, Color.red)).strip().lower() == 'y':
                    print("The arc sine of {0} is {1} degrees.".format(trigvalue, answer))
            
        def arccos(self):
            
            print("arccos({0}{1}___{2}) ".format(Color.green, Markings.bold, Markings.clear))
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.acos(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print("The arc cosine of {0} is {1} degrees.".format(trigvalue, ans_int))
                return
                
            print("The arc cosine of {0} is {1} degrees.".format(trigvalue, round(answer, 3)))
            if not answer.is_integer():
                if input("Would you like more precision? ({0}y{1}/{2}n{1}){1} ".format(Color.green, Markings.clear, Color.red)).strip().lower() == 'y':
                    print("The arc cosine of {0} is {1} degrees.".format(trigvalue, answer))
        
        def arctan(self):
            
            print("arctan({0}{1}___{2}) ".format(Color.green, Markings.bold, Markings.clear))
            print("ENTER VALUE (-1 to 1)\n")
            trigvalue = input().strip().lower()
            answer = math.atan(float(trigvalue))
            
            if answer.is_integer():
                ans_int = int(answer)
                print("The arc tangent of {0} is {1} degrees.".format(trigvalue, ans_int))
                return
                
            print("The arc tangent of {0} is {1} degrees.".format(trigvalue, round(answer, 3)))
            if not answer.is_integer():
                if input("Would you like more precision? ({0}y{1}/{2}n{1}){1} ".format(Color.green, Markings.clear, Color.red)).strip().lower() == 'y':
                    print("The arc tangent of {0} is {1} degrees.".format(trigvalue, answer))
                    
        def sin(self):
            
            print("sin({0}{1}___{2}) ".format(Color.green, Markings.bold, Markings.clear))
            print("ENTER VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.sin(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print("The sine of {0} is {1} degrees.".format(trigvalue, ans_int))
                return
                
            print("The sine of {0} is {1} degrees.".format(trigvalue, round(answer, 3)))
            if not answer.is_integer():
                if input("Would you like more precision? ({0}y{1}/{2}n{1}){1} ".format(Color.green, Markings.clear, Color.red)).strip().lower() == 'y':
                    print("The sine of {0} is {1} degrees.".format(trigvalue, answer))
            
            
        def cos(self):
            
            print("cos({0}{1}___{2}) ".format(Color.green, Markings.bold, Markings.clear))
            print("ENTER VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.cos(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print("The cosine of {0} is {1} degrees.".format(trigvalue, ans_int))
                return
                
            print("The cosine of {0} is {1} degrees.".format(trigvalue, round(answer, 3)))
            if not answer.is_integer():
                if input("Would you like more precision? ({0}y{1}/{2}n{1}){1} ".format(Color.green, Markings.clear, Color.red)).strip().lower() == 'y':
                    print("The cosine of {0} is {1} degrees.".format(trigvalue, answer))
            
        def tan(self):
            
            print("tan({0}{1}___{2}) ".format(Color.green, Markings.bold, Markings.clear))
            print("SELECT VALUE (IN DEGREES)\n")
            trigvalue = input().strip().lower()
            answer = math.tan(math.radians(float(trigvalue)))
            
            if answer.is_integer():
                ans_int = int(answer)
                print("The tangent of {0} is {1} degrees.".format(trigvalue, ans_int))
                return
                
            print("The tangent of {0} is {1} degrees.".format(trigvalue, round(answer, 3)))
            if not answer.is_integer():
                if input("Would you like more precision? ({0}y{1}/{2}n{1}){1} ".format(Color.green, Markings.clear, Color.red)).strip().lower() == 'y':
                    print("The tangent of {0} is {1} degrees.".format(trigvalue, answer))
            
    def radical(self):
        
        print("{0}{1}____{2}th root of ____".format(Color.green, Markings.bold, Markings.clear))
        print("ENTER VALUE      ")
        inputs[0] = input()
        
        suffix = "th"
        if int(inputs[0]) % 10 == 1:
            suffix = "st"
        elif int(inputs[0]) % 10 == 2:
            suffix = "nd"
        elif int(inputs[0]) % 10 == 3:
            suffix = "rd"
        
        print("{0}{1} root of {2}{3}____{4}".format(inputs[0], suffix, Color.green, Markings.bold, Markings.clear))
        print("ENTER VALUE")
        inputs[1] = input()
        
        answer = float(inputs[1]) ** (1 / float(inputs[0])) # Radical in exponent form
        
        display_answer = 0
        if answer.is_integer():
            display_answer = int(answer)
        else:
            display_answer = round(answer, 3)
            
        print("The {0}{1} root of {2} is {3}".format(inputs[0], suffix, inputs[1], str(display_answer)))

        if input("Would you like more precision? ({0}y{1}/{2}n{1}){1}".format(Color.green, Markings.clear, Color.red)) == 'y':
            print("The {0}{1} root of {2} is {3}".format(inputs[0], suffix, inputs[1], str(answer)))
        
        return 0
    def simple_algebra(self):
        print("First argument: {0}_{1} (x{2}0{1})".format(Color.green, Markings.clear, Markings.superscript))

def main_menu_prompt(): # Print main menu and recieve operation
    
    ti_system.clear_history()
    print("{0}***{1}SELECT OPERATION{2}{0}***{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* *{1}".format(Color.green, Markings.clear))
    print("{0}* {1}+ = ADD          {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}- = SUBTRACT     {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}* = MULTIPLY     {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}/ = DIVIDE       {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}^ = EXPONENTIATE {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}t = TRIGONOMETRY {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}r = RADICAL      {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}q = QUIT         {2}{0}*{2}".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* *{1}".format(Color.green, Markings.clear))
    print("{0}**********************{1}".format(Color.green, Markings.clear))
    
    command = input().strip().lower()
    ti_system.clear_history()
    return command # return the input


def trig_menu(): # Trig menu (also returns input)
    
    ti_system.clear_history()
    print("{0}***{1}TRIGONOMETRY{2}{0}***".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {0}*".format(Color.green))
    print("{0}* {1}s  = SINE     {2}{0}*".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}c  = COSINE   {2}{0}*".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}t  = TANGENT  {2}{0}*".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* {1}a_ = INVERSE  {2}{0}*".format(Color.green, Markings.bold, Markings.clear))
    print("{0}* *{1}".format(Color.green, Markings.clear))
    print("{0}******************{1}".format(Color.green, Markings.clear))
    
    command = input().strip().lower()
    ti_system.clear_history()
    return command


def main():

    arithmetic = Calculate.Arithmetic()
    radical = Calculate()
    trig = Calculate.Trig()
    operation = main_menu_prompt()

    # This 'if/elif' block replaces the original 'match' statement for compatibility
    if operation == '+':
        arithmetic.add()
    elif operation == '-':
        arithmetic.subtract()
    elif operation == '*':
        arithmetic.multiply()
    elif operation == '/':
        arithmetic.divide()
    elif operation == '^':
        arithmetic.exponent()
    elif operation == 'r':
        radical.radical()
    elif operation == 'q':
        quit_in = input("{0}{1}ARE YOU SURE YOU WANT TO QUIT? {2}({3}y{2}/{0}n{2})".format(Color.red, Markings.bold, Markings.clear, Color.green))
        if quit_in == 'y':
            quit()
        elif quit_in == 'n':
            main_menu_prompt()
        else:
            time_left = 3
            while time_left >= 0:
                print("{0}ERROR: Invalid input. Reverting to main menu in {1} seconds.{2}".format(Color.red, str(round(time_left, 3)).zfill(3), Markings.clear), end = '\r')
                time.sleep(0.01)
                time_left -= 0.01
            ti_system.clear_history()
    elif operation == 't':
        trig_op = trig_menu()
        # This 'if/elif' block replaces the nested 'match' statement
        if trig_op == 'as':
            trig.arcsin()
        elif trig_op == 'ac':
            trig.arccos()
        elif trig_op == 'at':
            trig.arctan()
        elif trig_op == 's':
            trig.sin()
        elif trig_op == 'c':
            trig.cos()
        elif trig_op == 't':
            trig.tan()
        else:
            print("{0}ERROR: Invalid trig operation!{1}".format(Color.red, Markings.clear))
    else:
        print("{0}ERROR: Invalid operation!{1}".format(Color.red, Markings.clear))

while True: # Main loops forever
    main()
