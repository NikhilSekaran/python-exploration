# This file contains examples related to Inheritance - Creating Sub Classes

#  Methods listed under Method resolution order is the place where Python searches for attributes and methods

# Never pass mutable datatype like list or dict as default arguments

# built-in functions isinstance & issubclass are useful when using inheritance

# isinstance() --> says whether an object is a an object of a class
# issubclass() --> says whether a class is a sub class of another

# Example 4

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

# here the Employee class is inherited to Developer
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):

        # line 39 & 40 does the same by passing the first, last, pay information to parent __init__ method
        # super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)

        # this is preferably used as it is useful for data sync in case of multiple inheritance
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# here the Employee class is inherited to Manager
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        # this is preferably used as it is useful for data sync in case of multiple inheritance
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Test', 'User', 5000, 'Python')
dev_2 = Developer('Nikhil', 'Sekaran', 1000, 'Java')

print(dev_1.mail)
print(dev_2.mail)

print('###########################')

# to know where all the attributes and methods are searched can be known from help command
print(help(Developer))

print('###########################')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print('###########################')

print(dev_1.mail)
print(dev_1.prog_lang)

print(dev_2.mail)
print(dev_2.prog_lang)

print('****************************')

mgr_1 = Manager('Vikkram', 'Ravi', '10000', [dev_1])

print(mgr_1.mail)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

print('****************************')

# example of isintance()
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print('****************************')

# example of issubclass()
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

"""
Exception module under python WSGI library is an example for Inheritance
"""