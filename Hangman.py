from random import choice as ch

HANGMAN = (
    '''
    -------
    |      |
    |
    |
    |
    |
    |
    ---------
    ''',
    '''
    -------
    |      |
    |      0
    |
    |
    |
    |
    ---------
    ''',
    '''
    -------
    |      |
    |      0
    |      |
    |
    |
    |
    |
    ---------
    ''',
    '''
    -------
    |      |
    |      0
    |    / |
    |
    |
    |
    |
    ---------
    ''',
    '''
    -------
    |      |
    |      0
    |    / | \\
    |
    |
    |
    |
    ---------
    ''',
    '''
    -------
    |      |
    |      0
    |     /|\\
    |     /
    |
    |
    |
    ---------
    ''',
    '''
    -------
    |      |
    |      0
    |     /|\\
    |     / \\
    |
    |
    |
    ---------
    '''
)
# максимальное кол-во попыток
max_attempts = len(HANGMAN) - 1

# создаем кортеж со словами для отгадывания
WORDS = ('питон', 'программирование', 'игра')

# рандомно выбираем слово из списка
word = ch(WORDS)
# создаем скрытое загаданное слово
word_q = '-' * len(word)
# колво не угаданных букв
mistakes = 0
# список угаданных букв
right_letters = []

# цикл для угадывания или проигрыша
while mistakes < max_attempts and word_q != word:
    print(HANGMAN[mistakes])
    print('\nВы использовали следующие буквы:\n', right_letters)
    print('\nНа данный момент слово выглядит вот так\n', word_q)

    guess = input('\nВведите предполагаемую букву: ')
    while guess in right_letters:
        print('Вы уже угадали данную букву', guess)
        guess = input('Введите другую предполагаемую букву: ')
    right_letters.append(guess)

    # проверяем есть ли буква в загаданном слове
    if guess in word:
        print('\nДа! буква', guess, 'есть в слове!')

        # запоминаем угаданную букву
        new_letter = ''
        for i in range(len(word)):
            if guess == word[i]:
                new_letter += guess
            else:
                new_letter += word_q[i]
        word_q = new_letter
    else:
        print('\nИзвините буквы которую вы ввели \'' + guess + '\' нет в слове')
        mistakes += 1

if mistakes == max_attempts:
    print(HANGMAN[mistakes])
    print('\nТебя повесили!!!')
else:
    print('\nВы угадали слово!!!')

print('\nЗагаданное слово было\'' + word + '\'')
