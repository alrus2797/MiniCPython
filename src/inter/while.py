import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\symbols')

from stmt import *

from type import *

class While(Stmt):
    def __init__(self):
        self.expr = None
        self.expr = None
    
    def init(self, x, s):
        self.expr = x
        self.stmt = s

        if self.expr.type != Types.Bool: self.expr.error("Boolean required in while")
    
    def gen(self, b, a):
        self.after = a
        self.expr.jumping(0, a)
        
        label = self.newlabel()

        self.emitlabel(label)
        self.stmt.gen(label, b)
        self.emit(f"goto L {b}")
