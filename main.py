import os
import random as rand

with open('wordlist.txt', 'r') as file:
    words=[word.strip() for word in file.readlines()]
word=rand.choice(words).upper()
print(word)
guessed_word='_'* len(word)
print(guessed_word)
choices=6
hangman={
    0: (
        " o ",
        "/|\\",
        "/ \\",
        ),
    1: (
        " o ",
        "/|\\",
        "/  ",
        ),
    2: (
        " o ",
        "/|\\",
        "   ",
        ),
    3: (
        " o ",
        "/| ",
        "   ",
        ),
    4: (
        " o ",
        " | ",
        "   ",
        ),
    5: (
        " o ",
        "   ",
        "   ",
        ),
    6: (
        "    ",
        "    ",
        "    "
        )
}
guess=[]
def display_hangman(ind):
    for line in hangman[ind]:
        print(line)
def main():
    global guessed_word
    global choices
    global guess
    display_hangman(6)
    while choices:
        letter=input("Guess a letter: ")[0].upper()
        if letter in guess:
            print('Letter already guessed')
            continue
        if letter in word:
            for ind in range(len(word)):
                if letter==word[ind]:
                    guessed_word=guessed_word[:ind]+letter+guessed_word[ind+1:]
            if guessed_word==word:
                print('Congratulations you won!!')
                break
        else:
            choices-=1
            print('Wrong guess')
            print('Remaining chances: ', choices)
        print(guessed_word)
        display_hangman(choices)
        guess.append(letter)
    else:
        print('Game Over')
        print('You lose')
    print('The correct word is: ', word)
if __name__ =='__main__':
    main()
