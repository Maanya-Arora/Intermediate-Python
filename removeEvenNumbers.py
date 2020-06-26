listoutput = [1,2,3,4,5,66,47,23,56,7,99,100]
print("this is your list:", listoutput)
for i in listoutput:
    if(int(i)%2==0):
        listoutput.remove(i)
print("your list without the even numbers is:",listoutput)
