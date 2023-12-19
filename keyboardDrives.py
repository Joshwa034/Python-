
def getMoneySpent(keyboards, drives, b):
    
    a = keyboards
    d = drives
    
    ls = []
    res = 0
    for i in range(len(a)):
        for j in range(len(d)):
            res = a[i]+d[j]
            if res<=b:
                ls.append(res)
                res = 0
    if len(ls)==0:
        return -1
    else:
                
        sol = max(ls)
        return sol
                
            
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)