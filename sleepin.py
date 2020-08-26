def sleep(weekday, vacation):
    if weekday == True and vacation == True:
        print("True")
    elif weekday == False and vacation == True:
        print("True")
    elif weekday == True and vacation == False:
        print("False")
    elif weekday == False and vacation == False:
        print("False")
    else:
        print("i could not understand your input")
sleep(True,False)