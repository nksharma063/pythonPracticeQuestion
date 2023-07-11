def Isprime(n):
    for each in range(2,n+1):
        if n == each:
            continue
        elif n % each == 0:
            return False
    return True
# print(Isprime(47))


def primeFilter(n):
    primeList = []
    for each in range(2, n+1):
        if each == 2:
            primeList.append(2)
        elif each % 2 != 0:
            primeList.append(each) 
            
    return primeList

def prime(n):
    prime = []
    for each in primeFilter(n):
        print("afterfilter",each)
        if Isprime(each):
            # print("Actual prime",each)
            prime.append(each)
    return prime

print(prime(20))        