def greatestCommonDivisor(a, b):
    while a != b:
        if a > b:
            a = a % b
            if a == 0:
                return b
        else:
            b = b % a
            if b == 0:
                return a
    return a

print(greatestCommonDivisor(210, 165))
print(greatestCommonDivisor(6, 18))