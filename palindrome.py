mystring = input("enter your string:")
length = len(mystring)
reversedstring = mystring[length :: -1]
if reversedstring == mystring:
    print("this string is a palindrome")
else:
    print("this string is not a palindrome")