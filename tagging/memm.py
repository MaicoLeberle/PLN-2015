from tagging.features import (History, word_lower, word_istitle, word_isupper,
                              word_isdigit, NPrevTags, PrevWord)
from featureforge.vectorizer import Vectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline


class MEMM:

    def __init__(self, n, tagged_sents, classifier='LR'):
        """
        n -- order of the model.
        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        self.__n = n
        self.__tagged_sents = tagged_sents
        # self.__voc is only used for self.unknown method.
        self.__voc = set()

        for sent in tagged_sents:
            for (word, tag) in sent:
                self.__voc.add(word)

        if (classifier == 'LSVC'):
            classif = LinearSVC()
        elif (classifier == 'MNB'):
            classif = MultinomialNB()
        else:
            classif = LogisticRegression()

        vect_params = [word_lower, word_istitle, word_isupper, word_isdigit]
        vect_params += [PrevWord(f) for f in vect_params]
        vect_params += [NPrevTags(j) for j in range(1, self.__n)]

        pipeline_params = [('vectorizer', Vectorizer(vect_params)),
                           ('classifier', classif)]

        self.__pipeline = Pipeline(pipeline_params)
        self.__pipeline.fit(self.sents_histories(tagged_sents),
                            self.sents_tags(tagged_sents))

    def sents_histories(self, tagged_sents):
        """
        Iterator over the histories of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        # ret will be a list of lists of Historys.
        ret = []

        for sent in tagged_sents:
            ret += self.sent_histories(sent)

        return (ret)

    def sent_histories(self, tagged_sent):
        """
        Iterator over the histories of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        # ret will be a list of Historys.
        ret = []
        previous = ('<s>',) * (self.__n - 1)
        words = []

        for i in range(len(tagged_sent)):
            (word, tag) = tagged_sent[i]
            words.append(word)
            ret.append(History(words, previous, i))
            if (self.__n != 1):
                previous = previous[1:] + (tag,)

        return (ret)

    def sents_tags(self, tagged_sents):
        """
        Iterator over the tags of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        ret = []

        for sent in tagged_sents:
            ret += self.sent_tags(sent)

        return (ret)

    def sent_tags(self, tagged_sent):
        """
        Iterator over the tags of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        ret = []

        for (word, tag) in tagged_sent:
            ret.append(tag)
        return (ret)

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        ret = []
        previous = ('<s>',) * (self.__n - 1)

        for i in range(len(sent)):
            aux = self.tag_history(History(sent, previous, i))
            ret.append(aux)
            if (self.__n != 1):
                previous = previous[1:] + (aux,)

        return (ret)

    def tag_history(self, h):
        """Tag a history.

        h -- the history.
        """
        return ((self.__pipeline.predict([h]))[0])

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return (w not in self.__voc)
