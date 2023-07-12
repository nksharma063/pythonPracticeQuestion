def SI(*args):
    print("Please enter principal, rateofinterest, time in year")
    principal, rateofinterest, time = args
    rateofinterest = (rateofinterest/100)/12
    time = time * 12
    si = principal * rateofinterest * time
    return si

print(SI(15000,13,1))
