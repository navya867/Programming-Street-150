import math as m
x=input(" ").split()
results=[]
for i in range(2,x):
    prime=i
    i=int(m.sqrt(i))
    while i>=2:
        if(prime%i==0):
            break
        i=i-1
    else:
        results.append(prime)
print(results)