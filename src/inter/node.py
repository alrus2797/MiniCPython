import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\lexer')

from lexer import *



class Node:
    lexline = 0
    labels = 0

    def __init__(self):
        self.lexline = Lexer.line
    
    def error(self, s):
        raise Exception(f"Error near line {str(lexline)}:  {s}")

    def new_label(self):
        self.labels += 1
        return self.labels
    
    def emit_label(self, i):
        print(f"L {i}: ", end="")
    
    def emit(self, s):
        print(f"\ts" )
