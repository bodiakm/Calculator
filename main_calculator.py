import re


class Calculator:
    pass


def add(numbers):
    result = 0
    last_two = len(numbers) - 2

    # finds new line at the end of the string, returns -1 if there is none
    if numbers.find("\n", last_two) is not -1:
        raise ValueError('Newline present at the end of the string')
    else:
        extracted_numbers = re.findall('[-\d]+', numbers)
        converted_to_int = list(map(int, extracted_numbers))
        for i in converted_to_int:
            if i < 0:
                raise ValueError('Negative(s) in %s not allowed' % converted_to_int)
            elif 0 <= i <= 1000:
                result += i
    return result
