def reverseanum(num):
 ans=0
 while num>0:   
    rem=num%10
    ans=ans*10+rem
    num=num//10
 return ans

def reversetwo(num):
  return str(num)[::-1]

print(reverseanum(1223))
print(reversetwo(1232421))

