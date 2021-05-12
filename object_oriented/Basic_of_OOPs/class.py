class Car:
    pass
ford=Car()
honda=Car()
audi=Car()

ford.speed=200
honda.speed=220
audi.speed=250

ford.color='red'
honda.color='black'
audi.color='grey'

print(audi.color)
print(audi.speed)

audi.speed=300
print(audi.speed)