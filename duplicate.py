listA = ['1', '2', '3', '1', '5', '8', '3']

nonDuplicateList = []
for i in (listA):
    if i not in (nonDuplicateList):
        nonDuplicateList.append(i)
print(nonDuplicateList)