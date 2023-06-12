import sys
import os

from problem06 import is_valid_math_expr

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

input01 = sys.argv[1]


print(is_valid_math_expr(input01))  # Output: False
