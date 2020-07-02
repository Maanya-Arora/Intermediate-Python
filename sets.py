firstSet = {"moon","sun","stars"}
print(firstSet)
firstSet.add("planets")
print(firstSet)
firstSet.update(["earth","mars"])
print(firstSet)
print(len(firstSet))
firstSet.remove("moon")
#firstSet.remove("moon") - prints error
print(firstSet)
firstSet.discard("moon")
print(firstSet)
firstSet.pop()
print(firstSet)
firstSet.clear()
print(firstSet)
del firstSet
#print(firstSet)

seta = {1,2,3}
setb = {4,5,6}
setc = seta.union(setb)
print(setc)
setd = {6,7,8}
setc.update(setd)
print(setc)

newSet = set(("a","b","c"))
print(newSet)