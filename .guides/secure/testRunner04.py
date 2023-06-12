import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem03 import min_deletions


string = sys.argv[1]

print(min_deletions(string))  # Output: 3