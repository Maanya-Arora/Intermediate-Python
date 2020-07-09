import random

print("hi, welcome to rock, paper, scissors!")
usermove = int(input("enter 1 if you would like to play rock, 2 for paper, and 3 for scissors:"))

mymove = random.randint(1,3)

if usermove == 1 and mymove == 1:
    print("it looks like i picked rock, too! it's a tie :)")
elif usermove == 1 and mymove == 2:
    print("i picked paper, I WIN! better luck next time!")
elif usermove == 1 and mymove == 3:
    print("woohoo, YOU WIN, since i picked scissors! don't worry, i'll beat you next time for sure!")

elif usermove == 2 and mymove == 1:
    print("woohoo, YOU WIN, since i picked rock! don't worry, i'll beat you next time for sure!")
elif usermove == 2 and mymove == 2:
    print("i picked paper, too! it's a tie :)")
elif usermove == 2 and mymove == 3:
    print("i picked scissors, I WIN! better luck next time!")

elif usermove == 3 and mymove == 1:
    print("i picked rock, I WIN! better luck next time!")
elif usermove == 3 and mymove == 2:
    print("woohoo, YOU WIN, since i picked paper! don't worry, i'll beat you next time for sure!")
elif usermove == 3 and mymove == 3:
    print("i picked scissors, too! it's a tie :)")