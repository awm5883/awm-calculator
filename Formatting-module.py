"""
FORMAT MODULE V1.0

A module for python with formats and colors for f-strings.

Notes: first commit

Author: Aidan McMillan
"""
print(f"\033[0m Hello World!")
class Color:
    
    def __init__(self):
        
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        yellow = '\033[33m'
        blue = '\033[34m'
        magenta = '\033[35m'
        cyan = '\033[36m'
        white = '\033[37m'

class Markings:
    
    def __init__(self):
        
        bold = '\033[1m'
        italic = '\033[3m'
        underline = '\033[4m'
        
class Clear:
    
    def __init__(self):
        
        clear = '\033[0m'
        
#END
        