# def getList(n):
#     rangeList = []
#     for each in range(n+1):
#         rangeList.append(each)
#     return rangeList

# def fin(n):
#     fibList = []
#     i = 0
#     while i <= n:
#         for each in getList(n):
#             item1 = each[i]
#             item2 = each[i+1]
#             fibList.append(item1 + item2)
#             i = i + 1
#     return fibList
    

# print(fin(20))


#     # for i in range(n+1):
#     #     list = each[i] + each[i+1]
#     #     list.append
# print(fib(20))          
def fib(n):
    count = 0
    num1 = 0
    num2 = 1
    print(num1, end=' ')
    print(num2, end=' ')
    while count <= n-1:
        num3 = num1 + num2
        print(num3, end=' ')
        num1 = num2
        num2 = num3
        count +=1
        continue

print(fib(20))


"""
We can search geekfor geek for storage efficent recursive manner for the same,
above soltion was also a bt of help from internet to get an idea about approach,
we are printing the first two elements as raw, and getting two global variable as num1 and num2.
we are running while loop till sequence but as we are printing two values upfron, we can reduce the while loop for 
below code.
then we are swicthing the numbers.

I APPROACHED IT , IT TOOK 4 HOURS, I WROTE 011235 AND THEN SWICTHED THE VARIABLES.

"""



