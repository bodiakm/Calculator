class Calculator:
    pass

def add(*args):
    result = 0
    for arg in args:
        result = result + int(arg)
    return result
