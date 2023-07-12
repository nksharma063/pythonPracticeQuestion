def unpacking(*args):
    list = []
    for each in args:
        list.append(sorted(each))
    return list

print(unpacking([2,1,4,5], [1,2,7,6,5]))    