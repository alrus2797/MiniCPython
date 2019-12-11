import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\lexer')

from op import *
from tag import *
from word import *

class Access(Op):
    def __init__(self, a, i, p):
        super().__init__(Word("[]", Tag.INDEX), p)
        self.array = a
        self.index = i

    def gen(self):
        return Access(self.array, self.index.reduce(), self.type)
    
    def jumping(self, t, f):
        self.emitjumps(self.reduce().toString(), t, f)
    
    def toString(self):
        return f"{self.array.toString()} [{self.index.toString()}]"