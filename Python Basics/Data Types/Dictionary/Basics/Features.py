
my_car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Ordered (>=3.7)
print(my_car)

#Mutable
my_car["year"] = 2005
my_car.pop("model")
print(my_car)

#No Duplicates
my_car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":2005
}
#Year Key repeated twice
print(my_car)

