sUm = 0
n = 0
while n >= 0:
    n = (int(input("enter your number:")))
    sUm = sUm + n
    print(sUm)
    if (n<0):
        print("sorry, we can't keep on adding negative numbers :)")
        break
        