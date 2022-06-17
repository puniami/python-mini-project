import beepy
from os import system
from random import choice


def hang(n):
    mapping = {
        0: "   ---------  ",
        1: "     \ O /    ",
        2: "      /|\     ",
        3: "      / \     "
    }

    if n > len(mapping)-1:
        mapping[1] = mapping[1].replace('\ O /', '  O_|')

    for each in range(n):
        print(mapping[each])


def game():
    word = choice([
                "tiger", "superman", "thor",
                "doraemon", "avenger", "water",
                "stream"])
    ans = ['_']*len(word)
    c = 0
    while '_' in ans:
        print(' '.join(ans))
        abet = input('guess an alphabet: ').lower()
        if not abet.isalpha():
            print('Please only entry alphabets...')
            continue
        if abet in word:
            ans[word.index(abet)] = abet
        else:
            c += 1
            if 0 < c < 4:
                hang(c)
            else:
                system('clear')
                hang(c)

                print('You are hanged...')
                beepy.beep(7)
                return
    print("Great you won :)")
    beepy.beep(6)


if __name__ == '__main__':
    game()
