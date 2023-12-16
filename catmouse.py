def catAndMouse(x, y, z):
    for i in range(q):
        cs1 = abs(x-z)
        cs2 = abs(y-z)

        if cs1 == cs2:
            return ("Mouse C")
            break
        elif (cs1> cs2):
            return ("Cat B")
            break
        else:
            return ("Cat A")
            break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)