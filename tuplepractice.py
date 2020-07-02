mytuple = (1,2,3,4,7,6,7,8)
print(mytuple[1:4])
#mytuple[3] = ("hello")
#print(mytuple)
print("")
multituple = (1,2,3,4,[6,7])
multituple[4][1] = ("hi")
print(multituple)

atuple = (3,3,3,3,3,3)
newtuple = mytuple + atuple
print(newtuple)
#del newtuple
#print(newtuple)

print("")
print(mytuple.index(4))
print(mytuple.count(7))
print(9 in mytuple)
print("")
for i in mytuple:
    print(i)