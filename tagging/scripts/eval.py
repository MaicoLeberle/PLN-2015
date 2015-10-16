"""Evaulate a tagger.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Tagging model file.
  -h --help     Show this screen.
"""
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

	# load the model
	filename = opts['-i']
	f = open(filename, 'rb')
	model = pickle.load(f)
	f.close()

	# load the data
	files = '3LB-CAST/.*\.tbf\.xml'
	corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)
	sents = list(corpus.tagged_sents())

	# Keep count of every missed or hit tag.
	known_count_total = 0
	unknown_count_total = 0

	# Set of tags found on corpus data or tagged by the model.
	set_tags_model = set()
	set_tags_corpus = set()

	# These are going to be used for creating the confusion matrix.
	original_dict = defaultdict(int)
	treebank_dict = defaultdict(int)
	# The confusion matrix, as explained in Jurafsky & Martin.
	matrix = dict()

	# tag
	hits, total = 0, 0
	n = len(sents)

	for i, sent in enumerate(sents):
		known_count = 0
		unknown_count = 0
		word_sent, gold_tag_sent = zip(*sent)

		model_tag_sent = model.tag(word_sent)
		assert len(model_tag_sent) == len(gold_tag_sent), i

		# global score
		hits_sent = [m == g for m, g in zip(model_tag_sent, gold_tag_sent)]

		# Differentiate known from unknown words. Add tags to set_tags.
		for j, (from_model, from_corpus) \
			in enumerate(zip(model_tag_sent, gold_tag_sent)):

			# Filling information for matrix.
			if (not word_sent in original_dict.keys()):
				original_dict[word_sent[j]] = set()
			if (not word_sent in treebank_dict.keys()):
				treebank_dict[word_sent[j]] = set()
			original_dict[word_sent[j]].add(from_model)
			treebank_dict[word_sent[j]].add(from_corpus)

			if (not model.unknown(word_sent[j])):
				known_count += 1
			else:
				unknown_count += 1
			set_tags_model.add(from_model)
			set_tags_corpus.add(from_corpus)

			# Add current results to the confusion matrix.
			if (not from_corpus in matrix.keys()):
				matrix[from_corpus] = defaultdict(int)
			matrix[from_corpus][from_model] += 1

		hits += sum(hits_sent)
		total += len(sent)
		known_count_total += known_count
		unknown_count_total += unknown_count
		acc = float(hits) / total

		progress('{:3.1f}% ({:2.2f}%)'.format(float(i) * 100 / n, acc * 100))

	# Calculate accuracy level and total number of mistakes made when tagging.
	acc = float(hits) / total
	mis  = float(total - hits)
	# Sort set of tags from model and in corpus.
	set_tags_model = list(set_tags_model)
	set_tags_model.sort()
	set_tags_corpus = list(set_tags_corpus)
	set_tags_corpus.sort()

	print('')
	print('Accuracy: {:2.2f}%'.format(acc * 100))
	print("Accuracy of known words: " 
		+ str(known_count_total * 100 / float(total)) + "%.")
	print("Accuracy of unknown words: " 
		+ str(unknown_count_total * 100 / float(total)) + "%.")

	conf = dict()
	for tag_c in set_tags_corpus:
		conf[tag_c] = dict()
		for tag_m in set_tags_model:
			if (tag_c != tag_m):
				if (tag_m in matrix[tag_c].keys()):
					# Number of times tag_c was confused with tag_m, divided 
					# the total number of mistakes.
					conf[tag_c][tag_m] = 100 * matrix[tag_c][tag_m] / mis
				else:
					conf[tag_c][tag_m] = 0.0
			else:
				conf[tag_c][tag_m] = '-'

	for tag_c in set_tags_corpus:
		errors = any([  tag_m 
						for tag_m in conf[tag_c].keys() 
						if (not conf[tag_c][tag_m] in [0.0, '-'])
					 ])
		if (errors):
			print("(original tag) {:2}: ".format(tag_c))
			error_tags = [  x 
							for x in set_tags_model 
							if (not conf[tag_c][x] in [0.0, '-'])
						 ]
			for tag_m in error_tags:
				print("\ttag selected by model -> " + str(tag_m) + " ", end='')
				print("(with ", end='')
				print('{:2.4f}'.format(conf[tag_c][tag_m]), end='')
				print("% of the mistakes).")
			print()