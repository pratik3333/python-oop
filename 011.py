class Employee:
    num_of_emps=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'123@gmail.com'
        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply(self):
        self.pay=int(self.pay*self.raise_amt)

    @classmethod
    def change_raise_amt(cls,amount):
        cls.raise_amt=amount

    @classmethod
    def from_string(cls,emp_string):
        first,last,pay=emp_string.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1=Employee('corey','schafer',50000)
emp_2=Employee('pratik','kagale',60000)

Employee.change_raise_amt(1.08)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1='John-Deo-70000'

first,last,pay=emp_str_1.split('-')

import datetime
my_date=datetime.date(2021,5,24)
print(Employee.is_workday(my_date))