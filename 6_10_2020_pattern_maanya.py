row = 5

for a in range(row):
    for b in range(0, a):
        print("*", end=" ")
    print("")

print("* * * * * ")

for i in range(row,0,-1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

#sorry, i didn't know how to do it with just one for loop
    
