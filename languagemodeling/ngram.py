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
        self.counts = defaultdict(int)
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
                self.counts[ngram] += 1
                self.counts[ngram[:-1]] += 1
                
                if not ngram[:-1] in self.probs.keys():
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
        return (self.n)

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

        if self.count(ngram) == 0:
            # Result will be 0, even if self.count(tuple(prev_tokens)) == 0 
            # (in which case this call to cond_prob should be undefined).
            return (0)
        else:
            # If self.count(ngram) != 0, then 
            #    self.count(tuple(prev_tokens)) != 0.
            return ((self.count(ngram) / float(self.count(tuple(prev_tokens)))))
 
    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.
 
        sent -- the sentence as a list of tokens.
        """
        sent = (['<s>'] * (self.n - 1)) + sent + ['</s>']
        
        res = 1

        for i in range(self.n - 1, len(sent) - self.n + 1):
            res *= self.cond_prob(sent[i], sent[i - self.n  + 1: i])

        return (res)

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

        return (res)


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
        return (sent)
 
    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.
 
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        assert(prev_tokens in self.probs.keys())
        x = uniform(0.0, 1.0)
        acc = 0.0
        for k, v in self.probs[prev_tokens].items():
            if acc + v >= x:
                return (k)
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
        self.counts = defaultdict(int)
        self.word_counts = defaultdict(int)
        self.total_count = 0

        for i in range(len(sents)):
            sents[i] = (['<s>'] * (n - 1)) + sents[i] + (['</s>'])

        for sent in sents:
            for i in range(len(sent) - n + 1):
                self.word_counts[sent[i+n-1]] += 1
                self.total_count += 1
                ngram = tuple(sent[i: i + n])
                self.counts[ngram] += 1
                self.counts[ngram[:-1]] += 1
                
    def get_n(self):
        return (self.n)

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
        return ((self.count(ngram) + 1) / float(self.count(tuple(prev_tokens)) + self.V()))

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.
 
        sent -- the sentence as a list of tokens.
        """
        sent = (['<s>'] * (self.n - 1)) + sent + ['</s>']
        
        res = 1

        for i in range(self.n - 1, len(sent) - self.n + 1):
            res *= self.cond_prob(sent[i], sent[i - self.n  + 1: i])

        return (res)

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

        return (res)

    def V(self):
        """ Size of the vocabulary. """
        return (len(self.word_counts))


