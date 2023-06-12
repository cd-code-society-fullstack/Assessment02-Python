import sys
import os
from problem05 import are_strict_sentences_anagrams
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


print(are_strict_sentences_anagrams("Hello, world!", "Howdy, partner!"))  # Output: False
