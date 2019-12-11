from logical import *

class Not(Logical):
    def __init__(self, tok, x2):
        super().__init__(tok, x2, x2)
    
    def jumping (self, t, f):
        self.expr2.jumping(f,t)

    def toString(self):
        return f"{self.op.toString()} {self.expr2.toString()}"