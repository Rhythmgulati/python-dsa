def hcf(a,b):
    divident=max(a,b)
    divisor=min(a,b)
    rem=1
    while rem!=0:
        rem=divident%divisor
        divident=divisor
        ans=divisor
        divisor=rem
    return ans 


def hcftwo(a,b):
    for i in range(1,max(a,b)):
        if a%i==0 and b%i==0:
            hcf =i
    return hcf
        

print(hcf(4,36))
print(hcftwo(4,32))


