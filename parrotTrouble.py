def parrot(talking, hour):
    if talking == True and hour < 7:
        print("True")
    elif talking == True and hour > 20:
        print("True")
    elif talking == True and hour < 20:
        print("False")
    elif talking == True and hour > 7:
        print("False")
    elif talking == False and hour >= 0:
        print("False")
    else:
        print("i could not understand your input")
parrot(True, 8)