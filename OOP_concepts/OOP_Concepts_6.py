# This file contains examples related to Property Decorators - Getters, Setters, Deleters

# Property Decorator allows class attributes to use Getter, Setter and Deleter functionality

# Example 6

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')

        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp1 = Employee('Test', 'User')

emp1.first = 'Nikhil'
"""
Even though the first name is updated the mail id does not reflect it with latest value.
To overcome this problem, we can create a function, but this is not a good idea as the client side also there is code
update due to this. 

To resolve this we go for Property decorator 
"""

# This line throws error "can't set attribute" as fullname does not have a setter
# This line works when @fullname.setter is available
emp1.fullname = 'Nikhil Sekaran'

print(emp1.first)

# This line prints "Test.User@email.com" if @property decorator is not used
# This line prints "Nikhil.User@email.com" with @property decorator
print(emp1.email)

print(emp1.fullname)

# This line invokes the deleter method
del emp1.fullname
