def vowels(**kwargs):
    for key,value in kwargs.items():  #Iterating to all item and values provided as input usin item()
        # print(value)
        # for each in 
        # print(type(value))
        count = 0
        for each in str(value): # type casting so that funnction llike lower and comparison will be better 
            each = each.lower()
            print(each, type(each))
            if each == 'a' or each == 'e' or each == 'i' or each == 'o' or each == 'u':
                count = count + 1
            else:
                pass
    return count 


        # return count  This was mistake as i was not getting the correct output as desired becasue loop just iterating over one value.


print(vowels(item = "aeiou", item1 = "mynameisneEraj"))     