string = input("enter your string:")
if len(string) == 0:
    print("try again. your string has no characters.")
else:
    remove = int(input("enter a value for n, the index value:"))
    newstring = string.replace(string[remove], "")
    print("this is your new string:",newstring)