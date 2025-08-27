import math as mat
n=int(input())
m=int(mat.sqrt(n))
per=1
for i in range(2,m+1):
    if(n%i==0):
        per=per+i
        if(i != n // i):
            per=per+(n // i)
if(n>1 and n==per):
    print("perfect number")
else:
    print("not perfect number")

    