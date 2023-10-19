n = 3763
e = 11

ys = [2514, 1125, 333, 3696, 2514, 2929, 3368, 2514]

y_to_x = {}

for i in range(0x100):
    y_to_x[pow(i, e, n)] = i

plaintext = ''
for y in ys:
    plaintext = plaintext + chr(y_to_x[y])

print(plaintext) // "SIMPSONS"

