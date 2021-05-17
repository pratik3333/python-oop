class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def did_it_pass(self):
        if self.marks >= 40:
            print("Pass")

        else:
            print("Fail")

s1=Student('Pratik',65)
s2=Student('Harry',30)

print(s1.name)
s1.did_it_pass()
print(s2.name)
s2.did_it_pass()