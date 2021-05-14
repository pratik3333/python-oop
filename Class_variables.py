class Employee:
    no_of_emps=0
    raise_amount=1.4
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'123@gmail.com'

        Employee.no_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        return self.pay * self.raise_amount

emp1=Employee('Corey','Schafer',78000)
emp2=Employee('Pratik','Kagale',78000)

print(emp1.raise_amount)
print(Employee.no_of_emps)
emp2.raise_amount=2
print(emp1.apply_raise())
print(emp2.apply_raise())