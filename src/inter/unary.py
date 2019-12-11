import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from type import *

from op import *

class Unary(Op):
    def __init__(self, tok, x):
        super().__init__(tok, None)
        self.expr = x
        self.type = Type.max(Types.Int, self.expr.type)
        if self.type == None: self.error("Type error")

    def gen(self):
        return Unary(self.op, self.expr.reduce())
    
    def toString(self):
        return f"{self.op.toString()} {self.expr.toString()}"
