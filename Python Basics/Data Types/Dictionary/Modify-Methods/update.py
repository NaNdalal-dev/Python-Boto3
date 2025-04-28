"""
dict.update():
Adds or updates key-value pairs from another dictionary.
"""
person = {
    'id' : 1020,
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

person.update({"city":"LA"})

print(person)


