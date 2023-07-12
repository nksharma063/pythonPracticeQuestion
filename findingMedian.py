import statistics

def meedian(*args):
    for each in args:
        print("median  for each input is ",statistics.median(each))



print(meedian([1,2,3,4,5,6], [1,2,3,4,5,6,7]))


"""
i know, it can be done through iterating element, count the total, if even then divide length into half and take average of them, and if odd then take middle one
but viola we have rich statistics library

"""