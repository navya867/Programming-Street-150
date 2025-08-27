x=int(input(" "))
y=int(input(" "))
result=[]
for i in range(x,y+1):
    arm=i
    leng=len(str(i))
    res=0
    while i>0:
        res+=(i%10)**leng
        i=i//10
    if(arm==res):
        result.append(res)
    else:
        continue
# arm=' '.join(result)
print(result)
        
# technically all single digits are armstrong numbers 

