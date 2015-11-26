"""Evaulate a parser.
Usage:
  eval.py -i <file> [-m <m>] [-n <n>]
  eval.py -h | --help
Options:
  -i <file>     Parsing model file.
  -m <m>        Evaluate only sentences whose lengths do not exceed m.
  -n <n>        Evaluate only the first n sentences.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import sys

from corpus.ancora import SimpleAncoraCorpusReader

from parsing.util import spans


def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':
    opts = docopt(__doc__)

    print('Loading model...')
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    if (opts['-m'] is None):
        # Easiest way to indicate that EVERY sentence should be evaluated,
        # not only those that do not exceed some limit length.
        m = float('inf')
    else:
        # float()-ing as to have uniformity in the types.
        m = float(opts['-m'])

    print('Loading corpus...')
    files = '3LB-CAST/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)
    # Every element in corpus.parsed_sents() retrieves its sentence, tokenized,
    #  through the method leaves.
    parsed_sents = [sent 
                        for sent in list(corpus.parsed_sents()) 
                        if len(sent.leaves()) <= m]
    if (opts['-n'] is not None):
        parsed_sents[:int(opts['-n'])]

    print('Parsing...')
    hits, total_gold, total_model, unlabeled_hits = 0, 0, 0, 0
    n = len(parsed_sents)
    format_str = '{:3.1f}% ({}/{}) (P={:2.2f}%, R={:2.2f}%, F1={:2.2f}%)'
    progress(format_str.format(0.0, 0, n, 0.0, 0.0, 0.0))
    for i, gold_parsed_sent in enumerate(parsed_sents):
        tagged_sent = gold_parsed_sent.pos()

        # parse
        model_parsed_sent = model.parse(tagged_sent)

        # compute labeled scores
        gold_spans = spans(gold_parsed_sent, unary=False)
        model_spans = spans(model_parsed_sent, unary=False)
        hits += len(gold_spans & model_spans)
        total_gold += len(gold_spans)
        total_model += len(model_spans)

        # compute unlabeled scores

        # Every element in gold_spans is composed by (n, i, j), where n is the 
        # non-terminal, i is the beginning of the interval and j is the ending
        # of the interval.
        unlabeled_gold_spans = set([(x[1], x[2]) for x in gold_spans])
        unlabeled_model_spans = set([(x[1], x[2]) for x in model_spans])
        # unlabeled_hits is the number of elements that were correctly parsed 
        # with the model. & is the symbol for intersection between sets.
        unlabeled_hits += len(unlabeled_gold_spans & unlabeled_model_spans)

        # compute labeled partial results
        prec = float(hits) / total_model * 100
        rec = float(hits) / total_gold * 100
        f1 = 0.0
        if (prec + rec != 0):
            f1 = 2 * prec * rec / (prec + rec)

        # compute unlabeled partial results

        unlabeled_prec = (unlabeled_hits / total_model) * 100
        unlabeled_rec = (unlabeled_hits / total_gold) * 100
        unlabeled_f1 = 0.0
        if (unlabeled_prec + unlabeled_rec != 0):
            unlabeled_f1 = 2 * unlabeled_prec * unlabeled_rec / (unlabeled_prec + unlabeled_rec)

        progress(format_str.format(float(i+1) * 100 / n, i+1, n, prec, rec, f1))
        progress(format_str.format(float(i+1) * 100 / n, i+1, n, unlabeled_prec, unlabeled_rec, unlabeled_f1))

    print('')
    print('Parsed {} sentences'.format(n))
    print('Labeled:')
    print('  Precision: {:2.2f}% '.format(prec))
    print('  Recall: {:2.2f}% '.format(rec))
    print('  F1: {:2.2f}% '.format(f1))
    print('Unlabeled:')
    print('  Precision: {:2.2f}% '.format(unlabeled_prec))
    print('  Recall: {:2.2f}% '.format(unlabeled_rec))
    print('  F1: {:2.2f}% '.format(unlabeled_f1))
