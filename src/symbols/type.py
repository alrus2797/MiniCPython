import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src\lexer')

from word import *
from tag import *

class Type(Word):
    def __init__(self, s, tag, w):
        Word.__init__(self, s, tag)
        self.width = w

    def numeric(self, p):
        if p == Types.Char or p == Types.Int or p == Types.Float: return True
        else: return False
    def max(self, p1, p2):
        if not self.numeric(p1) or not self.numeric(p2): return None
        elif p1 == Types.Float  or p2 == Types.Float: return Types.Float
        elif p1 == Types.Int    or p2 == Types.Int: return Types.Int
        else: return Types.Char
    
    def __eq__(self, other):
        if self.lexeme == other.lexeme and self.tag == other.tag and self.width == other.width:
            return True
        return False
    
    # def toString(self):
    #     return f'[ {self.lexeme}, {self.tag},  {self.width} ]'
class Types:
    Int   = Type( "int",   Tag.BASIC, 4 );
    Float = Type( "float", Tag.BASIC, 8 );
    Char  = Type( "char",  Tag.BASIC, 1 );
    Bool  = Type( "bool",  Tag.BASIC, 1 );

if __name__ == "__main__":
    a = Type('int', Tag.BASIC, 4)
    print(a.numeric(a))


