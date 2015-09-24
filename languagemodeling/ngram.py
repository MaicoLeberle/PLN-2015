# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log
from random import uniform

class EvaluatingClass(object):
    def __init__(self):
        pass

    def log_probability(self, test_set):
        """ Log-probability of the model on a test set.

            test_set -- the test corpus.
        """
        res = 0.0
        for sent in test_set:
            res += self.sent_log_prob(sent)
        return res

    def cross_entropy(self, test_set):
        """ Cross-entropy of the model on a test set.

            test_set -- the test corpus.
        """
        M = 0.0
        for s in test_set:
            M += len(s)
         
        return (self.log_probability(test_set) / -M)

    def perplexity(self, test_set):
        """ Perplexity of the model on a test set.

            test_set -- the test corpus.
        """
        return (pow(2, self.cross_entropy(test_set)))

class NGram(EvaluatingClass):

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

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.
 
        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return (self.counts[tuple(tokens)])
 
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
        """ Probability of a sentence. Warning: subject to underflow problems.
 
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
        self.n = self.model.n
 
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


class AddOneNGram(EvaluatingClass):

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
        """ Probability of a sentence. Warning: subject to underflow problems.
 
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
 


class InterpolatedNGram (EvaluatingClass):

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
            # Training is performed with 90% of sents, last 10% of the 
            # corpus is reserved as held-out data for estimating gamma.
            training = sents[:int(len(sents) * 0.9)]
        else:
            # If gamma is already provided, use the whole of sents as training 
            # set (no need for held-out data).
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
            if training[i][-1] != '</s>':
                training[i] = training[i] + ['</s>']
            training[i] = (['<s>'] * (n - 1)) + training[i]

        for sent in training:
            for i in range(len(sent) - n + 1):
                self.word_counts[sent[i+n-1]] += 1
                self.total_count += 1
                ngram = tuple(sent[i: i + n])
                for j in range(len(ngram)):
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
            # Held-out data is from 80% to 90% of the training corpus.
            held_out = sents[int(len(sents) * 0.9):]
            for i in range(len(held_out)):
                held_out[i] = (['<s>'] * (n-1)) + held_out[i] + (['</s>'])
            
            # Prepare c' information: number of ocurrences of each n-gram in 
            # the development set (i.e., held-out data).         
            self.counts_prime = defaultdict(int)
            for sent in held_out:
                for i in range(len(sent) - n + 1):
                    ngram = tuple(sent[i: i + n])
                    self.counts_prime[ngram] += 1
            self.__compute_gamma(held_out)

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
        if (self.n == 1):
            return self.unigram_model.cond_prob(token=token)

        if prev_tokens is None:
            prev_tokens = []
        assert(len(prev_tokens) == self.n - 1)

        acc_lambdas = []
        res = 0.0

        # For every i, add the i-th term in the interpolation formula, by 
        # computing the lambda coefficient and the maximum likelihood 
        # estimator for each term.
        for i in range(1, self.n + 1):    
            current_lambda = self.__get_lambda(tokens=prev_tokens[(i-1):], 
                                           prev_lambdas = 1 - sum(acc_lambdas))
            try:
                res +=  current_lambda * self.__max_likelihood_prob(
                      token=token, prev_tokens=prev_tokens[(i-1):])
            except ZeroDivisionError:
                # Do not add this term.
                pass
            acc_lambdas += [current_lambda] 
        return (res)

    def __max_likelihood_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token, corresponding to the maximum 
            likelihood estimator used in the previous classes. 
        """

        if prev_tokens is None or len(prev_tokens) == 0:
            prev_tokens = []
        ngram = tuple(list(prev_tokens) + [token])

        if (len(ngram) == 1):
            return self.unigram_model.cond_prob(token=token, prev_tokens=prev_tokens)
        else:
            # len(ngram) will never be 0, since len([token]) > 0.
            assert(len(ngram) > 1)
            return (self.count(ngram) / float(self.count(tuple(prev_tokens))))

    def __get_lambda(self, tokens, prev_lambdas=1):
        """ Compute i-th lambda value from an (n-1)-gram (tokens), gamma and 
            (1 - (1st lambda) - ... - ((i-2)-th lambda) - ((i-1)-th lambda)).
        """
        tokens = tuple(tokens)

        if (len(tokens) == self.n - 1):
            # First lambda coefficient
            return (self.count(tokens) / float(self.count(tokens) + self.gamma))
        elif (len(tokens) == 0):
            # Last lambda coefficient
            return (prev_lambdas)
        else:
            return (prev_lambdas * self.count(tokens) / float(self.count(tokens) + self.gamma))

    def sent_prob(self, sent):
        """ Probability of a sentence. Warning: subject to underflow problems.
 
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

    def __compute_gamma(self, devel_set):
        """ Compute gamma parameter for the model with the development set 
            (a.k.a. held-out data).
        """
        self.gamma = best_gamma = 1
        best_result = self.__compute_log_likelihood()

        for g in list(range(1, 1000, 50)):
            self.gamma = g
            current_result = self.__compute_log_likelihood()
            if current_result > best_result:
                best_result = current_result
                best_gamma = g

        self.gamma = best_gamma

    def __compute_log_likelihood(self):
        """ Change self.gamma and compute log-likelihood.
            Restor self.gamma to its previous value, and return the 
            log-likelihood value obtained.
        """
        log_likelihood = 0.0

        for key, value in self.counts_prime.items():
            log_likelihood += value * log (self.cond_prob(token=key[-1], prev_tokens=key[:-1]))

        return (log_likelihood)



