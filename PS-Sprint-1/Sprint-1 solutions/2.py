import math
def is_prime(p):
    count=0
    for i in range(2,int(math.sqrt(p))+1):
        if(p%i==0):
            count=count+1
            print(count)
    return count
p=int(input(" "))
count_value = is_prime(p)
if(count_value>0):
    print("Not prime")
else:
    print("Is prime")