"""Train a parser.
Usage:
  train.py [-m <model>] [-n <n>] -o <file>
  train.py -h | --help
Options:
  -m <model>    Model to use [default: flat]:
                  flat: Flat trees
                  rbranch: Right branching trees
                  lbranch: Left branching trees
  -n <n>        Horizontal Markovization parameter.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from corpus.ancora import SimpleAncoraCorpusReader

from parsing.baselines import Flat, RBranch, LBranch
from parsing.upcfg import UPCFG


models = {
    'flat': Flat,
    'rbranch': RBranch,
    'lbranch': LBranch,
    'upcfg': UPCFG
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    print('Loading corpus...')
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)

    print('Training model...')
    if(opts['-m'] != 'upcfg'):
        model = models[opts['-m']](corpus.parsed_sents())
    else:
        if (opts['-n'] is not None):
            model = UPCFG(parsed_sents=corpus.parsed_sents()
                        , horzMarkov=int(opts['-n']))
        else:
            model = UPCFG(parsed_sents=corpus.parsed_sents())

    print('Saving...')
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
