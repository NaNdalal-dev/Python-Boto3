#1. Storing Data as Key-Value Pairs
user_profile = {
    "username": "coder123",
    "name": "Alice",
    "email": "alice@example.com",
    "age": 28
}

#2. Representing JSON Data
#(This is similar to how you'd receive data from a web API.)
api_response = {
    "status": "success",
    "data": {
        "id": 101,
        "title": "Learn Python",
        "price": 49.99,
        "tags": ["programming", "python", "coding"]
    }
}

#3. Grouping and Counting
#(Word frequency or item count in a list.)

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = dict(Counter(words))
print(word_count)

# Output: {'apple': 3, 'banana': 2, 'orange': 1}

#4. Switch/Case Alternatives
#(Using a dictionary to simulate switch-case.)

def add(): return 10+2
def subtract(): return 3-9
def multiply(): return 6*9

operations = {
    "add": add,
    "sub": subtract,
    "mul": multiply
}

print(operations["add"]())  # Output: 12
