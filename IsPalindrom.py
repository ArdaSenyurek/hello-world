def IsPal(t):
    def str_mnp(t):
        clear = ''
        t_l = t.lower()
        for a in t_l:
            if ord(a) >= 97 and ord(a) <= 122:
                clear = clear + a
        print('ben strnin icindeyim', clear)
        return clear
    def isPal(str_mnp(t)):
        if len(a) <= 1:
            return True
        else:
            print(a[0] == a[-1])
            print(a)
            return a[0] == a[-1] and isPal(a[1:-1])
    
    return isPal(t)
            
while True:
    txt = input("Enter string to see if it's palindrom text: " ) 
    IsPal(txt)
    print(f"{txt} is {IsPal(txt)}")
