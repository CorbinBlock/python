"""
2020-12-26

Python Object-Oriented Programming
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Objective -
Create class and instance of class
Use instance level variable
"""


class Employee:
    

    # we use an init method to automatically set up employee class when we create an employee

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # need to include self argument for instance

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corbin', 'Block', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

incorrectclass = """

emp_1.first = 'Corbin'
emp_1.last = 'Block'
emp_1.email = 'corbinblock@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'USer'
emp_2.email = 'testuser@company.com'
emp_2.pay = 60000

print('{} {}'.format(emp_1.first, emp_1.last))

"""
