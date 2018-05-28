import re


class Calculator:
    pass

def add(string):
    result = 0
    integer_list = re.findall(r'\d+', string)
    y = list(map(int, integer_list))
    for item in integer_list:
        result = result + item
    return result
