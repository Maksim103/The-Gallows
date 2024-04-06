num = input('Введи число: ').strip()


def to_decimal(n):
    osn = int(input('Введи систему счисления ранее введёного числа (2, 8, 10, 16): '))
    s = str(n)[::-1]
    result = 0

    if osn != 16:
        for i in range(len(s)):
            result += int(s[i]) * osn**i
    else:
        hex_nums = ['10', '11', '12', '13', '14', '15']
        hex_abc = ['A', 'B', 'C', 'D', 'E', 'F']

        for i in range(len(s)):
            if s[i].isdigit():
                result += int(s[i]) * osn**i
            else:
                hex_i = hex_abc.index(s[i])
                result += int(hex_nums[hex_i]) * osn**i

    return result


def from_decimal(n):
    osn = int(input('Введи систему счисления, в которое ты хочешь перевести введёное число (2, 8, 10, 16): '))
    n = int(n)
    result = ''

    if osn != 16:
        result += str(n % osn)
        while n != 1:
            res = n // osn
            result += str(res % osn)

            if res > osn:
                res //= osn

            n //= osn

    else:
        hex_abc = ['A', 'B', 'C', 'D', 'E', 'F']
        while n != 0:
            res = n % osn
            print(res)
            if res < 10:
                result += str(res)
            else:
                result += hex_abc[res % 10]
            print(n)
            n //= osn

    return result[::-1]


print(from_decimal(num))
