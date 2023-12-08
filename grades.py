# n = 4
# int(input())
grades2=[23, 43, 84, 34]
grades=[]

for i in grades2:
    if(i>=38):
        val = i//5
        val2= (val+1)*5
        if (val2-i<3):
            i=val2
            grades.append(val2)
        else:
            grades.append(i)
    else:
        grades.append(i)
        
print(grades)




























