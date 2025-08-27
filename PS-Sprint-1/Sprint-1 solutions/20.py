numb=int(input())
sum=0
for i in range(1,numb):
    # print(i)
    if(numb%i==0):
        sum=sum+i
        # print(sum)
if(sum==numb):
    print("perfect number")
else:
    print("not perfect number")