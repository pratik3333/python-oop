class Calculation:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def Add(self):
        print(self.a + self.b)

    def Div(self):
        print(self.a / self.b)

c1=Calculation(10,20)
c2=Calculation(40,20)

c1.Add()
c2.Div()
