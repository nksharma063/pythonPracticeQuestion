import statistics
def average(*args):
    count = 0
    sum = 0
    for each in args:
        sum = sum + each
        count +=1
    return sum/count

print(average(1,2,3,4,5))

print(statistics.mean([1,2,3,4,5]))