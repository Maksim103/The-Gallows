def digital_root(n):
    if len(str(n)) == 1:
        return n
    s = 0

    while n != 0:
        last_digit = n % 10
        s += last_digit
        n //= 10
    n = s

    return digital_root(n)


print(digital_root(942))
