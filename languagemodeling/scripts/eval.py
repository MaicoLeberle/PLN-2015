""" Evaluate log-probability, cross-entropy and perplexity.

"""

from optparse import OptionParser
import sys
import pickle
from nltk.corpus import brown
from languagemodeling.ngram import NGram, AddOneNGram

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-i", dest="file", help="Language model file.", metavar="<file>")
	(options, args) = parser.parse_args()

	if options.file is None: 
		print("Missing parameter: file.")
		parser.print_help()
		sys.exit(0)

	try:
		f = open(options.file, "rb")
	except IOError:
		print(str(options.file) + " could not be opened.")
		sys.exit(0)

	try:
		lang_model = pickle.load(f)
	except pickle.UnpicklingError:
		print(str(options.file) + " is not a valid language model file.")
		sys.exit(0)

	# The last 10% of the corpus is the test set.
	test_sents = list(brown.sents())[int(len(brown.sents()) * 0.9):]

	print("log-probability: " + str(lang_model.log_probability(test_sents)))
	print("perplexity: " + str(lang_model.perplexity(test_sents)))
	print("cross-entropy: " + str(lang_model.cross_entropy(test_sents)))