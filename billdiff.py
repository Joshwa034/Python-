
def bonAppetit(bill, k, b):
    # Write your code here
    
        bill.pop(k)
        numsum = sum(bill)
        share= numsum/2
        
        if(b <= share):
            print("Bon Appetit")
        elif(b>share):
            res= b-share
            print(int(res))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
