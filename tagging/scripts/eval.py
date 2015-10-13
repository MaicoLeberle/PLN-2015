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
	set_tags = set()

	# These are going to be used for creating the confusion matrix.
	original_dict = defaultdict(int)
	treebank_dict = defaultdict(int)
	# The confusion matrix, as explained in Jurafsky & Martin.
	original_matrix = defaultdict(int)
	treebank_matrix = defaultdict(int)

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
		for j, (from_model, from_corpus) in 
			enumerate(zip(model_tag_sent, gold_tag_sent)):

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
			set_tags.add(from_model)
			set_tags.add(from_corpus)

        hits += sum(hits_sent)
        total += len(sent)
		known_count_total += known_count
		unknown_count_total += unknown_count
        acc = float(hits) / total

        progress('{:3.1f}% ({:2.2f}%)'.format(float(i) * 100 / n, acc * 100))

    acc = float(hits) / total

    print('')
    print('Accuracy: {:2.2f}%'.format(acc * 100))
	print("Accuracy of known words: " 
		+ str(known_count_total * 100 / float(total)) + "%.")
	print("Accuracy of unknown words: " 
		+ str(unknown_count_total * 100 / float(total)) + "%.")

	# Compute confusion matrix for original tagging. 
	for word in original_dict.keys():
		original_matrix[len(original_dict[word])] += 1
	print("Original tagging:")
	for key in original_matrix.keys():
		print("\t" + str(key) + "\t->\t" + str(original_matrix[key]))

	# Compute confusion matrix for treebank tagging.
	for word in treebank_dict.keys():
		treebank_matrix[len(treebank_dict[word])] += 1
	print("Treebank tagging:")
	for key in treebank_matrix.keys():
		print("\t" + str(key) + "\t->\t" + str(treebank_matrix[key]))
