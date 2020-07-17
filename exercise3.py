item = input("enter your word:")
if len(item) <= 3:
    print("sorry, try again")
else: 
    item2 = item[0:2] + item[-2:]
    print("this is your new string:", item2)

