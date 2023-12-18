
def beautifulDays(i, j, k):
    # Write your code here
    
    c = 0
    for s in range(i, j + 1):
        revnum = int(str(s)[::-1])
        res = abs(s - revnum) / k

        if res.is_integer():
            c += 1

    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)