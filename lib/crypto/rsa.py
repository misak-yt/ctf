import os
import math
import fractions

def is_prime(n):
    if n ==1 or n == 2:
        return False
    else:
        for i in range(3, math.sqrt(n)):
            if n % i == 0:
                return False
        return True

def lcm(p, q):
    return (p * q) // fractions.gcd(p, q)

# a, bが互いに素なときgcd(a, b) = 1
def ex_euqulid(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = ex_euqulid(b, a%b)
    y -= (a // b) * x
    
    return d, x, y

# 逆元の計算 ed ≡ 1(mod φ(n))
def inv_mod(e, d):
    return ex_euqulid(e, d)[0]


if __name__ == "__main__":

    p = int(input())
    q = int(input())
    n =  p * q
    l = lcm(p-1, q-1)
    e = 65537
    d = inv_mod(e, l)

    target = int(input("Enter Number: "))

    c = pow(target, e, n)
    print(c)

    print (pow(c, d, n))