dictionary = {"data1":3, "data2":5, "data3":10}
num = 1
values = dictionary.values()
for i in values:
    num = i * num
print(num)
