mylist = []
for i in range(0,10):
    theinput = (input("enter an item:"))
    mylist.append(theinput)

mylist.sort()
print("the minimum is:", mylist[0])
print("the maximum value is:", mylist[9])

