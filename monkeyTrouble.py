def monkey(smile1, smile2):
    if smile1 == True and smile2 == True:
        print("True")
    elif smile1 == False and smile2 == True:
        print("False")
    elif smile1 == True and smile2 == False:
        print("False")
    elif smile1 == False and smile2 == False:
        print("True")
    else:
        print("i could not understand your input")
monkey(False,False)