class Fruits:
    no_of_fruits=0
    def __init__(self,fno,fname,fcolor):
        self.fno=fno
        self.fname=fname
        self.fcolor=fcolor
        Fruits.no_of_fruits +=1

    def fruit_display(self):
        return 'FNO:{} FName:{} FColor:{}'.format(self.fno,self.fname,self.fcolor)

    @classmethod
    def total_fruits(cls):
        return ('Total numbers of fruits %d' % cls.no_of_fruits)





f1=Fruits(1,'Apple','Red')
f2=Fruits(2,'Banana','Yellow')
f3=Fruits(3,'lemon','Yellow')

print(f1.fruit_display())
print(f2.fruit_display())
print(f3.fruit_display())
print(Fruits.total_fruits())