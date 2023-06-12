import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem01 import get_contents

string = sys.argv[1]
keyword = sys.argv[2]

print(get_contents(string, keyword))  # Expected: "none"