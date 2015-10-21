"""Train a sequence tagger.

Usage:
	train.py [-m <model> -n <n>] -o <file>
	train.py -h | --help

Options:
	-m <model>    Model to use [default: base]:
								base: Baseline (default).
								mlhmm: Maximum likelihood hidden Markov model
								memm: Maximum Entropy Markov Model
	-n <n>        Length of n-grams for the mlhmm or memm model.
	-o <file>     Output model file.
	-h --help     Show this screen.
"""
from docopt import docopt
import pickle

from corpus.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger
from tagging.hmm import MLHMM
from tagging.memm import MEMM


models = {
		'base': BaselineTagger,
		'mlhmm': MLHMM,
		'memm': MEMM
}


if __name__ == '__main__':
	opts = docopt(__doc__)

	# load the data
	files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
	corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)
	sents = list(corpus.tagged_sents())


	# train the model
	if (opts['-m'] is None or opts['-m'] == 'base'):
		model = models[opts['-m']](sents)
	elif (opts['-m'] is 'mlhmm'):
		if (opts['-n'] is None):
			print("Missing -n parameter for the mlhmm model creation.")
			print("Invalid model.")
			parser.print_help()
			sys.exit(0)	
		# addone option is left to default (i.e., True).
		model = MLHMM(opts['-n'], sents)
	elif (opts['-m'] == 'memm'):
		if (opts['-n'] is None):
			print("Missing -n parameter for the memm model creation.")
			print("Invalid model.")
			parser.print_help()
			sys.exit(0)	
		# addone option is left to default (i.e., True).
		model = MEMM(opts['-n'], sents)
	else:
		print("Invalid model.")
		parser.print_help()
		sys.exit(0)

	# save it
	filename = opts['-o']
	f = open(filename, 'wb')
	pickle.dump(model, f)
	f.close()
