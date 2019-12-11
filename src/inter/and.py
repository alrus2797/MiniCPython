from logical import *

class And(Logical):
    def __init__(self, tok, x1, x2):
        super().__init__(tok, x1, x2)
    
    def jumping(self, t, f):
        label = f if f != 0 else self.newlabel()
        self.expr1.jumping(0, label)
        self.expr2.jumping(t,f)
        if f == 0: self.emitlabel(label)