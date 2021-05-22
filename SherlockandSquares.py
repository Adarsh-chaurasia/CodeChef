import math

def sqrt(num):
    s=math.sqrt(num)
    result=round(s*s,2)
    if  (num==result):
        print(result)
        return 1
    return 0

a,b=map(int,input().split())
z=0
for i in range(a,b+1):
    z+=sqrt(i)

print(z)
