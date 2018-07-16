# Course URL:
# https://deeplearningcourses.com/c/natural-language-processing-with-deep-learning-in-python
# https://udemy.com/natural-language-processing-with-deep-learning-in-python
from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
# Note: you may need to update your version of future
# sudo pip install -U future

import numpy as np

import os
import sys
sys.path.append(os.path.abspath('..'))
from brown import get_sentences_with_word2idx_limit_vocab, get_sentences_with_word2idx




if __name__ == '__main__':
  # load in the data
  # note: sentences are already converted to sequences of word indexes
  # note: you can limit the vocab size if you run out of memory
  sentences, word2idx = get_sentences_with_word2idx_limit_vocab(10000)
  # sentences, word2idx = get_sentences_with_word2idx()
  print(word2idx)