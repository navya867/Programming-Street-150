#Using Formula (Binet’s Formula)
#golden ratio
import math as m
n=int(input())
phi =(1+m.sqrt(5)) / 2
fib=round(((phi**n)-(1 - phi)**n) // m.sqrt(5))
print(fib)