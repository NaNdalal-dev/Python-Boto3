"""
dict.popitem()

Removes and returns the last key-value pair 
(Python >=3.7+).
"""

person = {
    'id' : 1020,
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

rm1 = person.popitem()
rm2 = person.popitem()

print(rm1)
print(rm2)

print(person)