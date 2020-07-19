mystring = input("enter a string greater than 4 letters:")
newstring = mystring[0:2] + mystring[-2::]
print("this is your new string, made of the first and last two characters of your original string:",newstring)