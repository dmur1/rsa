def eea(r0, r1):
    assert(r0 > r1)
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

p = 3
q = 11
n = p * q
phi = (p - 1) * (q - 1)
e = 3
g, s, t = eea(phi, e)
d = t

def enc(x):
    return (x ** e) % n

def dec(y):
    return (y ** d) % n

for i in range(1, n):
    print(i)
    assert(dec(enc(i)))
