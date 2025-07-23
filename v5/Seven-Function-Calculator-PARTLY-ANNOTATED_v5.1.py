# SEVEN-FUNCTION CALCULATOR V5.1
# All the notes are written after a hashtag symbol. This tells the computer to ignore the rest of the line.
# Import Modules
# Modules are new rules that can do things that cannot be done as easily normally.
import time # The time module lets the user delay for a certain amount of time.
import math # The math module includes functions like sine, cosine, and square root.
# Initialize variables
# Variables are placeholders for values.
# A placeholder is a value that stands in for another value that can be changed throughout the code.
# For example, firstTime is used to bypass the function asking if the user wants to do another calculation.
# However, this is changed to False once the user is not performing their first calculation.
# The values True and False are called "booleans"
# A boolean is used for a value that only needs two states and is often used for when a function needs to return if it had an error.
# Other common variable values are strings, integers, and floats.
goAgainVar = True
firstTime = True
# First Function!
# This is a function defenition. It only needs to be written once.
# There are three parts to the defenition.
# 1. The word "def"
#   "def" tells python that you are trying to define a function.
# 2. The name.
#    The name of this function is goAgain. The capitalization is known as camel casing, and it is used in coding as the widespread method of capitalization.
#    The name of the function is what the user will type later in the code to call the code inside the function. Think of the function as a placeholder, but for code!
# 3. The parentheses with firstTime
#    firstTime is known as an "argument". Arguments are values that are passed into the function that affect the outputs.
#    For example, when you add, that's a function! The two numbers you're adding are the arguments, and the output is the sum!
#    An addition function would look something like this:
#    def add(num1, num2):
#        sum = num1 + num2
#        return sum
#    Notice the two arguments and the variable inside.
# Variables defined inside of a function are called "local variables." They don't exist outside of the function.
# Functions are like their own bubbles, where variables defined inside don't go out.
# All function defenitions need to be indented!
# *******CHECK YOUR UNDERSTANDING*******
# Try to write a function that multiplies two numbers.
# You can use the above one as a template.
# Back to the code!
def goAgain(firstTime):
    # One line in and there's a new concept: an if statement!
    # If statements are exactly what they sound like. If the expression inside is true, the code inside runs!
    # Be careful with indentation here! The code inside the if statement needs to be indented just like a function defenition.
    # Also notice the use of TWO equals signs. ONE equals sign sets the object on the left to be equal to the one on the right, while TWO CHECK if they are equal.
    if firstTime == True: # <-- First if statement!
        # This part sets the firstTime variable to False, as this isn't the first time anymore, then returns 2, which means "Go again!" Though this isn't used, it's useful for debugging.
        # Every time a function has an error in this code, it returns 1. Things like this are useful for debugging.
        firstTime = False
        return 2 # <-- return the value, and exit the function.
    
    else:# Ahh, the if statement's inseparable friend, else. Else runs the code inside if the if statement is false.
        # You'll notice a new function here - one that's built into python. Can you spot it?
        
        # input()!
        # input() can take one argument, a string to be printed, like the print() function.
        # There's one difference, though.
        # input() returns the string that the user inputs.
        # A string is a line of text, with quotes around it when written in code.
        # This will be important later, so make sure you understand.
        # When a function outputs a value, it acts like a variable with that value.
        # For example, if the user inputs 'n', then the input() function acts like a string variable with the value 'n'
        goAgainStr = input("Do you want to perform another calculation? (y/n)")
        # Can you figure out what this does? Remember that "return" still returns the value to the function goAgain, not the if/elif/else.
        # Oh! elif! This is another part of an if statement, where if the if statement is false, it first checks the elif, then goes to the else.
        # These still need to be indented, and can be stacked as long as you want.
        if goAgainStr == 'y':
            goAgainVar = True
            return 2
        elif goAgainStr == 'n':
            goAgainVar = False
            return 0
        else:
            print("ERROR: Invalid input recieved when asking to restart in function goAgain")
            return 1
# The end of our first function! Phew, that one was tricky. With your newfound knowledge, try to go through this one on your own.
# There will be comments to help you if you need them.
def mainMenu():
    # Many prints can be used in a row, and are good for making are with characters.
    # \n is known as a "newline character". These are like hitting enter on your keyboard, and there's an invisible one at the end of every line you type.
    # When you type an essay, to the computer, it's one line separated by \n characters.
    # When using these in your own programs, remember to use backslash, below backspace, NOT forward slash (/) which is beside the shift key.
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
    # Another variable defenition, and a blank input() function (this does work).
    # Notice the .strip() and .lower()
    # .strip() removes the spaces from the response, so "      +   " becomes "+"
    # .lower() makes all of the letters entered lowercase, so "T" becomes "t"
    # Both of these combined make it much more friendly to user error, which is EXTREMELY important when writing code.
    # For example, someone who inputs "  R    " will have it corrected to "r" and thus, the code will go to the "radical" section. Handy!
    command = input().strip().lower() # Think of the .strip() and .lower() as suffixes or modifiers to the value.
    return command # You can return variables, too!
