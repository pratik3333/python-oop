

a=4
b=0

try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter the number":))
    print(k)


except ZeroDivisionError as e:
    print("hey, you cannot devide a number by zero.",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong...")
finally:
    print("Resource close")

