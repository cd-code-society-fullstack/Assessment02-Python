def is_valid_math_expr(s):
    operators = set(['+', '-', '*', '/'])
    s = s.replace(' ', '')  # remove spaces
    # check for operator at the beginning or end
    if s[0] in operators or s[-1] in operators:
        return False
    # check for two operators in a row
    for i in range(len(s) - 1):
        if s[i] in operators and s[i + 1] in operators:
            return False
    # check for division by zero
    if '/0' in s:
        return False
    try:
        eval(s)  # try to evaluate the expression
    except:
        return False  # if there is an error, it's not a valid expression
    return True

print(is_valid_math_expr("(1+2)*(3/4)"))  # Output: True
print(is_valid_math_expr("1+2*3/4"))  # Output: True
print(is_valid_math_expr("1++2*3"))  # Output: False
print(is_valid_math_expr("10/0"))  # Output: False
