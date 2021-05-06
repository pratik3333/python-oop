class Employee:
    number_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        self.email=name+"123@gmail.com"

    def printdetail(self):
        return f'''The name is {self.name}.\nsalary is {self.salary}.\nrole is {self.role}.\nemail id is "{self.email}" '''

    @classmethod
    def change_leaves(cls,newleaves):
        cls.number_of_leaves=newleaves


pratik=Employee("pratik",50000,"student")
pranit=Employee("Pranit",60000,"student")

print(pratik.printdetail())
print(pratik.number_of_leaves)

#classmethod apply
pratik.change_leaves(45)
print(pranit.number_of_leaves)

print(pratik.number_of_leaves)