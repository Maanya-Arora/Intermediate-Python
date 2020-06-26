mylist = []
for i in range(0,10):
    mylistinput = (input("enter 10 items:"))
    mylist += mylistinput
print("this is your list:" , mylist)
print("the smallest number in your list is:", min(mylist))
print("the largest number in your list is:", max(mylist))