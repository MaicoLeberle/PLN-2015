import math
from collections import defaultdict

class HMM:
 
    def __init__(self, n, tagset, trans, out):
        """
        n -- n-gram size.
        tagset -- set of tags.
        trans -- transition probabilities dictionary.
        out -- output probabilities dictionary.
        """
        assert(n > 0)

        # n is requested by ViterbiTagger; hence, it is not private attribute.
        self._n = n
        self.__tagset = tagset
        self.__trans = trans
        self.__out = out
 
    def tagset(self):
        """Returns the set of tags.
        """

        return (self.__tagset)

    def trans_prob(self, tag, prev_tags):
        """Probability of a tag.
 
        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        assert(prev_tags is not None or self._n > 1)

        ret = 0.0

        if (prev_tags in self.__trans.keys() 
            and tag in self.__trans[prev_tags].keys()):
                ret = self.__trans[prev_tags][tag]
        return (ret)
 
    def out_prob(self, word, tag):
        """Probability of a word given a tag.
 
        word -- the word.
        tag -- the tag.
        """
        ret = 0.0

        if (tag in self.__out.keys() and word in self.__out[tag].keys()):
            ret = self.__out[tag][word]
        return (ret)
 
    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.
 
        y -- tagging.
        """
        ret = 1
        previous = ('<s>',) * (self._n - 1)
        y = tuple(y) + ('</s>', )

        for t in y:
            ret *= self.trans_prob(t, previous)
            previous = previous[1:] + (t,)

        return (ret)
 
    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.
 
        x -- sentence.
        y -- tagging.
        """
        assert (len(x) == len(y))

        # The probability of a tagging, given a sentence and according to 
        # Collins notes, depends on the probability of a tag, given its 
        # context, and the probability of the word found, given that tag.
        ret = self.tag_prob(y)

        for i in range(len(x)):
            ret *= self.out_prob(x[i], y[i])

        return (ret)
 
    def tag_log_prob(self, y):
        """
        Log-probability of a tagging.
 
        y -- tagging.
        """
        ret = 0.0
        previous = ('<s>',) * (self._n - 1)
        y = tuple(y) + ('</s>', )

        for t in y:
            # Since we are computing the log probability, then we have to add 
            # and not multiply the results.
            ret += math.log2(self.trans_prob(t, previous))
            previous = previous[1:] + (t,)

        return (ret)
 
    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.
 
        x -- sentence.
        y -- tagging.
        """
        assert(len(x) == len(y))

        # The probability of a tagging, given a sentence and according to 
        # Collins notes, depends on the probability of a tag, given its 
        # context, and the probability of the word found, given that tag.
        ret = self.tag_log_prob(y)
        for i in range(len(x)):
            # Since we are computing the log probability, then we have to add 
            # and not multiply the results.
            ret += math.log2(self.out_prob(x[i], y[i]))

        return (ret)
 
    def tag(self, sent):
        """Returns the most probable tagging for a sentence.
 
        sent -- the sentence.
        """
        # ViterbiTagger is the class that returns the most probable tagging for
        #  a sentence, using the Viterbi algorithm.
        aux = ViterbiTagger(self)

        return (aux.tag(sent))
 
 
