import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem03 import count_word_frequency


string = sys.argv[1]

print(count_word_frequency(string))  
