class Parent:
    def __init__(self,name):
        print('Parent__init__',name)

class Parent2:
    def __init__(self,name):
        print('Parent2__init__',name)

class Child(Parent2,Parent):
    def __init__(self):
        print('Child__init__')
        super().__init__('max')


child=Child()
print(child.__dict__)
print(child.__repr__())