y = int(input())
x = int(input())

yprime = True if y%2 == 0 else False
xprime = True if x%2 == 0 else False

if (yprime and xprime) or (not yprime and not xprime):
    print('NEGRO')
else:
    print('BLANCO')
