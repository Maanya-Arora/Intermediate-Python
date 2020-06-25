mytuple = ('hi','hello','hey','hola','namaste')
print(mytuple[3])

print(" ")
for i in mytuple:
    print(i)

print("")
if "hi" in mytuple:
    print("hi is in your tuple!")
else:
    print("hi is not in your tuple.")

print("")
a,b,c,d,e = mytuple
print(b)
print(e)

print("")
print(mytuple[1:3])

print("")
tuple2 = ('item1')
print(type(tuple2))
print(type(mytuple))
