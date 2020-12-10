over10Error = "Input more than 10"
divisionByZero = "Error division by zero!"

def add(*arg):
    if(len(arg) > 10):
        result = over10Error
        return result
    result = 0
    for n in arg:
        result = result + n
    return result


def subtract(*arg):
    if(len(arg) > 10):
        result = over10Error
        return result
    result = arg[0]
    for n in range(1, len(arg)):
        result = result - arg[n]
    return result

def multiply(*arg):
    if(len(arg) > 10):
        result = over10Error
        return result
    result = arg[0]
    for n in range(1, len(arg)):
        result = result * arg[n]
    return result

def divide(*arg):
    if(len(arg) > 10):
        result = over10Error
        return result
    result = arg[0]
    try:
        for n in range(1, len(arg)):
            result = result / arg[n]
    except ZeroDivisionError:
        result = divisionByZero

    return result