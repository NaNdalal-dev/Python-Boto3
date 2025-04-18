"""
set.discard():

The discard() method removes the specified item from the set.
Difference between remove and discard is, discard will not throw an error if an item
does not exist.
"""

my_set = {1,2,3}

my_set.discard(9)

print(my_set)