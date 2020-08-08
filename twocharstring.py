mystring = input("enter a string:")
if len(mystring) < 2:
    print("empty string")
else:
    newstring = mystring[0:2] + mystring[-2::]
    print("this is your new string, made of the first and last two characters of your original string:",newstring)