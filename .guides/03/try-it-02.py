import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem03 import count_word_frequency


print(count_word_frequency("This is a test. This is only a test."))  # Expected: { "this": 2, "is": 2, "a": 2, "test": 2, "only": 1 }
