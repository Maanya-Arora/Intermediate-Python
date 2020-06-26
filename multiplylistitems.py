mylist = []
for i in range(0,10):
    mylistinput = (input("enter 10 items:"))
    mylist += mylistinput
print("this is your list:" , mylist)
multiplied = 1
for i in mylist:
    multiplied = multiplied * int(i)
print("this is the product of all the items in your list:" , multiplied)
