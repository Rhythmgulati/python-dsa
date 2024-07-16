def countdigits(num):
    coun=0
    while num>0:
        num=num//10
        coun+=1
    return coun


def countdigitstwo(num):
    return len(str(num))

print(countdigits(123432))
print(countdigitstwo(45434556))