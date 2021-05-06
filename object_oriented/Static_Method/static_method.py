class Employee:
    number_of_leaves=8

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        self.email=name+"123@gmail.com"

    def printdetail(self):
        return f'''The Employee name is {self.name}.\nsalary is {self.salary}.\nrole is {self.role}.\nemail is {self.email}.'''

    @classmethod
    def changeleaves(cls,newleaves):
        cls.number_of_leaves=newleaves


    @classmethod
    def from_dash(cls,string):
        #params = string.split("-")
        #print(params)
        #return cls (params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print(" This is good " + string)

pratik=Employee("Pratik",50000,"Student")
jack=Employee("Jack",60000,"super visor")
john=Employee.from_dash("John-980000-manager")

john.printgood("john")

jack.changeleaves(15)

#print(jack.number_of_leaves)

#(pratik.printdetail())

print(john.printdetail())