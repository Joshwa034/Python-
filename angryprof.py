
def angryProfessor(k, a):
    # Write your code here4
    c=0
    for i in range(len(a)):
        if a[i] <=0:
            c+=1           #1: 0, 2: -1

    if c>=k:
        return 'NO'
    elif(c<k):
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)