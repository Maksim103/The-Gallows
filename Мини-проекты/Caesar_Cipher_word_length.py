import string

text = input()


def caesar_cipher(words):
    s = words

    eng_lower_alphabet = string.ascii_lowercase
    eng_upper_alphabet = string.ascii_uppercase

    for c in words:
        if c == ' ':
            continue
        if not c.isalpha():
            words = words.replace(c, '')

    ln = [len(lst) for lst in words.split()]

    result = ''
    count = 0

    for c in s:
        if c.isalpha():
            if c.islower():
                lw_i = eng_lower_alphabet.find(c)
                result += eng_lower_alphabet[(lw_i + ln[count]) % 26]
            elif c.isupper():
                up_i = eng_upper_alphabet.find(c)
                result += eng_upper_alphabet[(up_i + ln[count]) % 26]
        elif c == ' ':
            count += 1
            result += c
        else:
            result += c

    return result


print(caesar_cipher(text))
