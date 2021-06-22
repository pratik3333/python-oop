from functools import reduce

def add_all(a,b):
    return a+b

nums=[2,3,4]

evens=list(filter(lambda n:n%2==0,nums))
double=list(map(lambda n:n*2,evens))

sum=reduce(add_all,double)

print(evens)
print(double)
print(sum)