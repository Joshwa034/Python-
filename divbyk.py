def divisibleSumPairs(n, k, ar):
    # Write your code here
    a=ar
    b=a
    count=0
    j=1

    for i in range(len(a)):
        for j in range(len(b)):
            if( i<j):
                d= a[i]+a[j]
                if(d%k==0):
                    count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
