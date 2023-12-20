def jumpingOnClouds(c, k):
    res = 100
    if (len(c)%k!=0):
        k = int((k-1)/2)
        
    for i in range(0, len(c), k):
        if (c[i]==1):
            res = res-3
        elif (c[i]==0):
            res= res-1
    return (res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# 
# c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
# n = len(c)
# k= 3