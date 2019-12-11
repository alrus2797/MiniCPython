from node import *

class NullStmt(Node):
    pass

class Stmt(Node):
    after   = 0
    Null    = 0
    Enclosing = Null
    def __init__(self):
        # self.n = Stmt()
        pass

    def gen(self, b, a):
        pass

Stmt.Null = Stmt()
Stmt.Enclosing = Stmt.Null