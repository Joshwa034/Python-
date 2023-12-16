
def migratoryBirds(arr):
    # Write your code here
    dic = {}
    res = 0
    set1 = set(arr)
    for i in set1:
        item_count = arr.count(i)
        dic[i]=item_count
        
    mx_val = max(dic.values())
    
    keyslist= list(sorted(dic.keys()))
    
    for i in range(len(keyslist)):
        if dic[keyslist[i]] == mx_val:
            res+=keyslist[i]
            break
    return res
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)