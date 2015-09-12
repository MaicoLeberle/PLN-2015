import sys
import pickle
from optparse import OptionParser
from languagemodeling.ngram import NGram, NGramGenerator

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-i", dest="file", help="Language model file.", metavar="<file>")
	parser.add_option("-n", dest="n", help="Number of sentences to generate.", metavar="<n>")
	(options, args) = parser.parse_args()

	if options.file is None:
		if options.n is None:
			print("Missing parameters: file, number of sentences to generate.")
			parser.print_help()
			sys.exit(0)
		else:
			print("Missing parameter: file.")
			parser.print_help()
			sys.exit(0)
	elif options.n is None:
		print("Missing parameter: number of sentences to generate.")
		parser.print_help()
		sys.exit(0)


	# Here I read with pickle.load the NGram object saved, via pickle.load, 
	# into options.file.
	try:
		f = open(options.file, "rb")
	except IOError:
		print(str(options.file) + " is not a valid file.")
		sys.exit(0)

	model = pickle.load(f)

	generator = NGramGenerator(model)
	for i in range(int(options.n)):
		s = generator.generate_sent()
		s[0] = s[0].capitalize()
		print((' ').join(s[:-1]) + ".")
