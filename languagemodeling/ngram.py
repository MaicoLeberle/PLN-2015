# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log
from random import uniform

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
        self.probs = defaultdict(int)
        self.sorted_probs = defaultdict(int)
        self.number_token_options = defaultdict(int)

        for i in range(len(sents)):
            sents[i] = (['<s>'] * (n - 1)) + sents[i] + (['</s>'])

        for sent in sents:
            for i in range(len(sent) - n + 1):
                self.word_counts[sent[i+n-1]] += 1
                self.total_count += 1
                ngram = tuple(sent[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1
                
                if not ngram[:-1] in self.probs:
                    self.probs[ngram[:-1]] = defaultdict(int)
                (self.probs[ngram[:-1]])[ngram[len(ngram) - 1]] += 1
                self.number_token_options[ngram[:-1]] += 1

        for key, value in self.probs.items():
            # Turn the number of occurrences into probabilities (that sum to 1,
            # all together) inside each n-gram.
            for k, v in value.items():
                value[k] = v / float(self.number_token_options[key])

        for key, value in self.probs.items():
            # Once self.probs is fully processed, self.sorted_probs is easily
            # obtainable.
            self.sorted_probs[key] = sorted(list(value.items()), key=lambda x: (-x[1], x[0]))

    def get_n(self):
        return self.n

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

class NGramGenerator(object):

    def __init__(self, model):
        """
        model -- n-gram model (NGram object).
        """
        self.model = model
        self.probs = defaultdict(int)
        for key, value in self.model.word_counts.items():
            self.probs[key] = value / float(self.model.total_count)
        self.probs = self.model.probs
        self.sorted_probs = self.model.sorted_probs
        self.n = self.model.get_n()
 
    def generate_sent(self):
        """Randomly generate a sentence."""
        prev_token = ('<s>',) * (self.n - 1)
        assert(prev_token in self.probs.keys())
        sent = []   
        current_token = ''
        while current_token != '</s>':
            current_token = self.generate_token(prev_token)
            if current_token != '</s>':
                sent = sent + [current_token,]
                prev_token = (prev_token + (current_token,))[1 : self.n]
        return sent
 
    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.
 
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        assert(prev_tokens in self.probs.keys())
        x = uniform(0.0, 1.0)
        acc = 0.0
        for k, v in self.probs[prev_tokens].items():
            if acc + v >= x:
                return k
            else:
                acc += v


class AddOneNGram(object):

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
        self.probs = defaultdict(int)
        self.sorted_probs = defaultdict(int)
        self.number_token_options = defaultdict(int)

        for i in range(len(sents)):
            sents[i] = (['<s>'] * (n - 1)) + sents[i] + (['</s>'])

        for sent in sents:
            for i in range(len(sent) - n + 1):
                self.word_counts[sent[i+n-1]] += 1
                self.total_count += 1
                ngram = tuple(sent[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1
                
                if not ngram[:-1] in self.probs:
                    self.probs[ngram[:-1]] = defaultdict(int)
                (self.probs[ngram[:-1]])[ngram[len(ngram) - 1]] += 1
                self.number_token_options[ngram[:-1]] += 1

        for key, value in self.probs.items():
            # Turn the number of occurrences into probabilities (that sum to 1,
            # all together) inside each n-gram.
            for k, v in value.items():
                value[k] = v / float(self.number_token_options[key])

        for key, value in self.probs.items():
            # Once self.probs is fully processed, self.sorted_probs is easily
            # obtainable.
            self.sorted_probs[key] = sorted(list(value.items()), key=lambda x: (-x[1], x[0]))

    def get_n(self):
        return self.n

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.
 
        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self.counts[tokens]

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.
 
        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        if prev_tokens is None:
            prev_tokens = []
        
        ngram = tuple((['<s>'] * (self.n - 1 - len(prev_tokens))) + prev_tokens + [token])
        return (self.count(ngram) + 1) / float(self.count(tuple(prev_tokens)) + self.V())

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

    def V(self):
        ''' Size of the vocabulary. '''
        return (len(self.word_counts))