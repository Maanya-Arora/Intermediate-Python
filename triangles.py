sideOne = int(input("enter the length of the first side of the triangle:"))
sideTwo = int(input("enter the length of the second side of the triangle:"))
sideThree = int(input("enter the length of the third side of the triangle:"))

if(sideOne == sideTwo and sideTwo == sideThree):
    print("all sides are equal, so this is an equilateral triangle.")
elif(sideOne==sideTwo or sideTwo==sideThree or sideThree==sideOne):
    print("this triangle is isoceles because only two sides are equal.")
else:
    print("no sides are equal, this is a scalene triangle.")