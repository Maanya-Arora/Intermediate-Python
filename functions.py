#functions ---> xyz()
#xyz(value)
# inbuilt, define

def printStatement():
    print("I am in 8th grade.")
printStatement()

def printcolor(color):
    print(color)

printcolor("green")

def avrg(grades):
    sum = 0
    for item in grades:
        sum_ = sum+item
    avg = sum_/2
    print(avg)

maanya= [100, 100, 98, 97, 11, 79]
emily = [100, 98, 99, 78, 13, 80]
print("maanyas average")
avrg(maanya)
print("emilys average")
avrg(emily)

def myfriends(*friends):
    print("my friends are-")
    print(friends[0])
    print(friends[1])

myfriends("emily","bofa")

def default(name = "maanya"):
    print(name)

default()
default("emily")