class BackOffNGram(EvaluatingClass):

    def __init__(self, n, sents, beta=None, addone=True):
        """ Back-off NGram model with discounting as described by Michael Collins.
     
            n -- order of the model.
            sents -- list of sentences, each one being a list of tokens.
            beta -- discounting hyper-parameter (if not given, estimate using
                held-out data).
            addone -- whether to use addone smoothing (default: True).
        """
        assert n > 0
        self.n = n

        if (beta is None):
            # Training is performed with 90% of sents, and last 10% of the 
            # corpus is reserved as held-out data for estimating beta.
            training = list(sents[:int(len(sents) * 0.9)])
        else:
            # If beta is already provided, use sents as training set. No need
            # for held-out data.
            training = list(sents)
            self.beta = beta

        self.addone = addone
        if (addone):
            # The lowest level n-gram (unigram) should implement add-one 
            # smoothing.
            self.unigram_model = AddOneNGram(1, training)
        else:
            self.unigram_model = NGram(1, training)

        self.counts = defaultdict(int)
        self.total_count = 0
        self.number_token_options = defaultdict(int)

        for i in range(len(training)):
            if training[i][-1] != '</s>':
                training[i] = training[i] + ['</s>']
            training[i] = (['<s>'] * (n - 1)) + training[i]

        for sent in training:
            for i in range(len(sent) - n + 1):
                self.total_count += 1
                ngram = tuple(sent[i: i + n])
                for j in range(len(ngram) + 1):
                    self.counts[ngram[:j]] += 1
            # Remaining computations related to the last ngram, in reverse 
            # order.
            ngram = tuple(sent[len(sent) - n:])
            for j in range(1, len(ngram)):
                self.counts[ngram[j:]] += 1

        self.__clear_memo()

        if (beta is None):
            # Computing of beta parameter from held-out data is now 
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

            # After this, self.beta will be set to the value in 
            # [0.1, ..., 0.9, 1.0] that maximizes the log-likelihood of the 
            # development corpus.
            self.__compute_beta(held_out)

    def count(self, tokens):
        """ Count for a k-gram with 0 <= k < n.
 
            tokens -- the k-gram tuple.
        """
        return (self.counts[tuple(tokens)])

    def cond_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token, given its context, and using 
            Back-off with discounting.

            token -- the token.
            prev_tokens -- the previous k tokens, with 0 <= k < n.
        """
        # Since memoization is implemented in this class, proceed with 
        # computation only if this same prev_tokens-token combination has never
        # been computed before.
        if (prev_tokens is None or prev_tokens == tuple()):  
            prev_tokens = []

        if (prev_tokens == []):
            return self.unigram_model.cond_prob(token=token)

        elif (tuple(list(prev_tokens) + [token]) in  self.__q_D.keys()):
            return self.__q_D[tuple(list(prev_tokens) + [token])]

        elif (len(prev_tokens) == 1):
            if (token in self.A(prev_tokens)):
                res = self.__count_star(list(prev_tokens) + [token])
                res /= float(self.count(prev_tokens))
            else:
                try:
                    res = self.__max_likelihood_prob(token=token, 
                        prev_tokens=prev_tokens[1:]) 
                    res /= self.denom(prev_tokens)
                    res *=  self.alpha(prev_tokens)
                except ZeroDivisionError:
                    res = 0.0
        else:
            if (token in self.A(prev_tokens)):
                res = self.__count_star(list(prev_tokens) + [token]) / float(self.count(prev_tokens))
            else:
                try:
                    res = self.cond_prob(token=token, 
                        prev_tokens=prev_tokens[1:]) 
                    res /= self.denom(prev_tokens)
                    res *= self.alpha(prev_tokens)
                except ZeroDivisionError:
                    res = 0.0

        # Memorize the result for this prev_tokens-token combination.
        self.__q_D[tuple(list(prev_tokens) + [token])] = res
        return (res)

    def sent_prob(self, sent):
        """ Probability of a sentence. Warning: subject to underflow problems.
 
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

    def A(self, tokens):
        """ Set of words with counts > 0 for a k-gram with 0 < k < n.
 
            tokens -- the k-gram tuple.
        """
        if (tuple(tokens) in self.__A.keys()):
            return (self.__A[tuple(tokens)])

        res = set([gram[-1] for gram in self.counts.keys()   
                if  (len(gram) > 0 and tuple(tokens) == gram[:-1]
                        and self.counts[gram] > 0)])

        self.__A[tuple(tokens)] = res
        return (res)
 
    def alpha(self, tokens):
        """ Missing probability mass for a k-gram with 0 < k < n.
 
            tokens -- the k-gram tuple.
        """

        if (tuple(tokens) in self.__alpha.keys()):
            return (self.__alpha[tuple(tokens)])

        try:
            res = self.beta * len(self.A(tokens)) / self.count(tuple(tokens))
        except ZeroDivisionError:
            res = 0.0

        self.__alpha[tuple(tokens)] = res
        return (res)
 
    def denom(self, tokens):
        """ Normalization factor for a k-gram with 0 < k < n.
 
            tokens -- the k-gram tuple.
        """
        if (tuple(tokens) in self.__denom.keys()):
            return (self.__denom[tuple(tokens)])

        sum_cond_prob = 0.0

        if (len(tokens) > 1):
            for token in self.A(tokens):
                sum_cond_prob += self.cond_prob(token=token, prev_tokens=tokens[1:])
        else:
            for token in self.A(tokens):
                sum_cond_prob += self.__max_likelihood_prob(token=token)

        self.__denom[tuple(tokens)] = 1.0 - sum_cond_prob
        return (1.0 - sum_cond_prob)

    def __compute_beta(self, devel_set):
        """ Compute beta parameter for the model with the development set 
            (a.k.a. held-out data).
        """
        self.beta = best_beta = 0.1 
        self.__clear_memo()
        best_log = self.__compute_log_likelihood()

        for beta in [(x+1) / 10.0 for x in range(1,10)]:
            self.beta = beta
            self.__clear_memo()
            current_log = self.__compute_log_likelihood()
            if current_log > best_log:
                best_log = current_log
                best_beta = beta

        self.beta = best_beta

    def __compute_log_likelihood(self):
        """ Change self.gamma and compute log-likelihood.
            Restor self.gamma to its previous value, and return the 
            log-likelihood value obtained.
        """
        print("__compute_log_likelihood")
        log_likelihood = 0.0

        for key, value in self.counts_prime.items():
            try:
                log_likelihood += value * log (self.cond_prob(token=key[-1], prev_tokens=key[:-1]))
            except ValueError:
                # log(0). Do not add anything to log_likelihood.
                continue

        return (log_likelihood)

    def __max_likelihood_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token, corresponding to the maximum 
            likelihood estimator used in the previous classes. 
        """
        if prev_tokens is None or len(prev_tokens) == 0:
            prev_tokens = []

        if (prev_tokens == []):
            return self.unigram_model.cond_prob(token=token, prev_tokens=prev_tokens)
        else:
            ngram = tuple((['<s>'] * (self.n - 1 - len(prev_tokens))) + list(prev_tokens) + [token])
            return (self.count(ngram) / float(self.count(tuple(prev_tokens))))

    def __count_star(self, tokens):
        """ Discounted count of a k-gram, with 1 < k <= n.

            tokens -- the k-gram tuple.
        """
        return (self.count(tokens) - self.beta)

    def __clear_memo(self):
        # The following are for memoization purposes.
        self.__q_D = defaultdict(float)
        self.__alpha = defaultdict(float)
        self.__denom = defaultdict(float)
        self.__A = defaultdict(float)