def conv(n):
    width = len(bin(n)[2:])

    for i in range(1,n+1):
        dec = str(i).rjust(width)
        octn = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binn = format(i, 'b').rjust(width)
        print(f"{dec} {octn} {hexa} {binn}")

conv(2)

