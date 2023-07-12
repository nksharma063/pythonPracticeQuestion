def squareRoot(*args):
    squareRoot = []
    for each in args:
        squareRoot.append(each**(1/2))
    return squareRoot


print(squareRoot(4,9,5,2,144,244,225,12.5))