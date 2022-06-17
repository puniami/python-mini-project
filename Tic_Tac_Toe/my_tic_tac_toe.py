from os import system


board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

maps = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
    }

def update_board(board):
    system('clear')
    print('--|---|--')
    for each in board:
        print(' | '.join(each), end='\n')
        print('--|---|--')

def get_players():
    p1 = input('player 1 name: ') or 'Player 1'
    p2 = input('player 2 name: ') or 'Player 2'
    return [(p1, 'X'), (p2, 'O')]

def game():

    p_data = get_players()
    update_board(board)

    for iteration in range(4):
        for name, item in p_data:
            num = input(f"{name} Enter (1-9) : ") or 0
            num = int(num)
            if not num in list(range(1, 10)):
                print('Wrong input, you lost this chance...')
                continue
            x, y = maps[num]
            if not board[x][y] == ' ':
                print('Already filled, you lost this chance...')
                continue
            board[x][y] = item
            update_board(board)

try:
    game()
except Exception:
    print('You are stupid....')
