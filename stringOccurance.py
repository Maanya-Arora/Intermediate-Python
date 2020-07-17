stringa = input("enter your string:")
letter = input("what letter do you want to check for:")
x = 0
for item in stringa:
    if letter == item:
        x += 1
    else:
        x = x
if x > 1:
    print("the letter",letter,"appears", x,"times")
else:
    print("there are no occurances of the letter",letter,"in your string")