def cakeCandels(arr):
    n = len(arr)
    max = 0 
    count = 0
    for i in range(n):
        if (arr[i]>max):
            max = arr[i]
            count=1
        elif(arr[i]==max):
            count+=1
    return count
a = [4,4,1,3]
print(cakeCandels(a))
