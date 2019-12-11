import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\lexer')


from expr import *
from word import *


class Temp(Expr):
    count = 0
    number = 0
    
    def __init__(self, p):
        super().__init__(Words.temp, p)
        self.count += 1
        self.number = self.count
    
    def toString(self):
        return f"t{self.number}"