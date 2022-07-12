# This file contains examples related to classmethods & staticmethods

# Regular instance methods takes instance as first argument automatically

# Class methods takes class as first argument automatically

# class methods can be called using the instances but there is no use of it and it is not good to do it
# class methods are used as alternative for constructors - to create different objects

# "cls" is common convention followed for "class object" which is similar to "self" for instance

# real time example of class methods used as alternative constructor is in datetime.py module

# Static methods don't take any argument automatically, but its defined within a class
# Static methods don't operate on a class or instance

# when instance information or class information is not used in your function then define that function as staticmethod

# Example 3


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

    @classmethod # this is a decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative constructor
    @classmethod
    # usually the method name starts with from, its just a convention
    def from_string(cls, emp_str):
        # splitting the string here
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Test', 'User', 5000)
emp2 = Employee('Nikhil', 'Sekaran', 1000)

# this function call does the same as Employee.raise_amount = 1.05
Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str_1 = 'Vikkram-Ravi-10000'
emp_str_2 = 'Vidya-Kamath-8000'
emp_str_3 = 'Princy-Babu-6000'

# # splitting the string here
# first, last, pay = emp_str_1.split('-')
# new_emp1 = Employee(first, last, pay)

# line 77, 78 is combined and done using from_string class method, which acts like alternative constructor
new_emp1 = Employee.from_string(emp_str_1)

print(new_emp1.mail)
print(new_emp1.pay)

import datetime
my_date = datetime.date(2019, 8, 31)

print(Employee.is_workday(my_date))