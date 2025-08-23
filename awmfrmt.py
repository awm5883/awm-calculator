"""
FORMAT MODULE V1.2

A module for python with formats and colors for f-strings.

Notes: Added message for solo running

Author: Aidan McMillan
"""

class Color:
    clear = '\033[0m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'

class Markings:
    clear = '\033[0m'
    bold = '\033[1m'
    italic = '\033[3m'
    underline = '\033[4m'

if __name__ == "__main__":
    print("This code is meant as a module! Please run awm-calculator-final.py to use the full calculator!")

#END
