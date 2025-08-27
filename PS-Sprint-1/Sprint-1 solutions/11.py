a=int(input())
b=int(input())
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    lcm_res=(a*b)//(gcd(a,b))
    return lcm_res
# hcf checks smallest number to dec upto 1 and lcm checks from highest number to its multiples highest numb+highes  numb 
print(lcm(a,b))