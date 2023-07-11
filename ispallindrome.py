def isPallin(**kwargs):
    for key,value in kwargs.items():
        reverseeach = value[::-1]
        if value == reverseeach:
            print(f"the value of {value} is {reverseeach}")
            print("the values are pallin whatever")
        else:
            print(f"the value of {value} is {reverseeach}")
            print("Strings are not pallindrome")
print(isPallin(name = "abba", name1 = "dbbd",  name2 = "12dgh", name3 = "jabba"))


"""
We can also try with taking input as string and iteraing over charcter, append to list and then compare both otr anyother data type if suits teh condition

We can also do temp storage and nce comparison done, remove from the list 
"""
