x = 0
num1 = 0
num2 = 1

while(x <= 101):
    if(x <= 1):
        newx = x
    else:
        newx = num1 + num2
        num1 = num2
        num2 = newx
    
    if x == 100:
        print(newx)
    x = x + 1
    
