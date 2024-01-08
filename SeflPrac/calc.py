qes = (input())
ls = qes.split()

opls = ["+", "-", "*", "/", "%"]

try:
    if(int(ls[0]).isdigit and ls[2]!= "0"  ):
        if(ls[1] == opls[0]):
            summ = int(ls[0]) + int(ls[2])
        elif(ls[1] == opls[1]):
            summ = int(ls[0]) - int(ls[2])
        elif(ls[1] == opls[2]):
            summ = int(ls[0]) * int(ls[2])
        elif(ls[1] == opls[3]):
            summ = int(ls[0])/int(ls[2])
        elif(ls[1] == opls):
            summ = int(ls[0])%int(ls[2])
        print(summ) 
    else:
        print("Invalid char")
except:
    print("invalid input")
   


