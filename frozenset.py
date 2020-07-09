colors = ['red','blue','purple']
print(colors)
colors[1] = "green"
print(colors)
frozencolors = frozenset(colors)
print("since the list is now frozen, we cant change any of the items. the following code will lead to an error.")
frozencolors[2] = "red"