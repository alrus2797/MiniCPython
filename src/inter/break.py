from stmt import *

class Break(Stmt):
    def __init__(self):
        if Stmt.Enclosing == Stmt.Null: self.error("Unenclosed break")
        self.stmt = Stmt.Enclosing
    
    def gen(self, b, a):
        self.emit(f"goto L {self.stmt.after}")