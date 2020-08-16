dictExample1 = {"maanya":"arora","emily":"le"}
print(dictExample1)
print(type(dictExample1))
print(dictExample1["maanya"])
print(dictExample1.get("emily"))

if "maanya" in dictExample1:
    print("maanya is in this dictionary")

if "emily" not in dictExample1:
    print("emily is not in this dictionary")
else:
    print("emily is in this dictionary")

for name in dictExample1:
    print(name)
for name in dictExample1:
    print(dictExample1[name])

for key,value in dictExample1.items():
    print(key,value)

print(len(dictExample1))

for lastnames in dictExample1.values():
    print(lastnames)

dictExample1["maanya"] = "8th grader"
dictExample1["emily"] = "also 8th grader"
print(dictExample1)

dictExample1["bofa"] = "another 8th grader"
print(dictExample1)

dictExample2 = {1:"red",2:"orange",3:"yellow"}
print(dictExample2[2])

dictExample1.pop("bofa")
print(dictExample1)

dictExample2.popitem()
print(dictExample2)

del dictExample2[2]
print(dictExample2)

#dictExample2.clear()
#print(dictExample2)

#del dictExample2
##print(dictExample2)
#will print an error ^^

dictExample2 = dictExample1
print(dictExample2)

dictExample1["maanya"] = "jh asb secretary"
print(dictExample2)

#dictExample2 = dictExample1.copy() WOULD NOT CHANGE BOTH VALUES --
dict1 = {1:"hi",2:"hello"}
dict2 = dict1.copy{}
print(dict2)
dict1[1] = "hey"
print(dict1)
print(dict2)

#HW
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Write a Python program to create a dictionary from a string. 
#Note: Track the count of the letters from the string.
#Sample string : 'w3resource'
#Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

#Write a function that prints the following -  
#{'one': 'uno', 'two': 'dos', 'three': 'tres', ‘four’:’quatro’, ’five’: ‘cinco’}

#+ more to come
