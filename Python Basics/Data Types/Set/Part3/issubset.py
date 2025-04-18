"""
set.issubset(<=):

Returns True if all elements of one set are present in another.
"""

setB = {1, 4, 8, 9, 11} #Superset
setA = {1, 9, 11,} #Subset

#Check if setA is subset of setB

issub = setA.issubset(setB) #Other method -> issub = setA <= setB

#Print values 
print("SetA = ",setA)
print("SetB = ", setB)

print("setA <= setB =", issub)
