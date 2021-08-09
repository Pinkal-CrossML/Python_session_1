"""
In this file we discuss how to create
class, call the class and with is __init__ and __add__
and class variable
"""

# in this calss we discuss how to create class, call the class, methods  and __init__()
class Car():
    modelname= ""
    year = ""
    price = ""

    def __init__(self, modelname, year, price):
        self.modelname = modelname
        self.year = year
        self.price = price


honda = Car('city', 2017, 10000)
tata = Car('bolt', 2016, 60000)

print(tata.price)


# in this calss we discuss what CLASS VARIABLE
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.id = first + last + '@gmail.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1=Employee('pinkal', 'sanoria',50000)
emp2=Employee('shivam', 'rana',60000)

emp1.appy_raise()
print(emp1.pay)



# how to  Add tow objects
class A:
    def __init__(self, a):
        self.a = a

    def disp(self):
        return self.a

    def __add__(self, param):
        return A(self.a + param.a)


obj1 = A(5)
obj2 = A(2)


c = obj1 + obj2
print(c.disp())