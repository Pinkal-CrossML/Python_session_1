"""
In this file we discuss how to create
function and *args
"""

# how to create function an call function
def print_Name(a):
    print("Hello world" + b)


b =" pinkal"
print_Name(b)


# create function with *args
def add_value(*args):
    l = []
    for value in args:
        l.append(value)

    return l


result = add_value(100,200,300,400,500)
print(result)

result = add_value(100,200)
print(result)













