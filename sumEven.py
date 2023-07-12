def sumEven(*args):
    sum = 0
    extendedList = []
    for each in args:
        extendedList.extend(each)
    
    for each in extendedList:
        if each % 2 == 0:
            sum += each
        else:
            continue
    return sum    
print(sumEven([1,2,3,4,5, 6], [1,2,3,4,5, 6]))