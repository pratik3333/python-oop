av = 2
x = int(input('How much candy you want?'))

i = 1
while i <= x:

    if i > av:
        print('out of stock')
        break

    print('candy')
    i += 1

print('bye')