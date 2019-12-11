from expr import *

class Id(Expr):
    def __init__(self, id, p, b):
        super().__init__(id, p)
        self.offset = b