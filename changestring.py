string = input("enter your string:")
firstchar = string[0]
lastchar = string[-1]
newstring = string.replace(string[0], "")
newstring1 = newstring.replace(string[-1], "")
newstring2 = lastchar + newstring1 + firstchar
print("your new string is:",newstring2)