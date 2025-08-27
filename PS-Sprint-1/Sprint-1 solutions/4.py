def is_armstrong(a):
    length_num=len(str(a))
    # print(length_num)
    arm=0
    while a>0 :
        a_1=a%10
        arm=a_1**length_num+arm
        # print(arm)
        a=a//10
    return arm

a= int(input(" "))
armstrong=is_armstrong(a)
if(armstrong==a):
    print("armstrong")
else:
    print("not armstrong")