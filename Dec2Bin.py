import math

while(True):
    dec = int(input('Input Dec:'))
    N = int(input('Bit number:'))

    org_dec = dec

    bin = [0]*N

    for i in range(N):
        bin[i] = math.floor(dec/2**(N-i-1))
        dec = dec - bin[i]*(2**(N-i-1))

    if org_dec < 0:
        bin[0] = 1;

    print(bin)