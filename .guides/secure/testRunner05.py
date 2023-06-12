import sys
import os

from problem05 import are_strict_sentences_anagrams
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

input01 = sys.argv[1]
input02 = sys.argv[2]

print(are_strict_sentences_anagrams(input01, input02))  

