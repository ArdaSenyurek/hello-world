def dec_to_bin():
    x = input('Enter some decimal number: ')
    y = int(x)
    b = ''
    counter = 0
    def power():
        for n in range(0, 32):
            if 2**n - y > 0:
                return n
    
    abc = power()
    while counter < abc:
        y // 2
        if counter == 0:
            a = y % 2
            b = b + str(a)
        else: 
            y // 2
            b = str(y % 2) + b 
            #print(b)
        y = y // 2
        #print(b)
        counter = counter + 1 
    print(b)
    dec_to_bin()
dec_to_bin()
