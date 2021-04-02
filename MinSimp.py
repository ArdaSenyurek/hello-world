L = [1,3,7,35,7,-8]
L2 = [2,4,5,6,7,9]


def MinSimp(a,b):
    """
    Assumes a and b are lists that contains no string. 
    Returns list of min values of pairs,e.g compares first elements, then second elements etc...
    """
    for i in a:
        assert type(i) != str , "elements shouldn't be string" 
    for i in b:
        assert type(i) != str , "elements shouldn't be string" 
    L3 = []
    L4 = []
    def makePairs(a,b):
        counter = 0
        for _1 in a[counter:]: 
            for _2 in b[counter:]:
                L3.append([_1,_2])
                break
            counter += 1
        return L3
    def FindMin(pairs):
        for pair in pairs:
            L4.append(min(pair)) 
                
        return L4
    return FindMin(makePairs(a,b))
print(MinSimp(L,L2))
help(MinSimp)
