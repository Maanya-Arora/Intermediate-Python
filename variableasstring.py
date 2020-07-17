x = ("hello")
print(x)
#x[2] = ("hi")
#print(x)
print(x[2])
print(x[-1])
print(x[1:3])
print(x[-3:-1])
print(" ")
print(chr(83))
print(chr(13))
print(chr(118))
print("")
print(ord('X'))
print(ord('V'))
print(ord("@"))
print(ord('$'))
print(ord("#"))
print("")
print(len(x))
print(str(8.74))
y = ("hi")
newstring = x + y
print(newstring)
print(newstring * 2)
w = ("hey")
z = x + y + w
print(z)
print("")
print("")

stringg = ("HI")
string2 = ("hi")
print(stringg)
print(stringg.lower())
print(string2)
print(string2.upper())

print("")
stringagain = ("Ji")
print(stringagain)
print(stringagain.replace("J","H"))

print("")
stringa = "hi , bye"
print(stringa.split(","))

print("")
stringb = "  hi   "
print(stringb)
print(stringb.strip())


string1 = ("hello,hey")
print("hi" in string1)
print("hello" not in string1)

print("")
days = 31
text = ("January has this many days- {}" )
print(text.format(days))