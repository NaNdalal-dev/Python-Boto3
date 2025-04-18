"""
set.issuperset(>=):

Returns True if a set contains all elements of another set.
"""

setB = {1, 4, 8, 9, 11} #Superset
setA = {1, 9, 11} #Subset

#Check if setB is superset of setA

issup = setB.issuperset(setA) #Other method -> issup = setB >= setA

#Print values 
print("SetA = ",setA)
print("SetB = ", setB)

print("setA >= setB =", issup)