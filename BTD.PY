def bintodec(inputBits):
    a = inputBits
    if len(a) %4 !=0:
        print("invalid input")
    else:
        lst = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/"]
        for i in range(0, len(a), 4):
            temp=a[i:i+4]
            btd_val = int(temp,2)
            p = lst[btd_val]
            if p in ["+", "-", "*","/"]:
                print()
                print(p)
            else:
                print(p,end="")
bintodec("10010100101000100000")
