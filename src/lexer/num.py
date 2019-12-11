from token import *
from tag import *


class Num(Token):
    def __init__(self, v):
        Token.__init__(self, Tag.NUM)
        self.value = v
    def toString(self):
        return str(self.value)
    