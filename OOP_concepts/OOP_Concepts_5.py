# This file contains examples related to Special Methods (Magic/Dunder)

# These special methods emulate some built-in behaviour within Python
# It is also how we implement operator overloading

# These special methods are always surrounded by double underscore

"""
When str is called without it being implemented then it uses repr as a fallback function, hence having atleast repr is
recommended
"""

"""
repr & str functions are used to change the way how the Objects are printed / displayed
"""

# there are lot of special methods to perform arithmetic, compare objects.
# Refer the documentation link: https://docs.python.org/3/reference/datamodel.html#special-method-names for more info


# Example 5

class Employee:
    raise_amount = 1.04  # This is a class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # keeping this as self.raise_amount gives flexibility to modify it for particular instance
        # instead of Employee.raise_amount
        # this allows even the sub-class to override the raise_amount later
        self.pay = self.pay * self.raise_amount

    # It is an unambiguous representation of the Object
    # It should be used for debugging & logging, it is for the Developer
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # It is used for readable representation of an Object, it is for the end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.mail)

    # Here self is the left argument and other is the right argument of + operator
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Test', 'User', 5000)
emp2 = Employee('Nikhil', 'Sekaran', 1000)

# here for integers '+' does Addition, for Strings does string concatenation
print(1 + 2) # int.__add__() is used in the background
print('a' + 'b') # str.__add__() is used in the background

# this prints "<__main__.Employee object at 0x00000299FD8FEF98>" this if __repr__ and __str__ function is not implemented
print(emp1)

# print on objects uses __repr__ function if implemented, it uses __str__ if both repr and str are available

print(repr(emp1)) # prints "Employee('Test', 'User', '5000')"
print(str(emp1)) # prints "Test User - Test.User@company.com"

# Line 70 and 71 are same as the below two lines
print(emp1.__repr__())
print(emp1.__str__())

# This print throws an Error "TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'" if __add__
# is not available as it does not know how to add the objects of Employee class
print(emp1 + emp2)

print(len("test")) # print("test".__len__()) is used in the background

# This print throws an Error "TypeError: object of type 'Employee' has no len()" if __len__ is not available
# as it does not know how to find the len on the objects of Employee class
print(len(emp1))