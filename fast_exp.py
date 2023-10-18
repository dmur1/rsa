def fast_mod_pow_understanding_cryptography(base, exp, mod):
    ''' Christof Paar. (2010). Understanding Cryptography.
        2nd ed. Berlin Heidelberg: Springer. p.182. '''
    r = base
    while exp > 0:
        if exp & 1:
            r = (r * base) % mod
        r = (r * r) % mod
        exp >>= 1
    return r

def fast_mod_pow_chat_gpt(base, exp, mod):
    ''' https://chat.openai.com/ '''
    r = 1
    while exp > 0:
        if exp & 1:
            r = (r * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return r

def test(i, j, k):
    a = fast_mod_pow_understanding_cryptography(i, j, k)
    b = fast_mod_pow_chat_gpt(i, j, k)
    c = pow(i, j, k)
    print(f"pow({i}, {j}, {k}) => uc: {a} gpt: {b} py: {c} {a == b == c}")

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            test(i, j, k)

print(fast_mod_pow_chat_gpt(2, 79, 101))
print(fast_mod_pow_chat_gpt(3, 197, 101))

