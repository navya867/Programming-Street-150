number=int(input())
numb=0
while number>0:
    numb+=number%10
    number=number//10
print(numb)