a = ''
def convert():
    """
    Recipe:
    asks for input, attach to var x, finds mod adds to a as a string, intwise divides by 2, do the same until x becomes 0. 
    Calls func again, do the same. 
    """
    x = int(input('Type Some Number In Decimal Base: '))
    global a 
    while x > 0: 
        a = str(x % 2) + a 
        x = x//2
    print(a)
    a = ''
    convert()
convert()
