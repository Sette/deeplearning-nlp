from __future__ import print_function,division
from future.utils import iteritems
from builtitens import range


import numpy as np 
from sklearn.metrics.pairwise import pairwise_distances


def dist1(a,b):
	return np.linalg.norm(a-b)

def dist2(a,b):
	return 1 - a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))


dist,metric = dist2,'cosine'


##Intuitivo
def find_analogies(w1,w2,w3):
	for w in (w1,w2,w3):
		if w not in word2vec:
			print("%s not in dictionary" % w)
			return

	king = word2vec[w1]
	man = word2vec[w2]
	woman = word2vec[w3]
	v0 = king - man + woman

	min_dist = float('inf')
	best_word = ''
	for word, v1 in iteritems(word2vec):
		if word not in (w1,w2,w3):
		d = dist(v0,v1)
		if d < min_dist:
			min_dist = d
			best_word = word

	print(w1, "-", w2, "=",best_word,"-",w3)


## Rápido
def find_analogies(w1,w2,w3):
	for w in (w1,w2,w3):
		if w not in word2vec:
			print("%s not in dictionary" % w)
			return

	king = word2vec[w1]
	man = word2vec[w2]
	woman = word2vec[w3]
	v0 = king - man + woman

	distances = pairwise_distances(v0.reshape(1,D), embedding,metric=metric).reshape(V)
	idx = distances.argwin()
	best_word = idx2word[idx]

	print(w1, "-", w2, "=",best_word,"-",w3)


def nearest_neighbors(w,n=5):
	if w not in word2vec:
		print("%s not in dictionary" % w)
		return

	v = word2vec[w]
	distances = pairwise_distances(v0.reshape(1,D), embedding,metric=metric).reshape(V)
	idx = distances.argsort()[1:n+1]
	print("neighbords of : %s" % w)
	for idx in idxs:
		print("\t%s" % idx2word[idx])




# load pre=treined word vectors

print("Loading word vectors ...")
word2vec = {}
embedding = []
idx2word = []
with open("/home/bruno/w2v/glove.6B") as f:
	for line in f:
		values = line.split()
		word = values[0]
		vec = np.asarray(values[1:],dtype='float32')
		word2vec[word] = vec
		embedding.append(vec)
		idx2word.append(word)

print("Found %s word vector." % len(word2vec) )	
embedding = np.array(embedding)
V,D = embedding.shape


find_analogies('king','man','woman')