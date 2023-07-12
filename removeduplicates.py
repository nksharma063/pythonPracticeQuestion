def removeDuplicate(**Kwargs):
    mainList=[]
    for key,value in Kwargs.items():
        list = []
        for each in value:
            if each not in list:
                list.append(each)
            else:
                pass
        mainList.append(list)
    return mainList
print(removeDuplicate(item1=['23','23','21','24','24'], item2=["abc", "abc", "def"]))