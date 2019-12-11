import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from stmt import *
from type import *

class If(Stmt):
    def __init__(self, x, s):
        self.expr = x
        self.stmt = s

        if self.expr.type != Types.Bool: self.expr.error("Boolean required in if")
    
    def gen(self, b, a):
        label = self.newlabel()
        self.expr.jumping(0,a)
        self.emitlabel(label)
        self.stmt.gen(label, a)