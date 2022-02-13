x = 12345
z1 = 0
y = 37568
z2 = 0
while x > 0:
    digit = x % 10
    x = x // 10
    z1 = z1 * 10
    z1 = z1 + digit
    while y > 0:
        digit = y % 10
        y = y // 10
        z2 = z2 * 10
        z2 = z2 + digit
print('37568 -> ',  z2)
print('12345 -> ',  z1)
