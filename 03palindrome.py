def reverse(num):
    ans=0
    while num>0:
        rem=num%10
        ans=ans*10+rem
        num=num//10
    return ans


def ispalindrome(num):
    return reverse(num)==num

def ispalindrometwo(num):
    return str(num)==str(num)[::-1]


print(ispalindrome(1221))
print(ispalindrometwo(1231))