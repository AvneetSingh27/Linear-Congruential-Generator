import math

def prime_factors(n):
    factors=[]
    while n % 2 == 0: 
        factors.append(2) 
        n = n / 2
           
    for i in range(3,int(math.sqrt(n))+1,2):  
        while n % i== 0: 
            factors.append(i) 
            n = n / i 
    
    if n > 2: 
        factors.append(n)

    return factors

def divisibile(a, b):
    factors = prime_factors(b)

    for i in factors:
        if a % i != 0:
            return False

    return True

def lcg(x0,a,c,m):
    full=False
    if math.gcd(c,m) ==1 and divisibile(a-1,m) and ((m%4==0) and ((a-1) % m ==0)):
        full=True
    
    prandomnums=[0] * m;
    prandomnums[0]=x0
    print(prandomnums[0],end=" ")
    for i in range(1,m):
        prandomnums[i]=((prandomnums[i-1]*a)+c)%m
        print(prandomnums[i],end=" ")
    
    count=1
    if(full):
        count=m
    else:
        for i in range(1,m):
            if(prandomnums[i] != x0):
                count+=1
            else:
                break
    
    print('\nCycle Length: ',count)
    


if __name__ == '__main__':
    x0=int(input('Enter Seed value: '))
    a=int(input('Enter multiplier: '))
    c=int(input('Enter increment: '))
    m=int(input('Enter modulus param: '))
    if m < 0 or a >= m or a <= 0 or c >= m or c < 0:
        print('Wrong Input, Please Follow the constraints')
    else:
        lcg(x0,a,c,m)
        
