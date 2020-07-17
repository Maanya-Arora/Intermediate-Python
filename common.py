stringa = input("enter your first string:")
stringb = input("enter your second string:")  
commonlist = []
for i in stringa:
    for x in stringb:
        if i == x:
            commonlist.append(i)
if len(commonlist) > 0:
    print("these is at least one common character in your strings.")
else:
    print("there are no common characters in your strings.")
            
        