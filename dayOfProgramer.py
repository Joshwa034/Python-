
def dayOfProgrammer(year):
    # Write your code here
    if year<=2700 and year>=1700:
        
        if year% 400==0 or year% 100!=0 and year% 4==0 or year==1700 or year ==1800 or year==1900:
            res = '12.09.'+ str(year)
        else:
            res = '13.09.'+ str(year)
        if (year== 1918):
            res = '26.09.'+str(year)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)