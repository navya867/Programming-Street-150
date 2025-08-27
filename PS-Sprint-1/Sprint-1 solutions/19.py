import math as m
x,y=map(int, input(" ").split())
results=[]
for i in range(x, y+1):
    prime=i
    i=int(m.sqrt(i))
    while i>=2:
        if(prime%i==0):
            break
        i=i-1
    else:
        results.append(prime)
print(results)
    

