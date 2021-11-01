import os, random


def get_word():
    words = []

    with open('./data/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    
    # we extract a random word from the list
    random_word = words.pop(random.randint(0,len(words)))

    # we convert string to letters and we add some additional information in a list of dictionaries
    selected_word = [{'letter': letter, 'found': False} for letter in random_word]

    return selected_word


def clear_screen():
    """It clears the screen"""
    os.system('clear')


def print_screen(selected_word):
    """It shows the letters found on the screen"""
    
    clear_screen()

    displayed_word = list(map(lambda x: x['letter'] if x['found'] else '-'  , selected_word))
    
    # we convert list to string
    displayed_word = ' '.join(displayed_word)

    print('Adivina la palabra!')
    print(displayed_word)


def print_lives(lives):
    """It shows a hangman picture on the screen, depending of lives left"""
    pictures = [
            '''
            ____
            |   |
            |   o
            |  -|-
            |  / \\
          __|______
            ''',
              '''
            ____
            |   |
            |   o
            |  -|-
            |  /
          __|______
            ''',
              '''
            ____
            |   |
            |   o
            |  -|-
            |
          __|______
            ''',
              '''
            ____
            |   |
            |   o
            |  -|
            |
          __|______
            ''',
              '''
            ____
            |   |
            |   o
            |   |
            |
          __|______
            ''',
              '''
            ____
            |   |
            |   o
            |
            |
          __|______
            ''',
              '''
            ____
            |   |
            |
            |
            |  
          __|______
            ''',
              '''
            ____
            |   
            |   
            | 
            |  
          __|______
            '''
    ]

    print(pictures[lives])


def find_in_selected_word(selected_word, letter):
    """It searchs for a letter in the word, and marks then as found"""
    
    found_words = 0
    for l in selected_word:
        if letter.lower() == l['letter'].lower() and not l['found']:
            found_words += 1
            l['found'] = True
    if found_words:
        return True
    else:
        return False


def you_won(selected_word):
    """It verify if all letters was found"""

    letters_left = list(filter(lambda x: not x['found'] ,selected_word))

    if len(letters_left) == 0:
        return True
    else:
        return False


def run():
    clear_screen()
    selected_word = get_word()

    lives = 7

    while True:
        print_screen(selected_word)
        print_lives(lives)
        
        letter = input('Ingresa una letra: ')
        assert letter.isalpha(), 'Solo puedes introducir letras'
        assert len(letter) == 1, 'Solo puedes introducir una letra a la vez'

        if not find_in_selected_word(selected_word, letter):
            lives -= 1
        
        # Do you won?
        if you_won(selected_word):
            clear_screen()
            print_screen(selected_word)
            print('Fantástico! la adivinaste!')
            break
        
        # Do you loose?
        if lives < 1:
            clear_screen()
            print_screen(selected_word)
            print('Lo siento! Perdiste!')
            break
    
    
if __name__ == '__main__':
    run()