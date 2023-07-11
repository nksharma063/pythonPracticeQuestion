def sum(*args):
    sum = 0
    for each in args:
        sum+= each
    return sum

print(sum(1,2,3,4,5))