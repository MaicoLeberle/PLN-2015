# parsed_sents parameter in UPCFG.__init__ is a list of nltk.tree.Trees.
from nltk.tree import Tree

# The following is going to be the 'root' of the PCFG we intend to create out 
# of the list of training trees provided to UPCFG.__init__(namely, 
# parsed_sents).
from nltk.grammar import Nonterminal

# This will be useful for creating a PCFG grammar out of a starting symbol and
# a list of productions.
from nltk.grammar import induce_pcfg

# This functions implement the unlexicalization and the relexicalization with 
# the POS tag, as requested in the exercise statement.
from parsing.util import lexicalize, unlexicalize

# Use CKYParser implemented in exercise 2 as the parser contained within UPCFG.
from parsing.cky_parser import CKYParser

# Apparently, from the tests (specifically, test_parse_no_parse_returns_flat),
# a parsing from a Flat parser should be returned if no parsing was returned 
# from the CKYParser.
from parsing.baselines import Flat

class UPCFG:
    """Unlexicalized PCFG.
    """
 
    def __init__(self, parsed_sents, start='sentence'):
        """
        parsed_sents -- list of training trees.
        """
        self.__start = Nonterminal(symbol=start)
        productions = list()
        for tree in parsed_sents:
            # First, unlexicalize the tree (i.e., replace the words in the 
            # leaves with the non-terminals that derive into them).
            temp_tree = unlexicalize(tree.copy(deep=True))
            # Second, make sure the tree is in CNF. This is because CKYParser 
            # only performs on binarised NLTK PCFGs.
            temp_tree.chomsky_normal_form()
            # chomsky_normal_form only binarises and unarises a tree. We also
            # need to eliminate unary productions, due to the way 
            # CKYParser.parse is implemented (CKYParser._pi.keys() is a list of
            # pairs).
            # "Unlexicalize completely the PCFG: in the rules, replace every
            # lexical element with its POS tag". This means that collapsePOS is
            #  True.
            temp_tree.collapse_unary(collapsePOS=True)
            # Finally, add temp_tree's productions to the list of productions 
            # that will be used for induce a PCFG later.
            productions += temp_tree.productions()
        # Now create the unlexicalized PCFG needed. Use start parameter as the 
        # starting symbol, and __productions as the list of productions from 
        # which to induce the PCFG.
        self.__pcfg = induce_pcfg(start=Nonterminal(symbol=start), 
                                    productions=productions)
        self.__parser = CKYParser(grammar=self.__pcfg)

    def productions(self):
        """Returns the list of UPCFG probabilistic productions.
        """
        return (self.__pcfg.productions())
 
    def parse(self, tagged_sent):
        """Parse a tagged sentence.
 
        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        # First, split tagged_sent into the list of words and the list of tags.
        words, tags = zip(*tagged_sent)
        
        # "The parser must also ignore the lexical elements and use the POS 
        # tags sentence to parse".
        prob, tagging = self.__parser.parse(tags)

        if (tagging is None):
            # No parsing was found; return the parsing that a flat tree 
            # returns (i.e., self.__start derives to every POS tag in 
            # tagged_sentence, and those tags derive into their corresponding 
            # words in the sentence).
            return (Flat(parsed_sents=None,
                             start=self.__start).parse(tagged_sent))
        else:
            # A parsing was found. Return such parsing, lexicalizing it with 
            # the words in the sentence (i.e., replacing every leaf, in the 
            # tree resulting from the parsing, with the corresponding word
            # in the sentence).
            tree = lexicalize(tagging, words)
            # Note, from the returning of a Flat parser parsing, that the 
            # result of the parsing returned should be in its unbinarised form.
            tree.un_chomsky_normal_form()
            return (tree)