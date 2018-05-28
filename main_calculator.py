import re


class Calculator:
    pass

def add(string):
    result = 0
    extracted_numbers = re.findall(r'\d+', string)
    converted = list(map(int, extracted_numbers))
    for item in converted:
        result = result + item
    return result
