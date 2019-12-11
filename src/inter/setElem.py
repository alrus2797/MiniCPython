import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from array import *
from type import *

from stmt import *

class SetElem(Stmt):
    def __init__(self, x, y):
        self.array  = x.array
        self.index  = x.index
        self.expr   = y
    
    def check(self, p1, p2):
        if isinstance(p1, Array) or isinstance(p2, Array): return None
        elif p1 == p2: return p2
        elif Type.numeric(p1) and Type.numeric(p2): return p2
        else: return None

    def gen(self, b, a):
        s1 = self.index.reduce().toString()
        s2 = self.expr.reduce().toString()
        self.emit(f"{self.array.toString()} [{s1}] = {s2}")

