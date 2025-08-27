x,y=map(int, input().split())
sum=0
for i in range(x+1,y+1):
    if(i%2!=0):
        sum=sum+i
print(sum)