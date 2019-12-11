from stmt import *

class Seq(Stmt):
    def __init__(self, s1, s2):
        self.stmt1 = s1
        self.stmt2 = s2
    
    def gen(self, b, a):
        if self.stmt1 == Stmt.Null: self.stmt2.gen(b, a)
        elif self.stm2 == Stmt.Null: self.stmt1.gen(b, a)
        else:
            label = self.newlabel()
            self.stmt1.gen(b, label)
            self.emitlabel(label)
            self.stmt2.gen(label, a)