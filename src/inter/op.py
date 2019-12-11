from expr import *
from temp import *


class Op(Expr):
    def __init__(self, tok, p):
        super().__init__(tok, p)
    
    def reduce(self):
        x = self.gen()
        t = Temp(self.type)
        self.emit(f"{t.toString()} = {x.toString()}")
        return t
