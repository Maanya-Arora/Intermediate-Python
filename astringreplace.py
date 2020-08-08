string = input("enter your word:")
length = len(string)
if string[0] == "s":
    string = string[1:length]
    newstring = string.replace("s","$")
    newstringtwo = ("s" + newstring)
    print(newstringtwo)
else:
    newstring = string.replace("s","$")
    print(newstring)