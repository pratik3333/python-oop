class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("parrot can't fly")


class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

#Comman interface
def flying_test(bird):
    bird.fly()

blu=Parrot()
pegge=Penguin()

flying_test(blu)
flying_test(pegge)