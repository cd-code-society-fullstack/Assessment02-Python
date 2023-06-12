import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem03 import count_word_frequency


print(count_word_frequency("The quick brown fox, jumped over the lazy dog."))  # Expected: { "the": 2, "quick": 1, "brown": 1, "fox": 1, "jumped": 1, "over": 1, "lazy": 1, "dog": 1 }
