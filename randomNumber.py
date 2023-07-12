import random

def randomNumber():
    number = int(input("Please enter the random number"))
    return random.randrange(number+1)  

print(randomNumber())