
def topten():


    yield 5


values=topten()
print(values.__next__())
