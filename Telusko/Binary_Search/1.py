pos=-1

def search(list,n):
    l=0
    u=len(list)-1

    while 1<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid+1
    return False

list=[23,5,4,5,56,6,8675,878,45,4345343,456]
n=10

if search(list,n):
    print("found at",pos+1)
else:
    print("Not found")