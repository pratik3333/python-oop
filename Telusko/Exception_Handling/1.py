

a=4
b=0

try:
    print("Resource open")
    print(a/b)

except Exception as e:
    print("hey, you cannot devide a number by zero.",e)

finally:
    print("Resource close")

