"""
description
In this Python file we will discuss python data type
like list(), tuple() and  dictionary() with built-in methods.
"""
# Python List and built-in methods
student_name = ["Pinkal", "Aman", "Pooja", "Jaspreet"]
student_age = [23, 24, 20, 24]

cars_price = {
    "bmw": 100000,
    "volvo": 45000,
    "ford": 28000
}

# append() function
student_name.append(student_age)
print(student_name)

# extend()function
student_name.extend(student_age)
print(student_name)

# clear()function
student_age = [23, 24, 20, 24]
student_age.clear()
print(student_age)

# count()function
student_name = ["Pinkal", "Aman", "Pooja", "Jaspreet"]
student_name.count("Pinkal")
print(counts)

# insert()function
student_name = ["Pinkal", "Aman", "Pooja", "Jaspreet"]
student_name.insert(1,"Suraj")
print(student_name)


# pop()function
student_name = ["Pinkal", "Aman", "Pooja", "Jaspreet"]
student_name.pop()
print(student_name)

# reverse()function
student_name = ["Pinkal", "Aman", "Pooja", "Jaspreet"]
student_name.reverse()
print(student_name)


# sort()function
student_age = [23, 24, 20, 24]
student_age.sort()
print(student_age)

# TODO: Python Dictionaries and built-in methods
# get()function and len() function
cars_price = {
    "bmw": 100000,
    "volvo": 45000,
    "ford": 28000
}
car = cars_price.get("bmw")
print(cars_price["volvo"])
print(car)
print(len(cars_price))

# keys() and values() method
cars_price = {
    "bmw": 100000,
    "volvo": 45000,
    "ford": 28000
}
car = cars_price.keys()
car = cars_price.values()
car = car

# Change Values()
cars_price = {
    "bmw": 100000,
    "volvo": 45000,
    "ford": 28000
}

cars_price["bmw"] = 300000
print(cars_price)

# Adding Items
cars_price["Thar"] = 300000
print(cars_price)


# : Python Tuple and built-in methods
week_days = ("sunday","Monday", "Tuesday","wednesday",)

# Tuple index() Method
week = week_days.index("Tuesday")
print(week)
