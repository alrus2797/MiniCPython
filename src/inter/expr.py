import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\lexer')

from node import *
from num import * 
from real import * 
from word import *
from token import *


class Expr(Node):
    def __init__(self, tok, p):
        if type(tok) not in [Num, Real, Word, Words, Token]:
            raise Exception(f"Argument Tok is {type(tok)}, expected {['Num','Real','Word', 'Words','Token']}")
        
        self.op     = tok
        self.type   = p
    
    def gen(self):
        return self
    
    def reduce(self):
        return self
    
    def jumping(self, t, f):
        self.emitjumps(self.toString(), t, f)

    def emitjumps(self, test, t, f):
        if t != 0 and f != 0:
            self.emit(f"if {test} got L {t}")
            self.emit(f"goto L {f}")
        elif t != 0:
            self.emit(f"if {test} goto L {t}")
        elif f != 0:
            self.emit(f"iffalse {test} goto L {f}")
    
    def toString(self):
        return self.op.toString()