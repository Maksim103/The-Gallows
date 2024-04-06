words = input()


def create_rus_alphabet():
    a = ord('а')  # 'а' - русская
    rus_lower = ''.join([chr(i) for i in range(a, a + 32)])

    return rus_lower


def create_eng_alphabet():
    a = ord('a')  # 'a' - английская
    eng_lower = ''.join([chr(i) for i in range(a, a + 26)])

    return eng_lower


rus_alphabet = create_rus_alphabet()
eng_alphabet = create_eng_alphabet()


def caesar_cipher(text: str, shift: int, alphabet: str):
    result = ''

    for c in text:
        if c.isalpha():
            if c.islower():
                lw_i = alphabet.lower().find(c)
                result += alphabet.lower()[(lw_i + shift) % len(alphabet)]
            elif c.isupper():
                up_i = alphabet.upper().find(c)
                result += alphabet.upper()[(up_i + shift) % len(alphabet)]
        elif c == ' ':
            result += ' '
        else:
            result += c

    return result


def decrypt_caesar_cipher(text: str, shift: int, alphabet: str):
    result = ''

    for c in text:
        if c.isalpha():
            if c.islower():
                lw_i = alphabet.lower().find(c)
                result += alphabet.lower()[(lw_i - shift) % len(alphabet)]
            elif c.isupper():
                up_i = alphabet.upper().find(c)
                result += alphabet.upper()[(up_i - shift) % len(alphabet)]
        elif c == ' ':
            result += ' '
        else:
            result += c

    return result


print(caesar_cipher(words, 25, eng_alphabet))  # Шифровка
# print(decrypt_caesar_cipher(words, 25, eng_alphabet))  # Дешифровка
