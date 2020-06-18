listoutput = []
n = int(input("how many numbers do you want your list to have:"))
for i in range(0,n):
    listinput = (input("enter a number:"))
    listoutput.append(listinput)
finalList = []
for i in listoutput:
    if int(i)%3==0:
        finalList.append(i)
print("the multiples of 3 from your list are:", finalList)
