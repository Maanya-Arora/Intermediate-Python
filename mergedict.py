dictionary = {4:5, 8:3, 9:12, 0:1, 18:19}
dictionary2 = {8:11, 7:35, 92:12}
print(dictionary)
print(dictionary2)
dictionary3 = dict(dictionary)
dictionary3.update(dictionary2)
print(dictionary3)