def trigMenu(): # Another function defenition with more print statements.
    print("\n\n\n\n\n\n\n\n\n") 
    print("***TRIGONOMETRY***")
    print("*                *")
    print("* s  = SINE      *")
    print("* c  = COSINE    *")
    print("* t  = TANGENT   *")
    print("* a_ = INVERSE   *")
    print("*                *")
    print("******************")
    command = input().strip().lower() # We've been here before...
    return command
def main(operation): # Main! Now we're talking! Most of the "meat" of the code is right here, so strap in!
    # That's a big if! (statement) But - it's pretty simple.
    # All != means is NOT equal to.
    # That means all the function does is give an error if the operation selected is not one of the valid ones, and if it is, it moves on.
    if operation != '+' and operation != '*' and operation != '-' and operation != '/' and operation != '^' and operation != 't' and operation != 'r': 
        print("ERROR: Invalid operation in function main")
        return 1 # Again, 1 is an error.
    # There are two "special" operations here. 't' and 'r'.
    # T goes to a separate trigonometry menu (Lines 102-113), while 'r' requires some special formatting.
    if operation == 't': # Double equals CHECKS, single equals SETS.
        trigCommand = trigMenu() # Because trigMenu() returns the input, we save that as a variable.
        trigValue = None   # Variables are often defined as None before use so that they aren't "too local".
        trigCmdStr = None  # These two store the input value and the string used to identify the operation respectively.
        # Try, try, try again. But don't in python!
        # Write your code until it works, don't give up, but use the try: function!
        # The try function has two parts: try: and except:.
        # The function tries the try: part, and if it would give an error, it uses the except: block instead.
        # It's often used for error messages and debugging.
        try: 
            if trigCommand[0] == 'a': # BIG elif stack incoming!
                # Have you noticed the numbers in brackets? Those are the character number in the string.
                # Python strings are "zero-indexed" so the first character is number 0.
                # For example, the function below
                # def myFifthLetter(name):
                #    print(name[4])
                # myFifthLetter("Aidan")
                # Would print
                # n
                # And not
                # a
                # Because python is zero-indexed.
                # ********CHECK FOR UNDERSTANDING********
                # What would this print?
                # myName = Sebastian
                # print(myName[6])
                #****************************************
                # So the trigCommand[0] is looking for the first character of the string trigInput
                # If it's a, indicating the user wants to do an arc, or inverse function (MATH STUFF YOU DON'T NEED TO KNOW) then the code checks the second letter.
                if trigCommand[1] == 's': 
                    print("arcsin(___) ")
                    print("       ^^^  ")
                    print("SELECT VALUE (-1 to 1)\n") # The newline character strikes again. Notice it is INSIDE the quotes, unlike a variable.
                    trigValue = input().strip().lower() # Again with the suffix/modifiers. Always program your code to be "foolproof"
                    # Lots to unpack here. First, we're using a variable called answer, which stores, you guessed it, the answer.
                    # Notice the "asin" function (arc sine) has the prefix "math". Remember the "modules" we defined at the start?"
                    # Well "asin" is a part of the "math" module. Think of math as a reference to what dictionary to use.
                    # If I told you to look in the Spanish dictionary for antidisestablishmentarianism, you wouldn't find it, because that's an English word.
                    # "Math" is saying to look in the "math" dictionary for the word "asin".
                    # Next, float. Float is a type of value (remember strings?) that allows for decimal numbers to be operated on (+, -, *, /, math stuff.)
                    # float(trigValue) takes the string trigValue and turns it into a float - ONLY FOR THIS OPERATION. trigValue is STILL A STRING OTHERWISE.
                    # Next, the trigCmdStr, which simply is a more user-friendly way to say the operation used, and is used when printing the answer.
                    answer = math.asin(float(trigValue))
                    trigCmdStr = "arc sine"
                elif trigCommand[1] == 'c': # Repeat for arc cosine
                    print("arccos(___) ")
                    print("       ^^^  ")
                    print("SELECT VALUE (-1 to 1)\n")
                    trigValue = input().strip().lower()
                    answer = math.acos(float(trigValue))
                    trigCmdStr = "arc cosine"
                elif trigCommand[1] == 't': # Repeat for arc tangent, but it doesn't have the -1 to 1 restriction.
                    print("arctan(___) ")
                    print("       ^^^  ")
                    print("SELECT VALUE\n")
                    trigValue = input().strip().lower()
                    answer = math.atan(float(trigValue))
                    trigCmdStr = "arc tangent"
                else: # Finally, the error. Give a location, and what happened, then exit the function and try again.
                    print("ERROR: Invalid operation in function trig")
                    return 1
            elif trigCommand == 's': # Now, we check the WHOLE string to see if it's 's'. This is because we're not handling inverse functions anymore.
                print("sin(___) ")
                print("    ^^^  ")
                print("SELECT VALUE (IN DEGREES)\n") # Specify units!
                trigValue = input().strip().lower() # More suffixes
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
        