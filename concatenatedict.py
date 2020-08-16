dict1={1:10,2:20}
print(dict1)
dict2={3:30,4:40}
print(dict2)
dict3={5:50,6:60}
print(dict3)
dict4 = dict(dict1)
dict4.update(dict2)
dict4.update(dict3)
print(dict4)