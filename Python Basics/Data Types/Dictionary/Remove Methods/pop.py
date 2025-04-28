"""
dict.pop():

Removes the key and returns its value.
Raises error if key not found.
"""

person = {
    'id' : 1020,
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

person.pop("age")

print(person)
