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

        for i in range(1, len(sent) + 1):
            self._pi[i] = dict()
            # Make a list of every tag in the tag set, paired with the
            # probability of that sequence of tags. Consider only those which
            # have probability that is not 0.
            aux = [(tag, self.__hmm.out_prob(sent[i-1], tag))
                   for tag in self.__hmm.tagset()]
            tags_and_out_probs = [(t, p) for (t, p) in aux if (p > 0.0)]
            for tag, probability in tags_and_out_probs:
                # Note that self._pi[i-1] is already defined, since self._pi[0]
                # is defined outside this for cycle, and this algorithm is
                # implemented in a DP fashion.
                for prev_n_1_gram in self._pi[i-1].keys():
                    (prob, tagging_so_far) = self._pi[i-1][prev_n_1_gram]
                    # c_tags (from "current tags") contains the sequence of
                    # tags of length (i+1) that is being analized now.
                    c_tags = tuple(prev_n_1_gram[1:]) + (tag,)
                    t_p = (self.__hmm).trans_prob(tag, prev_n_1_gram)
                    if (t_p > 0.0):
                        # There will be no ValueError for trying to compute
                        # math.log2(0).
                        # pos_max contains the maximum probability for c_tags.
                        pos_max = prob \
                            + math.log2(t_p) \
                            + math.log2(probability)
                        to_update = (pos_max, tagging_so_far + [tag])
                        # Now, self._pi[i+1] is updated if necessary.
                        if (c_tags not in self._pi[i].keys()
                                or self._pi[i][c_tags][0] < pos_max):
                                    # If c_tags is not in self._pi[i].keys(),
                                    # or if it exists but the current value is
                                    # less than pos_max, then pos_max is its
                                    # maximum probability so far (the sequence
                                    # of tags in this case is
                                    # tags_so_far + [tag]).
                                    self._pi[i][c_tags] = to_update

        # Now that the DP algorithm is done, we must check for the most
        # probable tagging sequence registered. Also, we have to add the END
        # symbol </s> .
        result = []
        # best_log_prob, so far, is the smallest value before analisis
        # (as a log-probability, which is minus infinity).
        best_log_prob = float('-inf')
        # exit(1)
        for key, info in self._pi[len(sent)].items():
            (log_probability, tagging_sequence) = info
            transition_probability = self.__hmm.trans_prob('</s>', key)
            if (transition_probability > 0.0):
                pos_max = log_probability + math.log2(transition_probability)
                if (pos_max > best_log_prob):
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

        # self.__words_voc and self.__tags_voc are the set of words and tags
        # seen in training data, respectively. They will be needed mainly for
        # the addone smoothing (and the unknown method).
        self.__words_voc = set()
        self.__tags_voc = set()

        # self.__counts_n, self.__counts_n_1 and self.__counts_1 will have the
        # number of appearances in the training data, related to n-grams,
        # (n-1)-grams and unigrams of tags, respectively.
        self.__counts_n = defaultdict(int)
        self.__counts_n_1 = defaultdict(int)
        self.__counts_1 = defaultdict(int)

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
                # if (self._n > 2):
                #   # Update the number of occurrences of the unigram tag.
                self.__counts_1[(tag,)] += 1

                # Update counts for this (tag, word) occurrence.
                if (tag not in self.__counts_words.keys()):
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
                self.__counts_n_1[complete_sent[i:i+self._n-1]] += 1
                self.__counts_n[complete_sent[i:i+self._n]] += 1

        # For better performance of the model, the maximum likelihood values
        # that will be needed later are computed only once now, and stored.
        for prev_tags in list(self.__counts_n.keys()):
            if (addone):
                self.__q[prev_tags] = float(self.__counts_n[prev_tags] + 1)
                self.__q[prev_tags] /= float(self.__counts_n_1[prev_tags[:-1]]
                                             + len(self.__tags_voc))
            else:
                self.__q[prev_tags] = float(self.__counts_n[prev_tags])
                if (self.__q[prev_tags] != 0):
                    assert (prev_tags[:-1] in self.__counts_n_1.keys())
                    self.__q[prev_tags] /= self.__counts_n_1[prev_tags[:-1]]

        for tag in self.__tags_voc:
            if (tag not in self.__e.keys()):
                self.__e[tag] = defaultdict(float)
            for word in self.__words_voc:
                self.__e[tag][word] = float(self.__counts_words[tag][word])
                if (self.__counts_1[(tag,)] != 0):
                    self.__e[tag][word] /= self.__counts_1[(tag,)]

    def tcount(self, tokens):
        """Count for an n-gram or (n-1)-gram of tags.

        tokens -- the n-gram or (n-1)-gram tuple of tags.
        """
        if (tokens not in self.__counts_n.keys()
                and tokens not in self.__counts_n_1.keys()):
                    return 0

        if (tokens in self.__counts_n.keys()):
            return (self.__counts_n[tokens])
        else:
            return (self.__counts_n_1[tokens])

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """

        return (w not in self.__words_voc)

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

        key = (tuple(prev_tags) + (tag,))[-self._n:]
        assert(len(key) == self._n)

        if (self.__q[key] != 0.0):
            # Note that self.__q[key] already considers addone
            # smoothing (or its absence) due to the way self.__q is computed.
            return (self.__q[key])
        else:
            return (1 / float(len(self.__tags_voc)))

    def out_prob(self, word, tag):
        """Probability of a word given a tag.

        word -- the word.
        tag -- the tag.
        """
        ret = 0.0

        if (tag in self.__e.keys()):
            if (word in self.__e[tag].keys()):
                ret = self.__e[tag][word]
            else:
                ret = 1.0 / len(self.__words_voc)

        return (ret)

    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.

        y -- tagging.
        """
        ret = 1.0
        previous = ('<s>',) * (self._n - 1)
        y = tuple(y) + ('</s>', )

        for t in y:
            ret *= self.trans_prob(t, previous)
            if (self._n > 1):
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
        # ret = 0.0
        # previous = ('<s>',) * (self._n - 1)
        # y = tuple(y) + ('</s>', )

        # for t in y:
        #     # Since we are computing the log probability, then we have to add
        #     # and not multiply the results.
        #     ret += math.log2(self.trans_prob(t, previous))
        #     if (self._n != 1):
        #         previous = previous[1:] + (t,)

        # return (ret)
        return (math.log2(self.tag_prob()))

    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.

        x -- sentence.
        y -- tagging.
        """
        # assert(len(x) == len(y))

        # # The probability of a tagging, given a sentence and according to
        # # Collins notes, depends on the probability of a tag, given its
        # # context, and the probability of the word found, given that tag.
        # ret = self.tag_log_prob(y)
        # for i in range(len(x)):
        #     # Since we are computing the log probability, then we have to add
        #     # and not multiply the results.
        #     ret += math.log2(self.out_prob(x[i], y[i]))

        # return (ret)
        return (math.log2(self.prob(x, y)))

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.

        sent -- the sentence.
        """
        # ViterbiTagger is the class that returns the most probable tagging for
        #  a sentence, using the Viterbi algorithm.
        aux = ViterbiTagger(self)

        return (aux.tag(sent))
