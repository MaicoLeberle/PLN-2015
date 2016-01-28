"""Evaluate a tagger.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Tagging model file.
  -h --help     Show this screen.
"""
import matplotlib.pyplot as pyplot
import numpy as np
from docopt import docopt
import pickle
import sys
from collections import defaultdict

from corpus.ancora import SimpleAncoraCorpusReader


def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':
    opts = docopt(__doc__)

    # Load the model.
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    # Load the data.
    files = '3LB-CAST/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)
    sents = list(corpus.tagged_sents())

    # Start evaluation.
    n = len(sents)

    hits, total = 0, 0
    hits_known, hits_unknown = 0, 0
    total_known, total_unknown = 0, 0

    # For confusion matrix. They are going to be filled with every new
    # tag that the model returns (model_tags), or with the correct tag
    gold_tags = set()
    model_tags = set()

    confusion_matrix = defaultdict(dict)

    for i, sent in enumerate(sents):
        word_sent, gold_tag_sent = zip(*sent)

        model_tag_sent = model.tag(word_sent)
        assert len(model_tag_sent) == len(gold_tag_sent), i

        # Update gold_tags and model_tags sets.
        gold_tags |= set(gold_tag_sent)
        model_tags |= set(model_tag_sent)

        # known and unknown score
        total_errors = 0
        for m, g, w in zip(model_tag_sent, gold_tag_sent, word_sent):
            if model.unknown(w):
                hits_unknown += (m == g)
                total_unknown += 1
            else:
                hits_known += (m == g)
                total_known += 1
            # Confusion Matrix
            if m != g:
                if m not in confusion_matrix[g]:
                    confusion_matrix[g][m] = 0
                confusion_matrix[g][m] += 1
                total_errors += 1

        # global score
        hits_sent = [m == g for m, g in zip(model_tag_sent, gold_tag_sent)]
        hits += sum(hits_sent)
        total += len(sent)
        acc = float(hits) / total

        progress('{:3.1f}% ({:2.2f}%)'.format(float(i) * 100 / n, acc * 100))

    # Results expected with regards to the model's accuracy.
    acc = float(hits) / total
    acc_known = float(hits_known) / total_known
    acc_unknown = float(hits_unknown) / total_unknown

    print('')
    print('Accuracy: {:2.2f}%'.format(acc * 100))
    print('Accuracy known: {:2.2f}%'.format(acc_known * 100))
    print('Accuracy unknown: {:2.2f}%'.format(acc_unknown * 100))

    # Build confusion matrix.
    cm = []

    model_tags_list = sorted(list(model_tags))
    cant_model_tags = len(model_tags)

    gold_tags_list = sorted(list(gold_tags))
    cant_gold_tags = len(gold_tags)

    # First, build confusion matrix.
    for gold_tag in gold_tags_list:
        # Start by creating a row associated to gold_tag, all filled with 0s.
        positions = [0] * cant_model_tags
        for t, v in sorted(confusion_matrix[gold_tag].items(),
                           key=lambda x: x[0]):
            # Then, for every tag t returned by the model, insert the number
            # of times gold_tag was confused with t.
            pos = model_tags_list.index(t)
            positions.remove(positions[pos])
            positions.insert(pos, v)
        # Finally, insert the row in the confusion matrix.
        cm.append(positions)

    # Now show confusion matrix in a separate window.
    pyplot.matshow(cm)
    # Reference data.
    pyplot.colorbar()
    pyplot.title('Confusion matrix')
    pyplot.ylabel('Right label')
    pyplot.xlabel('Model-attributed label')
    pyplot.xticks(np.arange(cant_model_tags), tuple(model_tags_list),
                  rotation=90)
    pyplot.yticks(np.arange(cant_gold_tags), tuple(gold_tags_list))

    pyplot.show()
