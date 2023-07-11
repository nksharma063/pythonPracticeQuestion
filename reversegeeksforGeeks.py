def reverse(s):
    str = ''
    for i in s:
        print(i)
        str = i + str
        print(str)
    return str

s = "Geeks"

print(s)
print(reverse(s))
