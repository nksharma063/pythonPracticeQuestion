# def gettingList(**kwargs):
#     list = []
#     for key,value in kwargs.items():
#         list.append(value)

#     return list

# def commonCharacters(**kwargs):
#     commonItem = []
#     for each in gettingList(**kwargs):
#         i = 0
#         print(len(each[0]), len(each[1]))
#         while i < (len(each[0]) + len(each[1])):
#             if  each[i] not in commonItem:
#                 commonItem.append(each[i])
#                 i+=1
#     return commonItem

    #     set1 = kwargs[key]
    #     set2 = kwargs[key]
    #     print(set1,set2)


def gettingList(**kwargs):
    sets = []
    for key, value in kwargs.items():
        sets.extend(value)
    return sets

def commonCharacters(**kwargs):
    sets = gettingList(**kwargs)
    unique = []
    for each in sets:
        if each in unique:
            continue
        else:
            unique.append(each)
    return unique

print(commonCharacters(item1 = "abcdef", item2 = "bcdefg"))