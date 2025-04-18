"""
set.intersection(&):

Returns a new set with elements common to all sets.
"""

setA = {1, 2, 3, 4, 5}
setB = {1, 3, 9, 12}

#Perform intersection of setA and setB

intersection = setA.intersection(setB) # other method -> intersection = setA & setB

#Print values 
print("SetA = ",setA)
print("SetB = ", setB)

print("SetA ∩ setB = ", intersection)