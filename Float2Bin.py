import math

while(True):
    f = float(input('Input Float:'))
    N = int(input('Bit number:'))

    dec = f*(2**(N-1))
    org_dec = dec

    bin = [0]*N

    for i in range(N):
        bin[i] = math.floor(dec/2**(N-i-1))
        dec = dec - bin[i]*(2**(N-i-1))

    if org_dec < 0:
        bin[0] = 1;

    print(bin)