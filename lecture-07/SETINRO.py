setA = {1,2,3,4}
setB = set([8,9,10])

setA.add(5)
setB.update([6,7])
Uset = setA | setB
print(Uset)
print(len(Uset))

setB.update('ABCD')
setA.update([6,7,8])
print(setB)

print(setA.intersection(setB))
print(setA )
