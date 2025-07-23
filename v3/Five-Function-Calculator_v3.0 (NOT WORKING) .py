#FOUR-FUNCTION CALCULATOR V3.0
import time
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
    print("*                    *")
    print("**********************")
    command = input().strip().lower()
    return command
def main(operation):
    if operation != '+' and operation != '*' and operation != '-' and operation != '/' and operation != '^':
        print("ERROR: Invalid operation in function main")
        return 1
    print("____ " + operation + " ____")
    print("^^^^       ")
    print("ENTER VALUE")
    num1 = input("1st Value: ")
    try:
        print(num1.zfill(4) + operation + " ____")
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
        break
        