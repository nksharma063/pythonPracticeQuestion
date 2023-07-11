"""
*args wil help us to uncover the list of values , but remeber it always take inut as Tuple and uncover any values under it

Creating a loop oevr all uncovered numbers from the tuple and passing the modulus consition whether number divided by 2 will give us the remiander of 0 or not

I could have printed the number to console but i am returning the output as True or False to return the value for further use
"""

def evenOdd(*args):
    for each in args:
        if each % 2 == 0:
            return True
            # print(f"{each} is Even Number")
        else:
            # print(f"{each} is Odd Number")
            return False
    
evenOdd(1,2,3,4,5,6)
