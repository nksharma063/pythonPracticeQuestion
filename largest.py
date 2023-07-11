def maxiMum(*args):
    numberList = list(args)
    temp = []
    for i in range(len(args)-1):
        if numberList[i] <= numberList[i+1]:
            temp = numberList[i+1]
            print(temp)
        else:
            continue
        
    
        
            
        

print(maxiMum(21,24,54,66,76))



""""
We can use sort, ascending number, max fucntion to get the values asap
like convert to list and fetch the last value throygh slicing , or max fucnction from math library or , create ascending number and do the same thing as sort
"""



