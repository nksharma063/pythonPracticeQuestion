def tempConverter(*args):
    # degList = list(args)
    celciusFehrentite = []
    for each in args:
        F = (each * 9/5) + 32
        celciusFehrentite.append(F)
    return {"the specific celcius to Fehrentite for {} are {}".format(args,celciusFehrentite)}

print(tempConverter(4,50.5,20,10))