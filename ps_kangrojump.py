#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # if x1>x2 or (x1<x2 and v2>v1):
    #     return "NO"
    # else:
    #     i =0
    #     xpos = 0
    #     ypos = 0
    #     while(i<1):
    #         x1 = x1+v1
    #         x2 = x2+v2
    #         xpos +=x1
    #         ypos +=x2
    #         if xpos == ypos:
    #             return "YES"
    #             i = 1
    result='NO'
    for i in range(max(x1,x2)**2):
        if x1+v1==x2+v2:
            result='YES'
            break
        else:
            x1+=v1
            x2+=v2
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
