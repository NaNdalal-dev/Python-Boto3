"""
set.union(|):

Combines all unique elements from two or more sets.
"""

setA = {2, 5, 7}
setB = {1, 2, 5, 8}

#Perform union of setA and setB
union = setA.union(setB) # Other methods -> union = setA | setB

#Print values 
print("SetA = ",setA)
print("SetB = ", setB)

print("SetA U setB = ", union)
