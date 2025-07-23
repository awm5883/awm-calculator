#SEVEN-FUNCTION CALCULATOR V5.1

import time
import math
promptRestartVar = True
firstTime = True
num1 = None
num2 = None
operation = None

def getInputs(operation) -> None:
    
    print(f"____ {operation} ____") # All other computations
    print(f"^^^^                 ")
    print(f"ENTER VALUE HERE     ")
    
    num1 = input("1st Value: ")
    
    try:
        print(f"{num1.zfill(4)} {operation} ____")
    except TypeError:
        print("ERROR: Invalid 1st input in function main branch *")
        return 1
    print("       ^^^^")
    print("ENTER VALUE HERE")
    num2 = input("2nd Value: ")
    
class calculate:
    
    def __init__(self):
        pass
    
    class arithmetic:
        
        def __init__(self):
            
            pass
        
        def add(self, num1, num2):
            
            getInputs('+')
            answer = int(num1) + int(num2)
            return f"The sum of {str(self.num1)} and {str(self.num2)} is {str(self.answer)}"
        
        def subtract(self, num1, num2):
            
            getInputs('-')
            answer = int(num1) - int(num2)
            return f"The difference between {str(self.num1)} and {str(self.num2)} is {str(self.answer)}"
        
        def multiply(self, num1, num2):
            
            getInputs('*')
            answer = int(num1) * int(num2)
            return f"The product of {str(self.num1)} and {str(self.num2)} is {str(self.answer)}"
        
        def divide(self, num1, num2):
            
            getInputs('/')
            try:
                answer = int(num1) / int(num2)
            except ZeroDivisionError:
                return "ERROR: Cannot divide by zero!"
            if answer.is_integer():
                ans_int = int(answer)
            return f"The quotient between {str(self.num1)} and {str(self.num2)} is {str(self.ans_int)}"
        
        def exponent(self, num1, num2):
            
            getInputs('^')
            answer = int(num1) ** int(num2)
            return f"{str(self.num1)} to the power of {str(self.num2)} equals {str(self.answer)}"
    
    class trig:
        
        def __init__(self):
            
            trigValue  = None
            trigCmdStr = None
            
        def arcsin(self):
            
            print("arcsin(___) ")
            print("       ^^^  ")
            print("ENTER VALUE (-1 to 1)\n")
            trigValue = input().strip().lower()
            answer = math.asin(float(trigValue))
            trigCmdStr = "arc sine"
            
        def arccos(self):
            
            print("arccos(___) ")
            print("       ^^^  ")
            print("ENTER VALUE (-1 to 1)\n")
            trigValue = input().strip().lower()
            answer = math.acos(float(trigValue))
            trigCmdStr = "arc cosine"
        
        def arctan(self):
            
            print("arctan(___) ")
            print("       ^^^  ")
            print("ENTER VALUE (-1 to 1)\n")
            trigValue = input().strip().lower()
            answer = math.atan(float(trigValue))
            trigCmdStr = "arc tangent"
        
        def sin(self):
            
            print("sin(___) ")
            print("    ^^^  ")
            print("ENTER VALUE (IN DEGREES)\n")
            trigValue = input().strip().lower()
            answer = math.sin(math.radians(float(trigValue)))
            trigCmdStr = "sine"
            
        def cos(self):
            
            print("cos(___) ")
            print("    ^^^  ")
            print("ENTER VALUE (IN DEGREES)\n")
            trigValue = input().strip().lower()
            answer = math.cos(math.radians(float(trigValue)))
            trigCmdStr = "cosine"
            
        def tan(self):
            
            print("tan(___) ")
            print("    ^^^  ")
            print("SELECT VALUE (IN DEGREES)\n")
            trigValue = input().strip().lower()
            answer = math.tan(math.radians(float(trigValue)))
            trigCmdStr = "tangent"
            
    def radical(self):
        
        print("____th root of ____")
        print("^^^^             ")
        print("ENTER VALUE      ")
        num1 = input()
        
        suffix = "th"
        if int(num1) % 10 == 1:
            suffix = "st"
        elif int(num1) % 10 == 2:
            suffix = "nd"
        elif int(num1) % 10 == 3:
            suffix = "rd"
        
        print(f"{num1.zfill(2)}{suffix} root of ____")
        print("             ^^^^")
        print("ENTER VALUE HERE")
        num2 = input()
        
        answer = float(num2) ** (1 / float(num1)) # Radical in exponent form
        ans_int = 0
        if answer.is_integer():
            ans_int = int(answer)
        print(f"The {num1}{suffix} root of {num2} is {str(round(ans_int, 3))}")
        if ans_int:
            return 0
        if input("Would you like more precision? (y/n)") == 'y':
            print(f"The {num1}{suffix} root of {num2} is {str(answer)}")
        return 0
    
def promptRestart(firstTime): # Perform another calculation message and surrounding computation.
    
    if firstTime == True:
        firstTime = False
        return 2
    else:
        promptRestartStr = input("Do you want to perform another calculation? (y/n)")
        if promptRestartStr == 'y':
            promptRestartVar = True
            return 2
        elif promptRestartStr == 'n':
            promptRestartVar = False
            return 0 # Success
        else:
            print("ERROR: Invalid input recieved when asking to restart in function promptRestart")
            return 1


def mainMenuPrompt(): # Print main menu and recieve operation 
    
    print("\n\n\n\n\n\n\n\n\n\n\n")
    print("***SELECT OPERATION***")
    print("*                    *")
    print("*  * = MULTIPLY      *")
    print("*  + = ADDITION      *")
    print("*  - = SUBTRACT      *")
    print("*  / = DIVIDE        *")
    print("*  ^ = EXPONENTIATE  *")
    print("*  t = TRIGONOMETRY  *")
    print("*  r = RADICAL       *")
    print("*                    *")
    print("**********************")
    command = input().strip().lower()
    return command # return the input


def trigMenu(): # Trig menu (also returns input)
    print("\n\n\n\n\n\n\n\n\n")
    print("***TRIGONOMETRY***")
    print("*                *")
    print("* s  = SINE      *")
    print("* c  = COSINE    *")
    print("* t  = TANGENT   *")
    print("* a_ = INVERSE   *")
    print("*                *")
    print("******************")
    command = input().strip().lower()
    return command


def main():

    match operation:
        
        case '+':
            
            print(calculate.add(num1, num2))
            
        case '-':
            
            print(calculate.subtract(num1, num2))
            
        case '*':
            
            print(calculate.multiply(num1, num2))
            
        case '/':
            
            print(calculate.divide(num1, num2))
            
        case '^':
            
            print(calculate.exponent(num1, num2))

def mainMenuAndGetInputs():
    
    return getInputs(mainMenuPrompt())

while True: # Loop forever, "Go again?" and sleep logic.
    if promptRestart(firstTime):
        firstTime = False
        operation = mainMenuAndGetInputs()
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
        print("Press ENTER to restart")
        if input():
            print("Restarting", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            firstTime = True
        else:
            print("Restarting", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            print(".", end = "")
            time.sleep(0.5)
            firstTime = True
