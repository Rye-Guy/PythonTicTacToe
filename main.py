import random
print('Welcome to Tic Tac Toe!') 

def display_board(board):
    print('------ ' + ' ----- ' + ' -----')
    print('------ ' + '|' + board[0] + '|' + board[1] + '|' + board[2] + '|' + ' -----')
    print('------ ' + '|' + board[3] + '|' + board[4] + '|' + board[5] + '|' + ' -----')
    print('------ ' + '|' + board[6] + '|' + board[7] + '|' + board[8] + '|' + ' -----')
    print('------ ' + ' ----- ' + ' ----- ')

test_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# display_board(test_board)

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player_input()

def place_marker(board, marker, position):
    board[position] = marker
    print(board[position])


def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
    (board[3] == mark and board[4] == mark and board[5] == mark) or 
    (board[6] == mark and board[7] == mark and board[8] == mark) or
    (board[0] == mark and board[3] == mark and board[6] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[0] == mark and board[4] == mark and board[8] == mark) or
    (board[2] == mark and board[4] == mark and board[6] == mark))  

def choose_first():
    randomInt = random.randint(1, 10)
    if randomInt <= 5:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] != 'X' or 'O'

def full_board_check(board):
    for space in range(1,10):
        if space_check(board, space):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [0,1,2,3,4,5,6,7,8] or not space_check(board, position):
        position = int(input('Choose a position between 1-9')) - 1
    return position

def replay():
    return input('Do you want to play again? (y or n)').lower.startswith('y')


# place_marker(test_board, 'O', 0)
# display_board(test_board)