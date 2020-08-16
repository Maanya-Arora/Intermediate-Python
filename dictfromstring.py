string = input("enter your string:")
mydictionary = {}
for i in string:
    mydictionary[i] = mydictionary.get(i, 0) + 1
print(mydictionary)