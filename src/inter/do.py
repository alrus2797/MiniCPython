import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from stmt import *
from type import *


class Do(Stmt):
    def __init__(self):
        self.expr = None
        self.stmt = None
    
    def init(self, s, x):
        self.stmt = s
        self.expr = x

        if self.expr.type != Types.Bool: self.expr.error("Boolean required in do")

    def gen(self, b, a):
        self.after = a
        label = self.newlabel()
        self.stmt.gen(b, label)
        self.emitlabel(label)
        self.expr.jumping(b, 0)


