def MakeStr(a):
    for e in a:
        if e != str:
            e = str(e)
    return a
L = [1,5]
L2 = [2, 4]
def FindMin(a, b):
    for el in a:
        for e in b:
            if e < el:
                print(f'element {e} is less than {el}')
            else:
                print(f'element {el}, which belongs to L, is less than {e}')
            
            
print(FindMin(L,L2))
for i in map(FindMin, L, L2):
    print(type(i))
    print(i)
