import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\lexer')

from type import *
from tag import *

class Array(Type):
    def __init__(self, sz, p):
        super().__init__("[]", Tag.INDEX, sz * p.width)
        self.size   = sz
        self.of     = p
    
    def toString(self):
        return f"[{self.size}] {self.of.toString()}"