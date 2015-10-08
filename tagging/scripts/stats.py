"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt

from corpus.ancora import SimpleAncoraCorpusReader


if __name__ == '__main__':
	opts = docopt(__doc__)

	# load the data
	corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/')
	sents = list(corpus.tagged_sents())

	# Counter of words and of tags.
	words_dic = defaultdict(int)
	tags_dic = defaultdict(int)
	# The following is needed for counting words associated to a certain tag, 
	# and when computing tags ambiguity.
	tags = dict()
	words = dict()

	for s in sents:
		for w in s:
			# w is a pair containing the token and its tag.
			(word, tag) = w
			words_dic[word] += 1
			tags_dic[tag] += 1
			if (not word in words.keys()):	
				words[word] = defaultdict(int)
			if (not tag in tags.keys()):
				tags[tag]  = defaultdict(int)

			words[word][tag] += 1
			tags[tag][word] += 1

	# compute and print the statistics
	print("Number of sents: " + str(len(sents)))
	# tokens_number is the number of tokens and also the number of tags.
	tokens_number = sum(words.values())
	print("Number of words (tokens): " + str(tokens_number))
	print("Number of distinct words: " + str(len(words_dic)))
	print("Number of tags used: " + str(len(tags)))

	# First, sort the dictionaries associated to each tag.
	first_10 = sorted(tags_dic.items(), key=lambda x: (-x[1], x[0]))[:10]
	for (t, appear) in first_10:
		print("* \"" + str(t) + "\" appears " + str(appear) + " times " 
			" in the corpus (" + str(appear / float(tokens_number)) + "%).")
		print("\tMost frequent words associated to this tag are:")
		first_5 = sorted(tags[tag].items(), key=lambda x: (-x[1], x[0]))[:5]
		for (t2, appear2) in first_5:
			print("\t\"" + str(t2) + "\" (" + str(appear2) + " times -" + \
				str(appear2 / float(appear)) + "% of the tag-).")

	# MISSING: Ambiguity levels of words.
