def eea(r0, r1):
    #assert(r0 > r1)
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    i = 1
    while True:
        i = i + 1
        r = r0 % r1
        if r == 0:
            break
        q = (r0 - r) // r1
        s = s0 - (q * s1)
        t = t0 - (q * t1)
        r0 = r1
        r1 = r
        s0 = s1
        s1 = s
        t0 = t1
        t1 = t
    return r1, s1, t1

def factor(n):
    toitent = 0
    for i in range(n-1):
        gcd, _, _ = eea(n, i + 1)
        if gcd == 1:
            toitent = toitent + 1
    return toitent

def inverse(x, n):
    _, _, inverse = eea(x, n)
    return inverse

n = 2623
phi = factor(n)
e = 2111
d = inverse(phi, e)
print(d)
