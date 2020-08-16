dictionary = {'4':'5','8':'3','9':'12','0':'1','18':'19'}
print(dictionary)
key = (input("which key do you want to check for:"))
if key in dictionary:
    print("the given key has been found")
else:
    print("the given key was not found")
