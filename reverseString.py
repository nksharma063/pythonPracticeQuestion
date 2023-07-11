def abc(**kwargs):
    for key, value in kwargs.items():
        reverseString = value[::-1]
        print("the reverse string for {} is {}".format(value,reverseString))
        continue

print(abc(name_1="Hello", name_2="World"))    


