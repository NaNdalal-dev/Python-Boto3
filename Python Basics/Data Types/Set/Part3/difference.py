"""
set.difference(-):

Returns a new set with elements that are only in the first set, not in the other(s).
"""

setA = {2, 3, 4, 5, 6, 7}
setB = {3, 5, 7, 9, 11, 13}

#Find difference of setA and setB

diff = setA.difference(setB) #Other method -> diff = setA - setB

#Print values 
print("SetA = ",setA)
print("SetB = ", setB)

print("SetA - setB = ", diff)
