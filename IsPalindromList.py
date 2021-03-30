txt = input(r"Enter text to see if it's a palindrom text: " )
txt_low = txt.lower()
print(txt_low)

if txt[-1] == '.': 
    txt_no_dot = txt[0:-1]
    mutated = txt_no_dot.split(' ')
    nospc = ''.join(mutated)
else: 
    mutated = txt.split(' ')
    nospc = ''.join(mutated)
    
print(nospc)
def ispalindrom(a):
    print(a)
    print(len(a))
    if len(a) <= 1:
        return True
    else: 
        ispalindrom(a[1:-1])
    
print(ispalindrom(nospc))
