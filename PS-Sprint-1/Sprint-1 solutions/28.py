n=int(input())
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
while fact>0:
    sum=sum+fact%10
    fact=fact//10
print(sum)

import math

# n = int(input())
# fact = math.factorial(n)                 # Fast factorial (C-optimized)
# digit_sum = sum(map(int, str(fact)))     # Convert to string and sum digits
# print(digit_sum)
