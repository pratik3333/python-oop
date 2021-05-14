class Employee:
    def __init__(self,first,last,pay,country):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'123@gmail.com'
        self.country=country

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1=Employee('Corey','Schafer',80000,'New York')
emp_2=Employee('Pratik','Kagale',78000,'India')

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_1.email)
print(emp_2.email)
print(emp_1.country)
print(emp_2.country)