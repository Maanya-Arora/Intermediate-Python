mylist = []
Sum = 0
n = int(input("how many numbers do you want your list to have:"))
for i in range(n):
    listinput = int(input("enter an item:"))
    mylist.append(listinput)
    Sum = mylist[i] + Sum
average = (Sum/n)
print("this is your list:" ,mylist)
print("the average of the numbers in your list is:", average)




