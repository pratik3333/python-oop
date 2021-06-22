from functools import reduce

nums=[2,3,4]

evens=list(filter(lambda n:n%2==0,nums))
double=list(map(lambda n:n*2,evens))

sum=reduce(lambda a,b:a+b,double)

print(evens)
print(double)
print(sum)