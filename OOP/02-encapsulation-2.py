
# NOTE: BREAKING ENCAPSULATION IS BAD.

class Myclass(object):
    def setValue(self,val):
        self.value=val

    def getValue(self):
        print(self.value)

a=Myclass()
b=Myclass()

a.setValue(100)
b.setValue(100)
a.value=200     # <== Overriding `set_value` directly
# <== ie..  Breaking encapsulation

a.getValue()
b.getValue()

