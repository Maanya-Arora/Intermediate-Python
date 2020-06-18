listoutput = []
n = int(input("how many elements do you want your list to have:"))
for i in range(n):
    listinput = (input("enter an item:"))
    listoutput.append(listinput)


listoutput.insert(n+1, "38")
listoutput.insert(0,"36")
listoutput.sort()
listoutput.extend("4")

for i in listoutput:
    print(i)

print(listoutput)
