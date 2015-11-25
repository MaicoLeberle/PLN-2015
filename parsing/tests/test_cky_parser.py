# https://docs.python.org/3/library/unittest.html
from unittest import TestCase
from math import log2

from nltk.tree import Tree
from nltk.grammar import PCFG

from parsing.cky_parser import CKYParser


class TestCKYParser(TestCase):

    def test_parse(self):
        grammar = PCFG.fromstring(
            """
                S -> NP VP              [1.0]
                NP -> Det Noun          [0.6]
                NP -> Noun Adj          [0.4]
                VP -> Verb NP           [1.0]
                Det -> 'el'             [1.0]
                Noun -> 'gato'          [0.9]
                Noun -> 'pescado'       [0.1]
                Verb -> 'come'          [1.0]
                Adj -> 'crudo'          [1.0]
            """)

        parser = CKYParser(grammar)

        lp, t = parser.parse('el gato come pescado crudo'.split())

        # check chart
        pi = {
            (1, 1): {'Det': log2(1.0)},
            (2, 2): {'Noun': log2(0.9)},
            (3, 3): {'Verb': log2(1.0)},
            (4, 4): {'Noun': log2(0.1)},
            (5, 5): {'Adj': log2(1.0)},

            (1, 2): {'NP': log2(0.6 * 1.0 * 0.9)},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': log2(0.4 * 0.1 * 1.0)},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': log2(1.0) + log2(1.0) + log2(0.4 * 0.1 * 1.0)},

            (1, 4): {},
            (2, 5): {},

            (1, 5): {'S':
                     log2(1.0) +  # rule S -> NP VP
                     log2(0.6 * 1.0 * 0.9) +  # left part
                     log2(1.0) + log2(1.0) + log2(0.4 * 0.1 * 1.0)},  # right part
        }
        self.assertEqualPi(parser._pi, pi)

        # check partial results
        bp = {
            (1, 1): {'Det': Tree.fromstring("(Det el)")},
            (2, 2): {'Noun': Tree.fromstring("(Noun gato)")},
            (3, 3): {'Verb': Tree.fromstring("(Verb come)")},
            (4, 4): {'Noun': Tree.fromstring("(Noun pescado)")},
            (5, 5): {'Adj': Tree.fromstring("(Adj crudo)")},

            (1, 2): {'NP': Tree.fromstring("(NP (Det el) (Noun gato))")},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': Tree.fromstring("(NP (Noun pescado) (Adj crudo))")},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': Tree.fromstring(
                "(VP (Verb come) (NP (Noun pescado) (Adj crudo)))")},

            (1, 4): {},
            (2, 5): {},

            (1, 5): {'S': Tree.fromstring(
                """(S
                    (NP (Det el) (Noun gato))
                    (VP (Verb come) (NP (Noun pescado) (Adj crudo)))
                   )
                """)},
        }
        self.assertEqual(parser._bp, bp)

        # check tree
        t2 = Tree.fromstring(
            """
                (S
                    (NP (Det el) (Noun gato))
                    (VP (Verb come) (NP (Noun pescado) (Adj crudo)))
                )
            """)
        self.assertEqual(t, t2)

        # check log probability
        lp2 = log2(1.0 * 0.6 * 1.0 * 0.9 * 1.0 * 1.0 * 0.4 * 0.1 * 1.0)
        self.assertAlmostEqual(lp, lp2)

    def test_ambiguous_parsing(self):
        grammar = PCFG.fromstring(
            """
                S -> NP VP              [1.0]

                VP -> Verb PPS          [0.4]
                VP -> Verb PP           [0.6]

                Verb -> 'habló'         [1.0]

                PPS -> PP PP            [1.0]

                PP -> Prep NPPP         [0.6]
                PP -> Prep NP           [0.4]

                Prep -> 'a'             [0.8]
                Prep -> 'con'           [0.2]

                NPPP -> NP PP           [1.0]

                NP -> Det Noun          [1.0]

                Det -> 'el'             [0.7]
                Det -> 'la'             [0.3]

                Noun -> 'periodista'    [0.3]
                Noun -> 'persona'       [0.4]
                Noun -> 'micrófono'     [0.3]
            """)

        parser = CKYParser(grammar)

        lp, t = parser.parse('el periodista habló a la persona con el micrófono'.split())
        # Notar que hay dos parsings posibles para esta oración:
        #
        # (S  (NP (Det el) 
        #         (Noun periodista)
        #     )
        #     (VP (Verb habló) 
        #         (PPS    (PP (Prep a) 
        #                     (NP (Det la) 
        #                         (Noun persona)
        #                     )
        #                 ) 
        #                 (PP (Prep con) 
        #                     (NP (Det el) 
        #                         (Noun micrófono)
        #                     )
        #                 )
        #         )
        #     )
        # )
        #
        # o
        #
        # (S  (NP (Det el)
        #         (Noun periodista)
        #     )
        #     (VP (Verb habló)
        #         (PP (Prep a)
        #             (NPPP   (NP (Det la)
        #                         (Noun persona)
        #                     )
        #                     (PP (Prep con)
        #                         (NP (Det el)
        #                             (Noun micrófono)
        #                         )
        #                     )
        #             )
        #         )  
        #     )
        # )

        # Check chart. pi will hold the most probable parsing, along with its 
        # probability.
        pi = {
            (1, 1): {'Det': log2(0.7)},
            (2, 2): {'Noun': log2(0.3)},
            (3, 3): {'Verb': log2(1.0)},
            (4, 4): {'Prep': log2(0.8)},
            (5, 5): {'Det': log2(0.3)},
            (6, 6): {'Noun': log2(0.4)},
            (7, 7): {'Prep': log2(0.2)},
            (8, 8): {'Det': log2(0.3)},
            (9, 9): {'Noun': log2(0.3)},

            (1, 2): {'NP': log2(1.0 * 0.7 * 0.3)},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {},
            (5, 6): {'NP': log2(1.0 * 0.3 * 0.4)},
            (6, 7): {},
            (7, 8): {},
            (8, 9): {'NP': log2(1.0 * 0.3 * 0.3)},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {},
            (4, 6): {'PP': log2(0.4) + log2(0.8) + log2(1.0 * 0.3 * 0.4)},
            (5, 7): {},
            (6, 8): {},
            (7, 9): {'PP': log2(0.4) + log2(0.2) + log2(1.0 * 0.3 * 0.3)},

            (1, 4): {},
            (2, 5): {},
            (3, 6): {},
            (4, 7): {},
            (5, 8): {},
            (6, 9): {},

            (1, 5): {},
            (2, 6): {},
            (3, 7): {},
            (4, 8): {},
            (5, 9): {'NPPP': 
                      log2(1.0) # NPPP -> NP PP [1.0]
                    + (log2(1.0 * 0.3 * 0.4)) # Left part
                    + (log2(0.4) + log2(0.2) + log2(1.0 * 0.3 * 0.3)) # Right part
                    },

            (1, 6): {},
            (2, 7): {}, 
            (3, 8): {},
            (4, 9): { 'PPS': 
                       log2(1.0) # PPS -> PP PP [1.0]
                     + (log2(0.4) + log2(0.8) + log2(1.0 * 0.3 * 0.4)) # Left part
                     + (log2(0.4) + log2(0.2) + log2(1.0 * 0.3 * 0.3)) # Right part
                    , 'PP':
                       log2(0.6) # PP -> Prep NPPP [0.6]
                     + (log2(0.8)) # Left part
                     + (log2(1.0)
                        + (log2(1.0 * 0.3 * 0.4))
                        + (log2(0.4) + log2(0.2) + log2(1.0 * 0.3 * 0.3))) # Right part
                    },

            (1, 7): {},
            (2, 8): {},
            # There are two possible parsings for this interval, both starting 
            # with VP. Hence, the most probable one, VP -> Verb PP, was chosen.
            (3, 9): {'VP':
                      log2(0.6) # VP -> Verb PP [0.6]
                    + log2(1.0) # Left part
                    + (log2(0.6)
                        + (log2(0.8))
                        + (log2(1.0)
                           + (log2(1.0 * 0.3 * 0.4))
                           + (log2(0.4) + log2(0.2) + log2(1.0 * 0.3 * 0.3)))) # Right part
                    },

            (1, 8): {},
            (2, 9): {},

            (1, 9): {'S':
                      log2(1.0) # S -> NP VP [1.0]
                    + log2(1.0 * 0.7 * 0.3) # Left part
                    + (log2(0.6)
                        + log2(1.0)
                        + (log2(0.6)
                            + (log2(0.8))
                            + (log2(1.0)
                               + (log2(1.0 * 0.3 * 0.4))
                               + (log2(0.4) + log2(0.2) + log2(1.0 * 0.3 * 0.3))))) # Right part
                    },
        }
        self.assertEqualPi(parser._pi, pi)

        # Check partial results. bp will hold the most probable parsing for 
        # each interval.
        bp = {
            (1, 1): {'Det': Tree.fromstring("(Det el)")},
            (2, 2): {'Noun': Tree.fromstring("(Noun periodista)")},
            (3, 3): {'Verb': Tree.fromstring("(Verb habló)")},
            (4, 4): {'Prep': Tree.fromstring("(Prep a)")},
            (5, 5): {'Det': Tree.fromstring("(Det la)")},
            (6, 6): {'Noun': Tree.fromstring("(Noun persona)")},
            (7, 7): {'Prep': Tree.fromstring("(Prep con)")},
            (8, 8): {'Det': Tree.fromstring("(Det el)")},
            (9, 9): {'Noun': Tree.fromstring("(Noun micrófono)")},

            (1, 2): {'NP': Tree.fromstring("(NP (Det el) (Noun periodista))")},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {},
            (5, 6): {'NP': Tree.fromstring("(NP (Det la) (Noun persona))")},
            (6, 7): {},
            (7, 8): {},
            (8, 9): {'NP': Tree.fromstring("(NP (Det el) (Noun micrófono))")},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {},
            (4, 6): {'PP': Tree.fromstring("(PP (Prep a) (NP (Det la) (Noun persona)))")},
            (5, 7): {},
            (6, 8): {},
            (7, 9): {'PP': Tree.fromstring("(PP (Prep con) (NP (Det el) (Noun micrófono)))")},

            (1, 4): {},
            (2, 5): {},
            (3, 6): {},
            (4, 7): {},
            (5, 8): {},
            (6, 9): {},

            (1, 5): {},
            (2, 6): {},
            (3, 7): {},
            (4, 8): {},
            (5, 9): {'NPPP': Tree.fromstring("(NPPP (NP  (Det la) (Noun persona)) (PP (Prep con) (NP (Det el) (Noun micrófono))))")},

            (1, 6): {},
            (2, 7): {}, 
            (3, 8): {},
            (4, 9): { 'PPS': Tree.fromstring("(PPS (PP (Prep a) (NP (Det la) (Noun persona) )) (PP (Prep con) (NP (Det el) (Noun micrófono))))")
                    , 'PP': Tree.fromstring("(PP (Prep a) (NPPP (NP (Det la) (Noun persona)) (PP (Prep con) (NP (Det el) (Noun micrófono)))))") 
                    },

            (1, 7): {},
            (2, 8): {},
            # There are two possible parsings for this interval, both starting 
            # with VP. Hence, the most probable one, VP -> Verb PP, was chosen.
            (3, 9): {'VP': Tree.fromstring("(VP (Verb habló) (PP (Prep a) (NPPP (NP (Det la) (Noun persona)) (PP (Prep con) (NP (Det el) (Noun micrófono))))))")},

            (1, 8): {},
            (2, 9): {},

            (1, 9): {'S': Tree.fromstring("(S (NP (Det el) (Noun periodista)) (VP (Verb habló) (PP (Prep a) (NPPP (NP (Det la) (Noun persona)) (PP (Prep con) (NP (Det el) (Noun micrófono)))))))")},
        }
        self.assertEqual(parser._bp, bp)

        # check tree
        t2 = Tree.fromstring(
            """
                (S  (NP (Det el) (Noun periodista))
                    (VP (Verb habló) 
                        (PP (Prep a) 
                            (NPPP   (NP (Det la) 
                                        (Noun persona)
                                    ) 
                                    (PP (Prep con) 
                                        (NP (Det el) 
                                            (Noun micrófono)
                                        )
                                    )
                            )
                        )
                    )
                )
            """)
        self.assertEqual(t, t2)

        # check log probability
        lp2 = log2(1.0 * 1.0 * 0.7 * 0.3 * 0.6 * 1.0 * 0.6 * 0.8 * 1.0 \
                        * 1.0 * 0.3 * 0.4 * 0.4 * 0.2 * 1.0 * 0.3 * 0.3)
        self.assertAlmostEqual(lp, lp2)

    def assertEqualPi(self, pi1, pi2):
        self.assertEqual(set(pi1.keys()), set(pi2.keys()))

        for k in pi1.keys():
            d1, d2 = pi1[k], pi2[k]
            self.assertEqual(d1.keys(), d2.keys(), k)
            for k2 in d1.keys():
                prob1 = d1[k2]
                prob2 = d2[k2]
                self.assertAlmostEqual(prob1, prob2)
