class Myclass(object):
    def setValue(self,val1):
        self.value=val1

    def getValue(self):
        print(self.value)
        return self.value

a=Myclass()
b=Myclass()

a.setValue(10)
b.setValue(1000)

a.getValue()
b.getValue()
print(a.getValue())