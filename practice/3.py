#parent class
class Bird:
    def __init__(self):
        print("Bird is ready")

    def Whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

#Child class
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def Whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy=Penguin()
peggy.Whoisthis()
peggy.swim()
peggy.run()
