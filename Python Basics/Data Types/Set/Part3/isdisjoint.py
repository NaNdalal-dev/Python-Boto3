"""
set.isdisjoint():

Returns True if two sets have no common elements, otherwise return false.
"""

setA = {1, 2, 3}
setB = {5, 7, 9}

#Check if setA and setB are disjoint (no common elements)

isdisjoint = setA.isdisjoint(setB)

#Print values 
print("SetA = ",setA)
print("SetB = ", setB)

print("are SetA and setB disjoint sets:", isdisjoint)