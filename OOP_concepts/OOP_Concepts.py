# This file contains examples related to Classes & Instances

# To Define EMPTY CLASS
# class Test:
# pass

# always the instance of a class is passed as first argument to all functions

# __init__(self), here the instance is mapped as self,
# __init__ is mapped as constructor with c++ or other high level languages

# Example 1

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Test', 'User')
emp2 = Employee('Nikhil', 'Sekaran')

print(emp1.mail)
print(emp2.mail)

# Below two lines perform the same action
# which prints the full name
print(emp1.fullname())
print(Employee.fullname(emp1))

"""
If self is removed as first argument in the function definition and
emp1 is not passed in line 31, then interpreter throws an error as follows:
TypeError: fullname() takes 0 positional arguments but 1 was given"
Actually line 30 is converted to the same format as line 31 internally

Hence it is advisable to mention "self" as first argument in the method fullname even though line 30 does not throw error.
"""