class ViterbiTagger:
 
    def __init__(self, hmm):
        """
        hmm -- the HMM.
        """
        self.__hmm = hmm
        # self._pi is requested by tagging/tests/test_viterbi_tagger.py
        # ; hence, it is not a private attribute.
        self._pi = dict()
 
    def tag(self, sent):
        """Returns the most probable tagging for a sentence.
 
        sent -- the sentence.
        """
        self._pi[0] = dict()
        # The maximum probability of getting to the (n-1)-gram of <s>'s at the 
        # beginning of the analisis is 1.0 (then, the value saved will be 
        # log2(1.0) == 0). This constitutes the base case.
        self._pi[0][('<s>',) * (self.__hmm._n - 1)] = (0, [])

        for i in range(0,len(sent)):
            for n_gram in self._pi[i].keys():
                # prob is the probability of having got to tags_so_far.
                (log_prob, tags_so_far) = self._pi[i][n_gram]
                # Having analized sequences of length up to i, we now analize 
                # the maximum probability for the sequence of length (i+1).
                self._pi[i+1] = dict()
                for t in self.__hmm.tagset():
                    # c_tags (from "current tags") contains the sequence of 
                    # tags of length (i+1) that is being analized now.
                    c_tags = tuple(n_gram[1:]) + (t,)
                    # pos_max contains the maximum probability for c_tags.
                    pos_max = log_prob
                    try:
                        pos_max += math.log2(self.__hmm.trans_prob(t, n_gram))
                        pos_max += math.log2(self.__hmm.out_prob(sent[i], t))
                    except ValueError:
                        # If the transition or out probability are 0, then a 
                        # math domain error raises, due to the fact that this 
                        # case is not possible.
                        continue
                    # Now, self._pi[i+1] is updated if necessary.
                    if ((not c_tags in self._pi[i+1].keys())
                        or (c_tags in self._pi[i+1].keys() 
                            and self._pi[i+1][c_tags][0] < pos_max)):
                        # If c_tags is not in self._pi[i+1].keys(), or if it 
                        # exists but the current value is less than pos_max,
                        # then pos_max is its maximum probability so far (the
                        # sequence of tags in this case is tags_so_far + [t]).
                        self._pi[i+1][c_tags] = (pos_max, tags_so_far + [t])

        # Now that the DP algorithm is done, we must check for the most 
        # probable tagging sequence registered.
        result = []
        # best_log_prob, so far, is the smallest value before analisis 
        # (as a log-probability).
        best_log_prob = float('-inf')
        for info in self._pi[len(sent)].values():
            (log_probability, tagging_sequence) = info
            if (result == [] or log_probability > best_log_prob):
                result = tagging_sequence
                best_log_prob = log_probability

        return (result)

