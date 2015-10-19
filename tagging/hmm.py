import math

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
            # Since we are computing the log probability, then we have to add and
            # not multiply the results.
            ret += math.log2(self.trans_prob(t, previous))
            previous = previous[1:] + (t,)

        return (ret)
 
    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.
 
        x -- sentence.
        y -- tagging.
        """
        # The probability of a tagging, given a sentence and according to 
        # Collins notes, depends on the probability of a tag, given its 
        # context, and the probability of the word found, given that tag.
        ret = self.tag_log_prob(y)
        for i in range(len(x)):
            # Since we are computing the log probability, then we have to add and
            # not multiply the results.
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
        # The probability of getting to the (n-1)-gram of <s>'s at the 
        # beginning of the analisis is 1.0 (then, the value saved will be 
        # log2(1.0) == 0). This constitutes the base case.
        self._pi[0][('<s>',) * (self.__hmm._n - 1)] = (0, [])

        for i in range(0,len(sent)):
            for n_gram in self._pi[i].keys():
                # prob is the probability of having got to tags_so_far.
                (log_prob, tags_so_far) = self._pi[i][n_gram]
                self._pi[i+1] = dict()
                for t in self.__hmm.tagset():
                    # prev_tags will now contain the previous (n-1)-gram, 
                    # followed in each loop by a tag in the tag set.
                    prob = log_prob
                    prob += math.log2(self.__hmm.trans_prob(t, n_gram))
                    prob += math.log2(self.__hmm.out_prob(sent[i], t))
                    # Now, self._pi[i+1] is updated. This happens if the 
                    # current sequence of tags (namely, tags_so_far + t)'s 
                    # probability is less than the current probability 
                    # (namely, prob).
                    # Notice that ngram[:1] + (t,) is the (n-1)-gram created 
                    # with the (n-2) last tags from ngram followed by t.
                    if ((not t in self._pi[i+1].keys()) or (self._pi[i+1][n_gram[:1] + (t,)][0] < log_prob)):
                            self._pi[i+1][n_gram[:1] + (t,)] = (log_prob, tags_so_far + (t,))

        # Now that the DP algorithm is done, we must check for the most 
        # probable tagging sequence registered.
        result = []
        # best_log_prob, so far, is the smallest value before analisis 
        # (as a log-probability).
        best_log_prob = float('-inf')
        for info in self._pi[len(sent)].values():
            (log_probability, tagging_sequence) = info
            if (result == [] or probability > best_log_prob):
                result = tagging_sequence
                best_log_prob = log_probability

        return (result)