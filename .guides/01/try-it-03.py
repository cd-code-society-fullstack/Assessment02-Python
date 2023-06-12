import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem01 import get_contents

print(get_contents("xxbreadyy", "bread"))  # Expected: "none"