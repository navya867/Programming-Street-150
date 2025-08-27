def is_leap_year(l):
    if((l%4==0) and ((l%100!=0)) or (l%400==0)):
       return True
    else:
        return False 
l=int(input(" "))
if(is_leap_year(l)):
    print("Leap year")
else:
    print("Not leap year")