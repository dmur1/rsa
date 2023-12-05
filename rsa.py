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

def inverse(x, n):
    _, _, inverse = eea(x, n)
    return inverse

p = 31
q = 37
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = inverse(phi, e)

print(f"p={p} q={q} n={n} phi={phi} e={e} d={d}")

def enc(x):
    return pow(x, e, n)

def dec(y):
    return pow(y, d, n)

dp = d % (p - 1)
dq = d % (q - 1)
cp = inverse(q, p)
cq = inverse(p, q)

def dec_crt(y):
    yp = y % p
    yq = y % q
    xp = (yp ** dp) % p
    xq = (yq ** dq) % q
    x = (((q * cq) * xp) + ((p * cp) * xq)) % n
    return x

print(enc(2))
print(enc(4))
print(enc(2) * enc(4) % n)
print(enc(2 * 4))

n = 9797
phi = (p - 1) * (q - 1)
e = 131
d = inverse(phi, e)

def sign(x):
    return pow(x, d, n)

def verify(x, y):
    return pow(y, e, n) == x

x = 123
print(f"{x} => {verify(x, 6292)}")

x = 4333
print(f"{x} => {verify(x, 4768)}")

x = 4333
print(f"{x} => {verify(x, 1424)}")
