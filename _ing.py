string = input("enter a string at least 3 characters long:")
if len(string) < 3:
    print(string)
elif string[-3:] == "ing":
    suffix = "ly"
    print(string + suffix)
else:
    suffix = "ing"
    print(string + suffix)
