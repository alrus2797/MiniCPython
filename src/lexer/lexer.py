import sys
sys.path.insert(0, 'C:\PerPer\Mini-C\src')

from symbols.type import *
from word import *
from token import *
from num import *

from readchar import readchar

class Lexer:
	line   = 1
	def __init__(self):
		self.peek   = ' '
		self.words  = {
			'if'	: Word('if', Tag.IF),
			'else'	: Word('else', Tag.ELSE),
			'while'	: Word('while', Tag.WHILE),
			'do'	: Word('do', Tag.DO),
			'break'	: Word('break', Tag.BREAK),
		}

		self.reserve( Words._True);
		self.reserve( Types.Int);
		self.reserve( Types.Bool);

		self.reserve( Words._False );
		self.reserve( Types.Char  );
		self.reserve( Types.Float );
	
	def reserve(self, w):
		if type(w) not in [Type, Word, Words, Types]:
			raise Exception("Argument is not a Type class")
		self.words[w.lexeme] = w
	
	def readch(self):
		# self.peek = readchar().decode('UTF-8')
		self.peek	= sys.stdin.read(1)
		# self.peek = input()
	
	def readch_and_compare(self, c):
		self.readch()
		if self.peek != c: return False
		peek = ' '
		return True

	def scan(self):
		while True:
			self.readch()
			# print("hi:", self.peek)
			if self.peek == ' ' or self.peek == '\t': continue
			elif self.peek == '\n': self.line = self.line + 1
			else: break
		
		if self.peek == '&':
			if self.readch_and_compare('&'): return Words._and
			else: return Token('&')
		if self.peek == '|':
			if self.readch_and_compare('|'): return Words._or
			else: return Token('|')
		if self.peek == '=':
			if self.readch_and_compare('='): return Words.eq
			else: return Token('=')
		if self.peek == '!':
			if self.readch_and_compare('='): return Words.ne
			else: return Token('!')
		if self.peek == '<':
			if self.readch_and_compare('='): return Words.le
			else: return Token('&')
		if self.peek == '>':
			if self.readch_and_compare('='): return Words.ge
			else: return Token('&')

		if self.peek.isdigit():
			v = 0
			while self.peek.isdigit():
				v = 10 * v + int(self.peek)
				self.readch()
			if self.peek != '.': return Num(v)
			x = v
			d = 10
			while True:
				self.readch()
				if not self.peek.isdigit(): break
				x = x + int(self.peek) / d
				d = d * 10
			return Real(x)
		
		if self.peek.isalpha():
			buffer = ""
			while self.peek.isalpha():
				buffer += self.peek
				self.readch()
			
			w = self.words.get(buffer)
			if w:
				return w
			w = Word(buffer, Tag.ID)
			self.words[buffer] = w
			return w
		
		tok = Token(self.peek)
		self.peek = ' '
		return tok


		
if __name__ == "__main__":
	lex = Lexer()
	a = lex.scan().toString()
	while a != '':
		print("Final: ", a)
		a = lex.scan().toString()
