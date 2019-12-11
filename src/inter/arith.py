from op import *

import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from type import *





class Arith(Op):
    def __init__(self, tok, x1, x2):
        super().__init__(tok, None)
        self.expr1 = x1
        self.expr2 = x2

        self.type = Types.max(self.expr1.type, self.expr2.type)
        if type == None: self.error("Type error")

    def gen(self):
        return Arith(self.op, self.expr1.reduce(), self.expr2.reduce())
    
    def toString(self):
        return f"{self.expr1.toString()} {self.op.toString()} {self.expr2.toString()}"