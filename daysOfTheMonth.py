month = input("enter the month:")
if(month == "february"):
    print("this month has either 28 or 29 days.")
elif(month == "april" or month == "june" or month == "september" or month == "november"):
    print("this month has 30 days.")
else:
    print("this month has 31 days.")