class MLHMM:
 
    def __init__(self, n, tagged_sents, addone=True):
        """
        n -- order of the model.
        tagged_sents -- training sentences, each one being a list of pairs.
        addone -- whether to use addone smoothing (default: True).
        """
        self._n = n
        self.__tagged_sents = tagged_sents
        self.__addone = addone
        # self.__words_voc and self.__tags_voc are the set of words and tags 
        # seen in training data, respectively. They will be needed mainly for 
        # the addone smoothing (and the self.unknown method).
        self.__words_voc = set()
        self.__tags_voc = set()
        # self.__counts will have the number of appearances in the training 
        # data, related to n-grams, (n-1)-grams and unigrams of tags.
        self.__counts = defaultdict(int)
        # self.__counts_words will have the number of times certain tag has 
        # been paired with a certain word
        self.__counts_words = dict()
        # self.__e is the maximum likelihood estimator of seeing a word given
        # its tag.
        self.__e = dict()
        # self.__q is the maximum likelihood estimator of finding a tag given
        # a (self._n - 1)-gram of previous tags.
        self.__q = defaultdict(float)

        # Store every piece of information that will be needed later.
        for sent in tagged_sents:
            for (word, tag) in sent:
                # Update the number of occurrences of the unigram tag.
                self.__counts[(tag,)] += 1
                # Update counts for this (tag, word) occurrence.
                if (not tag in self.__counts_words.keys()):
                    self.__counts_words[tag] = defaultdict(int)
                self.__counts_words[tag][word] += 1
                # Add these word and tag to their respective sets.
                self.__words_voc.add(word)
                self.__tags_voc.add(tag)
            # Next, update counts for n-grams and (n-1)-grams.
            complete_sent = ('<s>',) * (self._n - 1)
            for (word, tag) in sent:
                complete_sent += (tag,)
            complete_sent += ('</s>',)
            for i in range(len(complete_sent) - self._n + 1):
                self.__counts[complete_sent[i+1:i+n]] += 1
                self.__counts[complete_sent[i:i+n]] += 1

        # For better performance of the model, the maximum likelihood values
        # that will be needed later are computed only once now, and stored.
        for prev_tags in self.__counts.keys():
            if (len(prev_tags) is self._n):
                if (not self.__addone):
                    self.__q[prev_tags] = self.__counts[prev_tags]
                    if (self.__counts[prev_tags[1:]] != 0):
                        self.__q[prev_tags] /= self.__counts[prev_tags[1:]]
                else:
                    self.__q[prev_tags] = (self.__counts[prev_tags] + 1)
                    self.__q[prev_tags] /= float(self.__counts[prev_tags[1:]] 
                        + len(self.__tags_voc))
        for tag in self.__tags_voc:
            if (not tag in self.__e.keys()):
                self.__e[tag] = defaultdict(float)
            for word in self.__words_voc:
                # Note that the following is correct, since 
                # self.__counts_words[tag][word] will be 0 if never has tag 
                # been paired with word.
                if (not self.__addone):
                    self.__e[tag][word] = self.__counts_words[tag][word] 
                    self.__e[tag][word] /= self.__counts[(tag,)]
                else:
                    self.__e[tag][word] = self.__counts_words[tag][word] + 1
                    self.__e[tag][word] /= \
                        self.__counts[(tag,)] + len(self.__tags_voc)
 
    def tcount(self, tokens):
        """Count for an n-gram or (n-1)-gram of tags.
 
        tokens -- the n-gram or (n-1)-gram tuple of tags.
        """
        if (not tokens in self.__counts.keys()):
            return 0

        return (self.__counts[tokens])
 
    def unknown(self, w):
        """Check if a word is unknown for the model.
 
        w -- the word.
        """

        return (not w in self.__words_voc)

    def tagset(self):
        """Returns the set of tags.
        """

        return (self.__tags_voc)
 
    def trans_prob(self, tag, prev_tags):
        """Probability of a tag.
 
        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        if (prev_tags is None):
            prev_tags = ()
        
        # Note that self.__q[prev_tags + (tag,)] already considers addone 
        # smoothing (or its absence) due to the way self.__q is computedself.
        return (self.__q[prev_tags + (tag,)])
 
    def out_prob(self, word, tag):
        """Probability of a word given a tag.
 
        word -- the word.
        tag -- the tag.
        """
        ret = 0.0

        if (tag in self.__e.keys()):
            # Note that self.__e[tag][word] already considers addone smoothing
            # (or its absence) due to the way self.__e is computed.
            ret = self.__e[tag][word]

        return (ret)
 
    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.
 
        y -- tagging.
        """
        ret = 1
        previous = ('<s>',) * (self._n - 1)
        y = tuple(y) + ('</s>', )

        for t in y:
            ret *= self.trans_prob(t, previous)
            previous = previous[1:] + (t,)

        return (ret)
 
    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.
 
        x -- sentence.
        y -- tagging.
        """
        assert (len(x) == len(y))

        ret = self.tag_prob(y)

        for i in range(len(x)):
            ret *= self.out_prob(x[i], y[i])

        return (ret)
 
    def tag_log_prob(self, y):
        """
        Log-probability of a tagging.
 
        y -- tagging.
        """
        ret = 0.0
        previous = ('<s>',) * (self._n - 1)
        y = tuple(y) + ('</s>', )

        for t in y:
            # Since we are computing the log probability, then we have to add 
            # and not multiply the results.
            ret += math.log2(self.trans_prob(t, previous))
            previous = previous[1:] + (t,)

        return (ret)
 
    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.
 
        x -- sentence.
        y -- tagging.
        """
        assert(len(x) == len(y))

        # The probability of a tagging, given a sentence and according to 
        # Collins notes, depends on the probability of a tag, given its 
        # context, and the probability of the word found, given that tag.
        ret = self.tag_log_prob(y)
        for i in range(len(x)):
            # Since we are computing the log probability, then we have to add 
            # and not multiply the results.
            ret += math.log2(self.out_prob(x[i], y[i]))

        return (ret)
 
    def tag(self, sent):
        """Returns the most probable tagging for a sentence.
 
        sent -- the sentence.
        """
        # ViterbiTagger is the class that returns the most probable tagging for
        #  a sentence, using the Viterbi algorithm.
        aux = ViterbiTagger(self)

        return (aux.tag(sent))