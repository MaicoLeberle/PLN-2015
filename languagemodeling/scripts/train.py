"""Train an n-gram model.

Usage:
  train.py -n <n> -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from optparse import OptionParser
import sys
import pickle

from nltk.corpus import brown

from languagemodeling.ngram import NGram, AddOneNGram, InterpolatedNGram, BackOffNGram


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-o", dest="file", help="Output model file.", metavar="<file>")
    parser.add_option("-m", dest="model", help="Model to use [default: ngram]:\n \
                    \t\t\tngram: Unsmoothed n-grams.\
                    \t\t\taddone: N-grams with add-one smoothing.\
                    \t\t\tinterpolated: Smoothing by interpolation.\
                    \t\t\tbackoff: Smoothing by back-off with discounting."
                    , metavar="<model>")
    parser.add_option("-n", dest="n", help="Order of the model.", metavar="<n>")
    parser.add_option("--testing", dest="testing", action="store_true", default=False, help="Use only 90% of the corpus for training. Keep 10% for testing.")
    (options, args) = parser.parse_args()
    file_on = not options.file is None
    n_on = not options.n is None

    # Checking model option.
    if (options.model is None):
        options.model = 'ngram'
    if (options.model != 'ngram' and options.model != 'addone' and
             options.model != 'interpolated' and options.model != 'backoff'):
        print("Invalid model.")
        parser.print_help()
        sys.exit(0)

    # Checking output file and order arguments.
    if (not file_on or not n_on):
      print("Missing parameters:")
    if (not file_on):
        print("\t* Output model file")
    if (not n_on):
        print("\t* Order of the model")
    if (not file_on or not n_on):
        print()
        parser.print_help()
        sys.exit(0)

    if (options.testing):
        # The last 10% of the corpus is the test set.
        sents = list(brown.sents())[:int(len(brown.sents()) * 0.9)]
    
    else:
        sents = list(brown.sents())

    if (options.model == 'ngram'):
        model = NGram(int(options.n), sents)
    elif (options.model == 'addone'):
        model = AddOneNGram(int(options.n), sents)
    elif (options.model == 'interpolated'):
        model = InterpolatedNGram(int(options.n), sents)
    else:
        model = BackOffNGram(int(options.n), sents)

    try:
        f = open(options.file, "wb")
    except IOError:
        print(str(options.file) + " is not a valid file.")
        sys.exit(0)
    pickle.dump(model, f)
    f.close()
