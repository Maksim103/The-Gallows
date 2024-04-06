import random

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
             'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
             'конец',  'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'закон',
             'вода', 'отец', 'проблема', 'час', 'право', 'нога', 'решение', 'дверь', 'образ', 'история', 'власть']


def is_invalid(s: str):
    if not s.isalpha():
        return False
    return True


def get_word(lst):
    word = random.choice(lst)
    return word


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]

    return stages[tries]


def play(word: str):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print(display_hangman(tries))
    print(f'У тебя {tries} попыток')
    print(word_completion, ' - поля букв')

    while True:
        text = input('Введи букву или слово целиком: ')

        if not is_invalid(text):
            print('Ты ввёл неправильную строку')
            continue

        if text in guessed_letters or text in guessed_words:
            print('Ты уже это вводил')
            continue

        if text == word:
            print()
            print('Поздравляю. Ты угадал слово:', word)
            break

        if text in word:
            index_abc = [i for i in range(len(word)) if text == word[i]]

            word_completion = list(word_completion)

            for n in index_abc:
                word_completion[n] = text

            word_completion = ''.join(word_completion)
            print(word_completion)
        else:
            tries -= 1
            print(display_hangman(tries))
            print(f'У тебя {tries} попыток')

        if not tries:
            print('Ты проиграл :( \n Загаданным словом было ' + word)
            break

        if len(text) == 1:
            guessed_letters.append(text)
            print(*guessed_letters, ' - твои буквы, которые ты уже вводил')
        else:
            guessed_words.append(text)

        if not word_completion.count('_'):
            print()
            print('Поздравляю. Ты угадал слово:', word)
            break


while True:
    print('Давайте играть в угадайку слов!')
    play(get_word(word_list))

    flag = input('Хочешь сыграть заново (да/нет): ').strip().lower()

    if flag == 'да':
        play(get_word(word_list))
    else:
        break
