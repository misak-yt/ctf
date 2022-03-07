import os
import math
import fractions

def is_prime(n):
    if n ==1 or n < 0:
        return False
    else:
        for i in range(2, math.sqrt(n)):
            if n % i == 0:
                return False
        return True

def lcm(p, q):
    return (p * q) // fractions.gcd(p, q)

# a, bが互いに素なときgcd(a, b) = 1
def ex_euqulid(a, b):
    if b == 0:
        return a, 1, 0
    y, x, d = ex_euqulid(b, a%b)
    y -= (a // b) * x
    
    return x, y, d

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

    print('公開鍵：e = {0}, n = {1}'.format(e, n))
    print('暗号文：{0}'.format(c))
    print ('復号化：{0}'.format(pow(c, d, n)))