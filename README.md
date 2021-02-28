# Linear-Congruential-Generator
 Psuedo Random Number Generator

_Linear Congruence Relation :-_
#### Xi = (aXi-1 + c)mod m

- a: multiplier parameter
- c: increment parameter
- m: modulus
- X0: seed value


***
###### Mathematics Part

for eg:

a=5,c=2,m=123,X0=73

X1 = 5(73) + 2 = 365 + 2 = 367 (mod123) = 121 (mod123)

X2 = 5(121) + 2 = 607(mod 123) = 115 (mod 123)

similarly rest random numbers can be generated.
***

###### pseudo code

```python
def lcg(x0,a,c,m):
    prandomnums=[0] * 10;
    prandomnums[0]=x0
    for i in range(1,10):
        prandomnums[i]=((prandomnums[i-1]*a)+c)%m

    for i in prandomnums:
        print(i,end=" ")
```
