"""
dict.setdefault("key","value")

Return the value of a key if it exists.
If the key doesn’t exist, it inserts the key with a default value and returns that value.
"""
person = {
    'id' : 1020,
    'name': 'John',
    'age': 30,
    'city': 'New York',
    "phone": 970178,
    "email":"John@mail.com"
}

person.setdefault("email","optional")

print(person)


