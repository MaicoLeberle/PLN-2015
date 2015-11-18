from nltk.tree import Tree
from collections import defaultdict

class CKYParser:
 
	def __init__(self, grammar):
		"""
		grammar -- a binarised NLTK PCFG.
		"""
		# grammar is a binarised nltk.grammar.PCFG object, and needs not be 
		# accessed publicly. Among its methods, start() and productions().
		assert(grammar.is_binarised())
		self.__grammar = grammar

		# According to the tests in parsing/tests/test_cky_parser.py, a 
		# CKYParser object must have a _pi and a _bp attributes.
		#
		# _pi will consist of a dictionary with intervals as keys, and 
		# dictionaries with pairs (non-terminal, probability) as values.
		#
		# _bp will consist of a dictionary with intervals as keys, and 
		# dictionaries with pairs (non-terminal, nltk.tree.Tree) as values.s
		self._pi = dict()
		self._bp = dict()

		# self.__productions is a dictionary whose keys are terminals or 
		# pairs of the form (non-terminal, non-terminal), and whose values 
		# are lists of pairs of the form (non-terminal, log probability), 
		# such that each element in the list is the left-hand side of a 
		# production , and the key to which the list is associated with is the 
		# right-hand side of such production.
		self.__productions = defaultdict(defaultdict)
		for p in grammar.productions():
			# Each element in grammar.productions is a 
			# nltk.grammar.ProbabilisticProduction object, and hence has 
			# methods lhs (which returns the left-hand side non-terminal of the
			#  production) and rhs (which returns the right-hand terminals and 
			# non-terminals of the production). lhs and rhs (if it's a 
			# non-terminal) have a method symbol, which consists of the 
			# non-terminal representation.
			lhs, rhs = p.lhs(), p.rhs()
			if (len(rhs) > 1):
				assert(len(rhs) == 2)
				# Since grammar is binarised, we know that having an rhs of 
				# length greater than 1 means it is made of 2 non-terminals.
				rhs = rhs[0].symbol(), rhs[1].symbol()
			lhs = lhs.symbol()
			self.__productions[rhs][lhs] =  p.logprob()

 
	def parse(self, sent):
		"""Parse a sequence of terminals.
 
		sent -- the sequence of terminals.
		"""
		n = len(sent)

		# First, register a dictionary for every possible interval in sent. 
		# This is performed for later registration of probabilities and 
		# subtrees associated with productions.
		for i in range(1, n + 1):
			for j in range(i, n + 1):
				self._pi[(i,j)] = dict()
				self._bp[(i,j)] = dict()

		# Next, the CKY algorithm per se.
		# Base case of CKY algorithm.
		for i in range(1, n + 1):
			for (nterm, logprob) in self.__productions[(sent[i - 1],)].items():
				# For every word in sent (more precisely, for every interval 
				# of length 1), register a dictionary consisting of 
				# non-terminals (as keys) that derive in such word, and the 
				# probabilities for such a derivation (as values). 
				self._pi[(i, i)][nterm] = logprob
				# Also, register the subtree related to such non-terminal and 
				# word.
				self._bp[(i, i)][nterm] = Tree(nterm, [sent[i - 1]])
		# Recursive case.
		for l in range(1, n):
			# l determines the length of the interval. It is not 0 because
			# intervals that consist of a single word have already been
			# considered in the base case.
			for i in range(1, (n + 1) - l):
				# i is the left-hand end of the range, and j is the right-hand
				# end of the range.
				j = i + l
				for s in range(i, j):
					# s is the breaking point of the subsentence of length l 
					# that is being considered.
					for Y in self._pi[(i, s)].keys():
						# Y is the maximum probability non-terminal that parses
						#  correctly the substring sent[i]...sent[s]
						for Z in self._pi[(s + 1, j)].keys():
							# Z is the maximum probability non-terminal that
							# parses correctly the substring sent[s+1]...sent[j]
							for nterm in self.__productions[(Y, Z)].keys():
								# nterm is the non-terminal such that there is 
								# a production of the form (nterm -> Y Z).
								pos_max = (self.__productions[(Y, Z)][nterm]) \
									+ self._pi[(i, s)][Y] \
									+ self._pi[(s + 1, j)][Z]
								# Update (or inser for the first time) maximum
								#  probability parsing, and the tree related to 
								# it, for parsing from nterm.
								if (not nterm in self._pi[(i, j)].keys() 
									or pos_max > self._pi[(i, j)][nterm]):
										self._pi[(i, j)][nterm] = pos_max
										aux = Tree(nterm
											,[self._bp[(i, s)][Y]
											, self._bp[(s + 1, j)][Z]])
										self._bp[(i, j)][nterm] = aux

		s = self.__grammar.start().symbol()
		if (s in self._pi[(1, n)].keys()):
			# A parsing starting from s was found; return its probability
			# and the parsing itself.
			return ((self._pi[(1, n)][s], self._bp[1, n][s]))
		else:
			# If no parsing starting from s was found, return the minimum 
			# possible log probability, and None as the parsing.
			return ((float('-inf'), None))