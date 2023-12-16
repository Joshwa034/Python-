
def birthday(s, d, m):
    # Write your code here
    sm = 0 
    for i in range(len(s)-m+1):
        csm =0
        for j in range(i,i+m):
            csm += s[j]
        if csm == d:
            sm +=1
    return sm 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
