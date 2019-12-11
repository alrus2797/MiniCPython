from token import *
from tag import *
class Word(Token):
	def __init__(self, s, tag):
		Token.__init__(self, tag)
		self.lexeme = s
	
	def toString(self):
		return self.lexeme

class Words(Token):
	_and    = Word( "&&", Tag.AND );  _or   = Word( "||", Tag.OR );
	eq      = Word( "==", Tag.EQ  );  ne    = Word( "!=", Tag.NE );
	le      = Word( "<=", Tag.LE  );  ge    = Word( ">=", Tag.GE );

	minus  = Word( "minus", Tag.MINUS );
	_True  = Word( "true",  Tag.TRUE  );
	_False = Word( "false", Tag.FALSE );
	temp   = Word( "t",     Tag.TEMP  );
