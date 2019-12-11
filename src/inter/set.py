import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from type import *
from stmt import *

class Set(Stmt):
    def __init__(self, i, x):
        self.id = i
        self.expr = x
        if self.check(self.id.type, self.expr.type) == None: self.error("Type error")
    
    def check(self, p1, p2):
        if Type.numeric(p1) and Type.numeric(p2): return p2
        elif p1 == Types.Bool and p2 == Types.Bool: return p2
        else: return None

    def gen(self, b, a):
        self.emit(f"{self.id.toString()} = {self.expr.gen().toString()}")