"""
dict[‘key’] = ‘value’
If the 'key' already exists, this will update its value.
If the 'key' doesn't exist, this will create a new key-value pair.
"""
person = {
    'id' : 1020,
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

person["age"]= 25

print(person)


