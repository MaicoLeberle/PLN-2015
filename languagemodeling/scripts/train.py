"""Train an n-gram model.

Usage:
  train.py -n <n> -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
# from docopt import docopt
from optparse import OptionParser
import sys
import pickle

from nltk.corpus import brown

from languagemodeling.ngram import NGram, AddOneNGram


if __name__ == '__main__':
    # opts = docopt(__doc__)

    # # load the data
    # sents = brown.sents()

    # # train the model
    # n = int(opts['-n'])
    # model = NGram(n, sents)

    # # save it
    # filename = opts['-o']
    # f = open(filename, 'wb')
    # pickle.dump(model, f)
    # f.close()

    parser = OptionParser()
    parser.add_option("-o", dest="file", help="Output model file.", metavar="<file>")
    parser.add_option("-m", dest="model", help="Model to use [default: ngram]:\n \
                                                \t\t\tngram: Unsmoothed n-grams.\
                                                \t\t\taddone: N-grams with add-one smoothing.", metavar="<model>")
    parser.add_option("-n", dest="n", help="Order of the model.", metavar="<n>")
    (options, args) = parser.parse_args()
    file_on = not options.file is None
    n_on = not options.n is None

    # Checking model option.
    if options.model is None:
        options.model = 'ngram'
    if (options.model != 'ngram' and options.model != 'addone'):
        print("Invalid model.")
        parser.print_help()
        sys.exit(0)

    # Checking output file and order arguments.
    if not file_on or not n_on:
      print("Missing parameters:")
    if not file_on:
        print("\t* Output model file")
    if not n_on:
        print("\t* Order of the model")
    if not file_on or not n_on:
        sys.exit(0)

    sents = list(brown.sents())
    # print("type(sents): " + str(type(sents)))
    # assert(False)
    if options.model == 'ngram':
        model = NGram(int(options.n), sents)
    else:
        model = AddOneNGram(int(options.n), sents)

    try:
        f = open(options.file, "wb")
    except IOError:
        print(str(options.file) + " is not a valid file.")
        sys.exit(0)
    pickle.dump(model, f)
    f.close()
