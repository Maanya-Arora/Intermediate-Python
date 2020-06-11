total_sum = 0
num=0
while True:
    numbers = (input("enter your number (type STOP to stop entering numbers):"))
    if numbers == "STOP":
        break
    else:
        total_sum += float(numbers)
        num += 1

avg = total_sum/num
print('average of the numbers is :', avg)