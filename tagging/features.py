from collections import namedtuple

from featureforge.feature import Feature


# sent -- the whole sentence.
# prev_tags -- a tuple with the n previous tags.
# i -- the position to be tagged.
History = namedtuple('History', 'sent prev_tags i')


def word_lower(h):
    """Feature: current lowercased word.

    h -- a history.
    """
    sent, i = h.sent, h.i
    return (sent[i].lower())


def word_istitle(h):
    """Feature: Is h a title?

    h -- a history.
    """
    sent, i = h.sent, h.i

    return (sent[i].istitle())


def word_isupper(h):
    """Feature: Is h uppercased?

    h -- a history.
    """
    sent, i = h.sent, h.i

    return (sent[i].isupper())


def word_isdigit(h):
    """Feature: Is h in digits?

    h -- a history.
    """
    sent, i = h.sent, h.i

    return (sent[i].isdigit())


def prev_tags(h):
    """ Previous tags.

    h -- a history.
    """
    return (h.prev_tags)


class NPrevTags(Feature):

    def __init__(self, n):
        """Feature: n previous tags tuple.

        n -- number of previous tags to consider.
        """
        assert(n > 0)
        self.__n = n

    def _evaluate(self, h):
        """n previous tags tuple.

        h -- a history.
        """
        return ((list(h.prev_tags))[-(self.__n):])


class PrevWord(Feature):

    def __init__(self, f):
        """Feature: the feature f applied to the previous word.

        f -- the feature.
        """
        self.__f = f

    def _evaluate(self, h):
        """Apply the feature to the previous word in the history.

        h -- the history.
        """
        if (h.i is 0):
            # According to tests, result here should be 'BOS'.
            return ('BOS')
        else:
            # Return the result of applying self.__f to a new history with the
            # same sent, same prev_tags, and changed i (i is now (i - 1)).
            return (str(self.__f(History(h.sent, h.prev_tags, h.i - 1))))
