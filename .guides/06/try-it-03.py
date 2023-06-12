import sys
import os

from problem06 import is_valid_math_expr
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

print(is_valid_math_expr("1++2*3"))  # Output: False

