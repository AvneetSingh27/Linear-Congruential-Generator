def lcg(x0,a,c,m):
    prandomnums=[0] * 10;
    prandomnums[0]=x0
    for i in range(1,10):
        prandomnums[i]=((prandomnums[i-1]*a)+c)%m

    for i in prandomnums:
        print(i,end=" ")
    


if __name__ == '__main__':
    x0=int(input('Enter Seed value'))
    a=int(input('Enter multiplier'))
    c=int(input('Enter increment'))
    m=int(input('Enter modulus param'))

    lcg(x0,a,c,m)
