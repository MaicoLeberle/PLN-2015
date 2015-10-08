from collections import defaultdict
class BaselineTagger:

	def __init__(self, tagged_sents):
		"""
		tagged_sents -- training sentences, each one being a list of pairs.
		"""
		# Counter of words and of tags.
		words = dict()
		tags = dict()

		for s in tagged_sents:
			for w in s:
				# w is a pair containing the token and its tag.
				(word, tag) = w
				if (not word in words.keys()):
					words[word] = defaultdict(int)
				if (not tag in tags.keys()):
					tags[tag] = defaultdict(int)
				# Increment word's tag counter, so then the tag assigned to a word
				# past to self.tag_word(...) is the most frequent tag seen in the 
				# training corpus for that word.
				words[word][tag] += 1
				tags[tag][word] += 1

		# Now, for each word in self.words, sort the tags they have been assigned 
		# with and select the most seen tag as the one that should be returned from
		#  self.tag_word(...). Store the results in self.words.
		self.words = dict()
		for w in words.keys():
			self.words[w] = sorted(words[w].items(), key=lambda x: x[1])[0][0]
	
		# Store most seen tag in the corpus.
		cur_count = 0
		prev_processing = dict()
		self.most_seen_tag = ''
		for t in tags.keys():
			prev_processing[t] = 0
			for w in tags[t].keys():
				prev_processing[t] += tags[t][w]
			# Now check if t represents the maximum so far.
			if (prev_processing[t] > cur_count):
				cur_count = prev_processing[t]
				self.most_seen_tag = t
		assert(self.most_seen_tag != '')

	def tag(self, sent):
		"""Tag a sentence.

		sent -- the sentence.
		"""
		return ([self.tag_word(word) for word in sent])

	def tag_word(self, w):
		"""Tag a word.

		w -- the word.
		"""
		if (w in self.words.keys()):
			# self.words[w] contains the most seen tag for such a word.
			return (self.words[w])
		else:
			# Assignment specifies the following is what should be returned
			# in such a case.
			return (self.most_seen_tag)

	def unknown(self, w):
		"""Check if a word is unknown for the model.

		w -- the word.
		"""
		return (not w in self.words.keys())
