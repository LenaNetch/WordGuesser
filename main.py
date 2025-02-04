import random

word_list = ['Князь', 'тишины', 'Гудбай', 'Америка']

def get_word():
    global word_list
    return random.choice(word_list).upper()

def stage():
    while True:
        user_stage = input('Включить легкую сложность? y/n\n').lower()
        if user_stage == 'y' or user_stage == 'n':
            return user_stage
        else:
            print('Ожидается y или n')

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давай играть в угадайку слов')
    user_stage = stage()
    if user_stage == 'y':
        word_completion = word[0] + '_' * (len(word) - 2) + word[-1]
    while not guessed and tries > 0:
        print(word_completion)
        user_input = input('Ожидание ввода: ').upper()
        if len(user_input) == 1 and user_input.isalpha():
            if user_input not in guessed_letters:
                guessed_letters.append(user_input)
                if user_input in word:
                    word_completion = ''
                    for i in range(len(word)):
                        if user_input == word[i]:
                            word_completion += user_input
                        elif word[i] in guessed_letters:
                            word_completion += word[i]
                        else:
                            word_completion += '_'
                else:
                    tries -= 1
                    print('Данной буквы нет в слове ', tries)
            else:
                print('Данную букву уже загадывали')
        elif user_input != 1 and user_input.isalpha():
            if user_input not in guessed_words:
                guessed_words.append(user_input)
                if user_input != word:
                    tries -= 1
                    print('Данное слово не то ', tries)
                else:
                    word_completion = user_input
            else:
                print('Данное слово уже загадывали')
        elif not user_input.isalpha():
            print('Ожидается слово, либо буква')
        if word_completion == word:
            print('Вы победили!')
            guessed = True
        if tries == 0:
            print('Вы проиграли. Загаданное слово: ', word)

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

word = get_word()
play(word)