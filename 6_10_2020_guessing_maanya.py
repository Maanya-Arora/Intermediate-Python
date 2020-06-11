guess = 7
for i in range (0,6):
    guesses = (input("try guessing my number (it is between 1 and 20)! you have 6 tries:"))

    if (guesses == "6" or guesses == "8"):
        print("you got this! you're only off by a number")
    elif (guesses > "4"):
        print("aim higher")
    elif (guesses < "10"):
        print("aim lower!")
    elif guesses == "7":
        print("well guessed!")