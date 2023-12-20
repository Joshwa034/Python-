
def permutationEquation(p):
    # Write your code here

    ls=[]
    for i in range(1,(len(p))+1):

        a = p.index(i)+1
        b = p.index(a)+1
        ls.append(b)
        
    return ls
        
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))
    
    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# 5
# 4,2,3,1,5