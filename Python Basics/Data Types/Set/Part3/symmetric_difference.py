"""
set.symmetric_difference(^):

Returns a new set with elements that are in either of the sets, 
but not both(Removes the common elements.)
"""

setA = {1, 2, 3, 4, 5, 6, 7, 8}
setB = {1, 3, 5, 6, 7, 8, 9}

#Find symmetric difference of setA and setB

symm_diff = setA.symmetric_difference(setB) #Other method -> symm_diff = setA ^ setB

#Print values 
print("SetA = ",setA)
print("SetB = ", setB)

print("SetA ^ setB = ", symm_diff)