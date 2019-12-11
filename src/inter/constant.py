import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src')

from lexer.token import * 
from symbols.type import *
from lexer.word import *

from expr import *

class Constant(Expr):
    def __init__(self, tok, p = -1):
        if isinstance(tok, Token):
            super().__init__(tok, p)
        elif isinstance(tok, int):
            super().__init__(Num(tok), Types.Int)

    def jumping(self, t, f):
        if self == BoolConstant._True and t != 0: self.emit(f"got L {t}")
        elif self == BoolConstant._False and f != 0: self.emit(f"got L {f}")

class BoolConstant:
    _True   = Constant(Words._True, Types.Bool)
    _False  = Constant(Words._False, Types.Bool)
