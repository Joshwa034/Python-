
def viralAdvertising(n):
    s = 5
    l = 2
    c = 2
    
    for i in range(2,n+1):
        s= l*3
        l = s//2
        c+=l
    return c
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
