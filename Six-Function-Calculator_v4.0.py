#SEVEN-FUNCTION CALCULATOR V5.1
import time
import math
goAgainVar = True
firstTime = True
def goAgain(firstTime):
    if firstTime == True:
        firstTime = False
        return 2
    else:
        goAgainStr = input("Do you want to perform another calculation? (y/n)")
        if goAgainStr == 'y':
            goAgainVar = True
            return 2
        elif goAgainStr == 'n':
            goAgainVar = False
            return 0
        else:
            print("ERROR: Invalid input recieved when asking to restart in function goAgain")
            return 1
def mainMenu():
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
    return command
def trigMenu():
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
def main(operation):
    if operation != '+' and operation != '*' and operation != '-' and operation != '/' and operation != '^' and operation != 't' and operation != 'r':
        print("ERROR: Invalid operation in function main")
        return 1
    if operation == 't':
        trigCommand = trigMenu()
        trigValue = None
        trigCmdStr = None 
        try:
            if trigCommand[0] == 'a':
                if trigCommand[1] == 's':
                    print("arcsin(___) ")
                    print("       ^^^  ")
                    print("SELECT VALUE (-1 to 1)\n")
                    trigValue = input().strip().lower()
                    answer = math.asin(float(trigValue))
                    trigCmdStr = "arc sine"
                elif trigCommand[1] == 'c':
                    print("arccos(___) ")
                    print("       ^^^  ")
                    print("SELECT VALUE (-1 to 1)\n")
                    trigValue = input().strip().lower()
                    answer = math.acos(float(trigValue))
                    trigCmdStr = "arc cosine"
                elif trigCommand[1] == 't':
                    print("arctan(___) ")
                    print("       ^^^  ")
                    print("SELECT VALUE (-1 to 1)\n")
                    trigValue = input().strip().lower()
                    answer = math.atan(float(trigValue))
                    trigCmdStr = "arc tangent"
                else:
                    print("ERROR: Invalid operation in function trig")
                    return 1
            elif trigCommand == 's':
                print("sin(___) ")
                print("    ^^^  ")
                print("SELECT VALUE (IN DEGREES)\n")
                trigValue = input().strip().lower()
                answer = math.sin(math.radians(float(trigValue)))
                trigCmdStr = "sine"
            elif trigCommand == 'c':
                print("cos(___) ")
                print("    ^^^  ")
                print("SELECT VALUE (IN DEGREES)\n")
                trigValue = input().strip().lower()
                answer = math.cos(math.radians(float(trigValue)))
                trigCmdStr = "cosine"
            elif trigCommand == 't':
                print("tan(___) ")
                print("    ^^^  ")
                print("SELECT VALUE (IN DEGREES)\n")
                trigValue = input().strip().lower()
                answer = math.tan(math.radians(float(trigValue)))
                trigCmdStr = "tangent"
            else:
                print("ERROR: Invalid operation in function trig")
                return 1
            try:
                print(f"The {trigCmdStr} of {trigValue} degrees is {answer:.5f}")
                return 0
            except:
                print("ERROR: Error printing answer in function trig")
                return 1
        except:
            print("ERROR: Computation error in function trig")
            return 1
    elif operation == 'r':
        print("____th root of ____")
        print("^^^^             ")
        print("ENTER VALUE      ")
        num1 = input()
        print(num1.zfill(2) + "th root of ____")
        print("            ^^^^")
        print("ENTER VALUE HERE")
        num2 = input()
        answer = float(num2) ** (1 / float(num1))
        print("The " + num1 + "th root of " + num2 + " is " + str(answer))
        return 0
    print("____ " + operation + " ____")
    print("^^^^       ")
    print("ENTER VALUE")
    num1 = input("1st Value: ")
    try:
        print(num1.zfill(4) + " " + operation + " ____")
    except:
        print("ERROR: Invalid 1st input in function main branch *")
        return 1
    print("       ^^^^")
    print("ENTER VALUE")
    num2 = input("2nd Value: ")
    if operation == '*':
        answer = int(num1) * int(num2)
        try:
            print("The product of " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function main")
            return 1
        return 0
    elif operation == '+':
        answer = int(num1) + int(num2)
        try:
            print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function main branch +")
            return 1
        return 0
    elif operation == '-':
        answer = int(num1) - int(num2)
        try:
            print("The difference between " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function main branch -")
            return 1
        return 0
    elif operation == '/':
        try:
            answer = int(num1) / int(num2)
        except:
            print("ERROR: Cannot divide by zero!")
            return 1
        try:
            print("The quotient between " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function main branch /")
            return 1
        if goAgain(firstTime) == 1:
            return 1
        else:
            print("ERROR: Invalid input recieved when asking to restart in function main branch /")
            return 1
        return 0
    elif operation == '^':
        answer = int(num1) ** int(num2)
        try:
            print("The answer to " + str(num1) + " to the power of " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function main branch ^")
            return 1
        return 0
    else:
        print("ERROR: Invalid operation in function main")
while True:
    if goAgain(firstTime):
        firstTime = False
        main(mainMenu())
    else:
        print("Exiting calculation...")
        time.sleep(3)
        print("Calculation Exited")
        time.sleep(1)
        print("Press any button to restart")
        if input():
            print("Restarting")
            time.sleep(0.5)
            firstTime = True
        