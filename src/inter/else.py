import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from type import *
from stmt import *

class Else(Stmt):
    def __init__(self, x, s1, s2):
        self.expr = x
        self.stmt1 = s1
        self.stmt2 = s2

        if self.expr.type != Types.Bool: self.expr.error("Boolean required in If statement")
    
    def gen(self, b, a):
        label1 = self.newlabel()
        label2 = self.newlabel()
        self.expr.jumping(0, label2)
        self.stmt1.gen(label1, a)
        self.emitlabel(label1)
        self.emit(f"goto L {a}")

        self.emitlabel(label2)
        self.stmt1.gen(label2, a)