"""Train a sequence tagger.

Usage:
	train.py [-m <model>] [-n <n>] [-c <classifier>] -o <file>
	train.py -h | --help

Options:
	-m <model>    	Model to use [default: base]:
								base: Baseline (default).
								mlhmm: Maximum likelihood hidden Markov model
								memm: Maximum Entropy Markov Model
	-n <n>        	Length of n-grams for the mlhmm or memm model.
	-c <classifier> Type of classifier used:
						LR: linear_model.LogisticRegression (default)
						LSVC: svm.LinearSVC 
						MNB: naive_bayes.MultinomialNB

	-o <file>     	Output model file.
	-h --help     	Show this screen.
"""
from optparse import OptionParser
import pickle
import sys

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
	parser = OptionParser()
	parser.add_option("-m", dest="model", help="Type of model to be trained.", metavar="<model>")
	parser.add_option("-n", dest="n", help="Length of n-grams for the mlhmm or memm model.", metavar="<n>")
	parser.add_option("-c", dest="classifier", help="Classifier to use with the memm model.", metavar="<classifier>")
	parser.add_option("-o", dest="output", help="Output model file.", metavar="<output>")
	(options, args) = parser.parse_args()

	# load the data
	files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
	corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)
	sents = list(corpus.tagged_sents())


	# train the model
	if (options.model is None or options.model == 'base'):
		model = models['base'](sents)
	elif (options.model == 'mlhmm'):
		if (options.n is None):
			print("Missing -n parameter for the mlhmm model creation.")
			print("Invalid model.")
			parser.print_help()
			sys.exit(0)	
		# addone option is left to default (i.e., True).
		model = MLHMM(int(options.n), sents)
		print("Created MLHMM tagger.")
	elif (options.model == 'memm'):
		if (options.n is None or options.classifier not in ['LR', 'LSVC', 'MNB']):
			print("Missing -n parameter for the memm model creation.")
			print("Invalid model.")
			parser.print_help()
			sys.exit(0)	
		model = MEMM(int(options.n), sents, classifier=options.classifier)

	else:
		print("Invalid model: " + str(options.model))
		parser.print_help()
		sys.exit(0)

	if (not options.output is None):
		# save it
		filename = options.output
		f = open(filename, 'wb')
		pickle.dump(model, f)
		f.close()
	else:
		print("Missing output file.\n")
		parser.print_help()
		sys.exit(0)