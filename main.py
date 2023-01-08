#TicTacToe Scripting Game

def check_row(row):
    if row == 1:
        player_row = 0
        return player_row
    elif row == 2:
        player_row = 1
        return player_row
    elif row == 3:
        player_row = 2
        return player_row

def check_column(column):
    if column == 1:
        player_column = 0
        return player_column
    elif column == 2:
        player_column = 1
        return player_column
    elif column == 3:
        player_column = 2
        return player_column

def has_won(game_board):
    game_over = False
    #Version 1
    if game_board[0][0] == 'X'and game_board[1][0] == 'X' and game_board[2][0] == 'X' \
            or game_board[0][0] == 'O'and game_board[1][0] == 'O' and game_board[2][0] == 'O':
        game_over = True
        return game_over
    # Version 2
    elif game_board[0] == ['X','X','X'] \
            or game_board[0] == ['O', 'O', 'O']:
        game_over = True
        return game_over
    # Version 3
    elif game_board[1] == ['X','X','X'] \
            or game_board[1] == ['O', 'O', 'O']:
        game_over = True
        return game_over
    # Version 4
    elif game_board[2] == ['X','X','X'] \
            or game_board[2] == ['O', 'O', 'O']:
        game_over = True
        return game_over
    # Version 5
    elif game_board[0][1] == 'X'and game_board[1][1] == 'X' and game_board[2][1] == 'X' \
            or game_board[0][1] == 'O'and game_board[1][1] == 'O' and game_board[2][1] == 'O':
        game_over = True
        return game_over
    # Version 6
    elif game_board[0][2] == 'X'and game_board[1][2] == 'X' and game_board[2][2] == 'X' \
            or game_board[0][2] == 'O'and game_board[1][2] == 'O' and game_board[2][2] == 'O':
        game_over = True
        return game_over
    # Version 7
    elif game_board[0][0] == 'X'and game_board[1][1] == 'X' and game_board[2][2] == 'X' \
            or game_board[0][0] == 'O'and game_board[1][1] == 'O' and game_board[2][2] == 'O':
        game_over = True
        return game_over
    # Version 8
    elif game_board[0][2] == 'X'and game_board[1][1] == 'X' and game_board[2][0] == 'X' \
            or game_board[0][2] == 'O'and game_board[1][1] == 'O' and game_board[2][0] == 'O':
        game_over = True
        return game_over
    else:
        return game_over

print("Let's play TicTacToe!! \n"
      "Player X will go first and then Player O\n"
      "Here is the board \n")

game_board = [['_','_','_'],['_','_','_'],['_','_','_']]
for row in game_board:
    print(row)

is_game_running = True
player_X_turn = True
player_O_turn = False

def play_game(is_game_running, player_X_turn, player_O_turn,game_board):
    while is_game_running:
        game_over = has_won(game_board)
        if game_over:
            print("GAME OVER Player O wins!")
            is_game_running = False
            break
        else:
            print("Please tell us the row and the column you want to write in")
            if player_X_turn:
                player_row = int(input('Player X Please enter row you want to mark on the board: '))
                player_col = int(input('Player X Please enter column you want to mark on the board: '))
                game_board[check_row(player_row)][check_column(player_col)] = 'X'
                for row in game_board:
                    print(row)
                game_over = has_won(game_board)
                print(game_over)
                if game_over:
                    print("GAME OVER Player X wins!")
                    is_game_running = False
                    break
                else:
                    player_O_turn = True
            if player_O_turn:
                player_row = int(input('Player O Please enter row you want to mark on the board: '))
                player_col = int(input('Player O Please enter column you want to mark on the board: '))
                game_board[check_row(player_row)][check_column(player_col)] = 'O'
                for row in game_board:
                    print(row)
                player_X_turn = True


if is_game_running:
    play_game(is_game_running, player_X_turn, player_O_turn,game_board)
elif is_game_running== False:
    print("Thank you for playing")
    restart = input("If want to play again press Y else press N: ")
    if restart == 'Y':
        game_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        is_game_running = True
        player_X_turn = True
        player_O_turn = False
        play_game(is_game_running, player_X_turn, player_O_turn)
    elif restart == 'N':
        print("Thank you for playing")
        exit()




