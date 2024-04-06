import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cntPw = int(input('Укажите количество паролей для генерации: '))
lenPw = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? (y/n) ')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')


def add_chars(char):
    if digOn == 'y':
        char += digits
    if ABCon == 'y':
        char += uppercase_letters
    if abcOn == 'y':
        char += lowercase_letters
    if chOn == 'y':
        char += punctuation
    if excOn == 'y':
        for c in excOn:
            char = char.replace(c, '')


add_chars(chars)


def generate_password(length, char):
    password = ''

    for i in range(length):
        r_c = random.choice(char)
        password += r_c

    return password


for _ in range(cntPw):
    generate_password(lenPw, chars)
