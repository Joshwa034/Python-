
def findDigits(n):
    # Write your code here
    c=0
    ls = list((str(n)))
    for i in range(len(ls)):

        if int(ls[i]) != 0 and n % int(ls[i]) == 0:
            c+=1
        # print(int(ls[i]))
    return(c)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
