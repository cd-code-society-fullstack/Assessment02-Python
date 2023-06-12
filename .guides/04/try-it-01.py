import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem03 import min_deletions


print(min_deletions("abcba"))  # Output: 0