class InterpolatedNGram:
    # Add-one para p_ML(w) (en el nivel mas bajo: unigramas) sii addone == True (independientemente del n).
    # held-out data == development data
    # si cond_prob devuelve (0 / 0) -> en NGram no importa
    #                               -> en AddOne no pasa
    #                               -> en Interpolated si pasa e importa. Pero el coeficiente lambda correspondiente será 0 en este caso, por lo que hay que implementar un if ahi para que no se rompa.
    # el valor de gamma se calcula con el 10% del parámetro sents del __init__. Probar distintos gammas hasta encontrar el rango sobre el que se maximizan los distintos valores de gamma, y de ahí hacer barrido para elegir especificamente el valor óptimo.
    # TODO: registrar unigramas, bigramas, ..., n-gramas en self.counts
    def __init__(self, n, sents, gamma=None, addone=True):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        gamma -- interpolation hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        assert n > 0
        self.n = n

        if (gamma is None):
            # Training is performed with 90% of sents, and last 10% of the 
            # corpus is reserved as held-out data for estimating gamma.
            training = sents[:int(len(sents) * 0.9)]
        else:
            # If gamma is already provided, use sents as training set. No need
            # for held-out data.
            training = sents
            self.gamma = gamma

        self.addone = addone
        if (addone):
            # The lowest level n-gram (unigram) should implement add-one 
            # smoothing.
            self.unigram_model = AddOneNGram(1, training)
        else:
            self.unigram_model = NGram(1, training)

        self.counts = defaultdict(int)
        self.word_counts = defaultdict(int)
        self.total_count = 0
        self.number_token_options = defaultdict(int)

        for i in range(len(training)):
            # print("pre_training[i]: " + str(training[i]))
            if training[i][-1] != '</s>':
                training[i] = training[i] + ['</s>']
            training[i] = (['<s>'] * (n - 1)) + training[i]
            # print("training[i]" + str(training[i]))

        for sent in training:
            for i in range(len(sent) - n + 1):
                self.word_counts[sent[i+n-1]] += 1
                self.total_count += 1
                ngram = tuple(sent[i: i + n])
                for j in range(len(ngram)):
                    # print("J: " + str(j))
                    # print("NGRAM[J:]: " + str(ngram[j:]))
                    # Note that len(ngram) = n.
                    # Thus, every n-gram, (n-1)-gram, ...
                    #   , (n-(n-2))-gram = 2-gram is registered in self.counts.
                    # The registrations of 1-grams and the 0-gram are done
                    # in self.unigram_model (be it with add-one smoothing or 
                    # not).
                    self.counts[ngram[j:]] += 1

        if (gamma is None):
            # Computing of gamma parameter from held-out data is now 
            # realizable, since only now self.counts is available in its 
            # wholeness.
            held_out = sents[int(len(sents) * 0.9):]   
            for i in range(len(held_out)):
                held_out[i] = (['<s>'] * (n-1)) + held_out[i] + (['</s>'])
            
            # Prepare c' information (number of ocurrences of each n-gram in 
            # the development set).         
            self.counts_prime = defaultdict(int)
            for sent in held_out:
                for i in range(len(sent) - n + 1):
                    ngram = tuple(sent[i: i + n])
                    self.counts_prime[ngram] += 1
            self.gamma = self.__compute_gamma(held_out)
        # print(str(self.gamma))

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.
 
        tokens -- the n-gram or (n-1)-gram tuple.
        """
        if (len(tokens) < 2):
            return self.unigram_model.count(tokens=tuple(tokens))
        else:
            return (self.counts[tuple(tokens)])

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.
 
        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        if prev_tokens is None:
            prev_tokens = []
        assert(len(prev_tokens) == self.n - 1)

        skip_next = False
        acc_lambdas = 0.0
        res = 0.0

        for i in range(0, self.n - 1):
            current_lambda = self.__get_lambda(tokens=prev_tokens, i=i, 
                                   gamma=self.gamma, prev_lambdas=1 - acc_lambdas)

            if (current_lambda != 0):
                if (i == 0):
                    res += current_lambda * self.__max_likelyhood_prob(token=token, 
                                prev_tokens=prev_tokens[:len(prev_tokens) - i])
                else:
                    res += (1 - acc_lambdas) * self.__max_likelyhood_prob(token=token, 
                                prev_tokens=prev_tokens[:len(prev_tokens) - i])
            acc_lambdas += current_lambda
        # Finally, the MLE for the unigram case needs to be incorporated in the
        # final result.
        res += (1 - acc_lambdas) * self.unigram_model.cond_prob(token=token)
        return (res)

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.
 
        sent -- the sentence as a list of tokens.
        """
        sent = (['<s>'] * (self.n - 1)) + sent + ['</s>']
        res = 1

        for i in range(self.n - 1, len(sent) - self.n + 1):
            res *= self.cond_prob(sent[i], sent[i - self.n  + 1: i])

        return (res)

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

        return (res)

    def V(self):
        ''' Size of the vocabulary. '''
        return (len(self.word_counts))

    def get_n(self):
        return (self.n)

    def __compute_gamma(self, devel_set):
        """ Compute gamma parameter for the model with the development set 
            (a.k.a. held-out data).
        """
        gammas = list(range(1, 10001, 500))
        best_gamma = gammas[0]
        best_result = self.__compute_log_likelihood(gamma=gammas[0])
        for g in gammas:
            current_result = self.__compute_log_likelihood(gamma=g)
            if current_result > best_result:
                best_result = current_result
                best_gamma = g
        return (best_gamma)

    def __compute_log_likelihood(self, gamma):
        """ Change self.gamma and compute log-likelihood.
            Restor self.gamma to its previous value, and return the 
            log-likelihood value obtained.
        """
        self.gamma = gamma
        log_likelihood = 0.0

        for key, value in self.counts_prime.items():
            log_likelihood += value * log (self.cond_prob(token=key[-1], prev_tokens=key[:-1]))

        return (log_likelihood)

    def __max_likelyhood_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token, corresponding to the maximum 
            likelyhood estimator used in the previous classes. 
        """
        if prev_tokens is None or len(prev_tokens) == 0:
            prev_tokens = []
        ngram = tuple((['<s>'] * (self.n - 1 - len(prev_tokens))) + list(prev_tokens) + [token])

        if (len(ngram) == 1):
            return self.unigram_model.cond_prob(token=token, prev_tokens=prev_tokens)
        else:
            # len(ngram) will never be 0, since len([token]) > 0.
            assert(len(ngram) > 1)
            return (self.count(ngram) / float(self.count(tuple(prev_tokens))))

    def __get_lambda(self, tokens, i, gamma, prev_lambdas=1):
        """ Compute i-th lambda value from an (n-1)-gram (tokens), gamma and 
            (1 - (1st lambda) - ... - ((i-2)-th lambda) - ((i-1)-th lambda)).
        """
        uple = tuple(tokens[:len(tokens) - i])
        if (len(uple) == 0):
            return (prev_lambdas)
        else:
            return (prev_lambdas * self.count(uple) / float(self.count(uple) + gamma))
