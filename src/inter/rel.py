import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from type import *
from array import *
from logical import *

class Rel(Logical):
    def __init__(self, tok, x1, x2):
        super().__init__(tok, x1, x2)
    
    def check(self, p1, p2):
        if isinstance(p1, Array) or isinstance(p2, Array): return None
        elif p1 == p2: return Types.Bool
        else: return None
    
    def jumping(self, t, f):
        a = self.expr1.reduce()
        b = self.expr2.reduce()

        test = f"{a.toString()} {self.op.toString()} {b.toString()}"
        
        self.emitjumps(test, t, f)
