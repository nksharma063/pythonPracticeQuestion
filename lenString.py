def lenString(**kwargs):
    for key,value in kwargs.items():
        print(value, type(value))
        length = len(value)
        print(f"the length {key} is {length}")   # using the format fucntion and length fucntion to check the length of value provided in string

print(lenString(item1="abcdefg", item2="my name is")) 


"""
we can also iterate of each value or create two fucntion and povide input value to other fucntion and create count to determmine the length of the strig if , we want to avoid using len() for siplicaity 
"""
