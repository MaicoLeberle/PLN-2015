# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log

def first_non_extra(ngram):
    res = ""
    for i in range(len(ngram)):
        if ngram[i] != "<s>":
            res = ngram[i]
            break
    return res  

class NGram(object):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self.n = n
        self.counts = counts = defaultdict(int)
        self.word_counts = defaultdict(int)
        self.total_count = 0

        for i in range(len(sents)):
            sents[i] = (['<s>'] * (n - 1)) + sents[i] + (['</s>'] * n)

        for sent in sents:
            for i in range(len(sent) - n + 1):
                self.word_counts[first_non_extra(sent[i:i+n])] += 1
                self.total_count += 1
                ngram = tuple(sent[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.
 
        tokens -- the n-gram or (n-1)-gram tuple.
        """

        return (self.counts[tokens])
 
    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.
 
        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """

        if prev_tokens is None:
            prev_tokens = []

        
        ngram = tuple((['<s>'] * (self.n - 1 - len(prev_tokens))) + prev_tokens + [token])
        
        if float(self.counts[tuple(prev_tokens)]) == 0:
            return 0
        else:
            return (self.counts[ngram] / float(self.counts[tuple(prev_tokens)]))
 
    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.
 
        sent -- the sentence as a list of tokens.
        """


        sent = (['<s>'] * (self.n - 1)) + sent + ['</s>']
        
        res = 1

        for i in range(self.n - 1, len(sent) - self.n + 1):
            res *= self.cond_prob(sent[i], sent[i - self.n  + 1: i])

        return res

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.
 
        sent -- the sentence as a list of tokens.
        """

        sent = (['<s>'] * (self.n - 1)) + sent + ['</s>']
        
        res = 0

        for i in range(self.n - 1, len(sent) - self.n + 1):
            t = self.cond_prob(sent[i], sent[i - self.n  + 1: i])
            if t == 0:
                res = float('-inf')
                break
            res += log(t, 2)


        return res

    def prob(self, token, prev_tokens=None):
        n = self.n
        if not prev_tokens:
            prev_tokens = []
        assert len(prev_tokens) == n - 1

        tokens = prev_tokens + [token]
        return float(self.counts[tuple(tokens)]) / self.counts[tuple(prev_tokens)]
