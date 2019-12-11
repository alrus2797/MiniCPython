from token import *
from tag import *

class Real(Token):
    def __init__(self, v):
        Token.__init__(self, Tag.REAL)
        self.value = v
    def toString(self):
        return str(self.value)