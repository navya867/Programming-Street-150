def fibbonacci(f):
    a,b=0,1
    while(a<=f):
        print(a, end=' ')
        a,b=b,a+b                 #tuple unpacking assigns original values and sequential will assigns the above assigned value 

f=int(input(" "))
fibbonacci(f)

# F(n) = (φⁿ - ψⁿ) / √5

# Where:
# φ (phi) = (1 + √5) / 2 ≈ 1.618 (the golden ratio)
# ψ (psi) = (1 - √5) / 2 ≈ -0.618