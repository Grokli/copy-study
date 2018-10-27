# Cryptomath Module
# http://inventwithpython.com/hacking (BSD Licensed)

def gcd(a, b):
    # 获得a与b的最大公约数
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    # 获得a与m的模逆
    if gcd(a, m) != 1:
        return None # a与m必须互质
    
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 //v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m