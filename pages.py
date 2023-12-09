
def pageCount(n, p):
    # Write your code here
    
   
    if p==1 or n==p:
        return 0
    else:
        if (n-p)<p:
            if n-p <=1 and p%2!=0:
                return 1
            else:
                return (n-p)//2
        else:
            return p//2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
