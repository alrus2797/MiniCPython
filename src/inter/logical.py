import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from type import *
from temp import *


class Logical(Expr):
    def __init__(self, tok, x1, x2):
        super().__init__(tok, None)
        self.expr1  = x1
        self.expr2  = x2
        self.type   = self.check(expr1.type, expr2.type)

    def check(self, p1, p2):
        if p1 == Type.Bool and p2 == Type.Bool: return Type.Bool
        return None
    
    def gen(self):
        f = self.new_label()
        a = self.new_label()

        temp = Temp(self.type)
        self.jumping(0, f)
        self.emit(f"{temp.toString()} = true")
        self.emit(f"goto L {a}")
        self.emit(f)
        self.emit(f"{temp.toString()} = false")
        self.emit(a)
        return temp
    
    def toString(self):
        return f"{self.expr1.toString()} {self.op.toString()} {self.expr2.toString()}"

