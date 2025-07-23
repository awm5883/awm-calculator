#FOUR-FUNCTION CALCULATOR v2.2
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
    print("*                    *")
    print("**********************")
    operation = input().strip().lower()
    return operation
def getInputs(operation):
    if operation == '*':
        print("____ * ____")
        print("^^^^       ")
        print("ENTER VALUE")
        num1 = input("1st Value: ")
        try:
            print(num1.zfill(4) + " * ____")
        except:
            print("ERROR: Invalid 1st input in function getInputs branch *")
            return 1
        print("       ^^^^")
        print("ENTER VALUE")
        num2 = input("2nd Value: ")
        answer = int(num1) * int(num2)
        try:
            print("The product of " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function getInputs branch *")
            return 1
    elif operation == '+':
        print("____ + ____")
        print("^^^^       ")
        print("ENTER VALUE")
        num1 = input("1st Value: ")
        try:
            print(num1.zfill(4) + " + ____")
        except:
            print("ERROR: Invalid 1st input in function getInputs branch +")
            return 1
        print("       ^^^^")
        print("ENTER VALUE")
        num2 = input("2nd Value: ")
        answer = int(num1) + int(num2)
        try:
            print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function getInputs branch +")
            return 1
        return 0
    elif operation == '-':
        print("____ - ____")
        print("^^^^       ")
        print("ENTER VALUE")
        num1 = input("1st Value: ")
        try:
            print(num1.zfill(4) + " - ____")
        except:
            print("ERROR: Invalid 1st input in function getInputs branch -")
            return 1
        print("       ^^^^")
        print("ENTER VALUE")
        num2 = input("2nd Value: ")
        answer = int(num1) - int(num2)
        try:
            print("The difference between " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function getInputs branch -")
            return 1
        return 0
    elif operation == '/':
        print("____ / ____")
        print("^^^^       ")
        print("ENTER VALUE")
        num1 = input("1st Value: ")
        try:
            print(num1.zfill(4) + " / ____")
        except:
            print("ERROR: Invalid 1st input in function getInputs branch -")
            return 1
        print("       ^^^^")
        print("ENTER VALUE")
        num2 = input("2nd Value: ")
        try:
            answer = int(num1) / int(num2)
        except:
            print("ERROR: Cannot divide by zero!")
            return 1
        try:
            print("The quotient between " + str(num1) + " and " + str(num2) + " is " + str(answer))
        except:
            print("ERROR: Answer print error in function getInputs branch /")
            return 1
        if goAgain(firstTime) == 1:
            return 1
        else:
            print("ERROR: Invalid input recieved when asking to restart in function getInputs branch /")
            return 1
        return 0
    else:
        print("ERROR: Invalid operation in function getInputs")
        return 1
while True:
    if goAgain(firstTime):
        firstTime = False
        operation = mainMenu()
        getInputs(operation)
    else:
        print("Exiting calculation...")
        time.sleep(3)
        print("Calculation Exited")
        break
