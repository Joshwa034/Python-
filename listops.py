if __name__ == '__main__':
    N = int(input())
    res=[]

    for _ in range(N):
        opr=input().split()
        
        if opr[0]=="insert":
            res.insert(int(opr[1]), int(opr[2]))
        elif opr[0]=="print":
            print(res)
        elif opr[0]=="remove":
            res.remove(int(opr[1]))
        elif opr[0]=="append":
            res.append(int(opr[1]))
        elif opr[0]=="sort":
            res.sort()
        elif opr[0]=="pop":
            res.pop()
        elif opr[0]=="reverse":
            res=res[::-1]
            
        
        
    
    
