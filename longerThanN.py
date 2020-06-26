listoutput = []
n = int(input("how many elements do you want your list of words to have:"))
for i in range(0,n):
    listinput = (input("enter an item:"))
    listoutput.append(listinput)
print('this is your list:', listoutput)
length = int(input("enter a length:"))
lengthofitem = 0
finallist = []
for item in listoutput:
    for letter in item:
        lengthofitem += 1
    if lengthofitem > length:
        finallist.append(item)
        lengthofitem = 0
    else:
        lengthofitem = 0
print("these are the words from your original list that are longer than", length,":" , finallist)        

