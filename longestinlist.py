listlength = int(input("enter the number of items in your list:"))
mylist = []
word = ("")
for i in range(0,listlength):
    listitems = input("enter your word:")
    mylist.append(listitems)
    if len(listitems) > len(word):
        word = listitems
print("in this list",mylist,", the longest word is:",word,", and it has a length of:",len(word))
