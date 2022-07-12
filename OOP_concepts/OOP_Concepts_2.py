# This file contains examples related to Class Variables

# Class variables are common to all instances
# Instance variables and Class variables differ. Both are not same

# __dict__ is used to get the namespace

"""
Scenario in which there is no idea of using self for a class variable is:
When we want to know the count of no of employees created for the below example
"""


# Example 2

class Employee:
    raise_amount = 1.04  # This is a class variable
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@company.com'
        self.pay = pay

        # Class variable always
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # keeping this as self.raise_amount gives flexibility to modify it for particular instance
        # instead of Employee.raise_amount
        # this allows even the sub-class to override the raise_amount later
        self.pay = self.pay * self.raise_amount


# Here the value is Zero
print(Employee.num_of_emps)

emp1 = Employee('Test', 'User', 5000)
emp2 = Employee('Nikhil', 'Sekaran', 1000)

# Here the value is Two
print(Employee.num_of_emps)

print(Employee.__dict__)  # here we can see raise_amount in the namespace

# in the below two prints we cannot see raise_amount in the namespace
print(emp1.__dict__)
print(emp2.__dict__)

print(Employee.raise_amount)  # Class variable

# when the raise_amount is printed, if it is not in its namespace then it fetches from the Class namespace
# that is the reason there is no error when we access raise_amount in the below prints
print(emp1.raise_amount)  # instance variable
print(emp2.raise_amount)

emp1.raise_amount = 1.05
# in the below print we can see raise_amount in the namespace as it is explicitly modified by emp1 instance
# in the above line
print(emp1.__dict__)

# now the change for raise_amount is applied only for emp1
# it can be verified by the below prints
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
