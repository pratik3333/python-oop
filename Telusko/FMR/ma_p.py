

nums=[2,3,4,5,6,67,890,66]

evens=list(filter(lambda n:n%2==0,nums))

double=list(map(lambda n:n*2,evens))

print(double)