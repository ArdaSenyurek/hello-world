a = ''
x = int(input('Type Some Number In Decimal Base: '))

while x > 0: 
    a = str(x % 2) + a 
    x = x//2
print(a)
