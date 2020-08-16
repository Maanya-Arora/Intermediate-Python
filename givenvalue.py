dictionary = {'4':'5','8':'3','9':'12','0':'1','18':'19'}
print(dictionary)
value = (input("which value do you want to check for:"))
if value in dictionary.values():
    print("the given value has been found")
else:
    print("the given value was not found")
