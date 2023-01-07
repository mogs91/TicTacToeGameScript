#TicTacToe Scripting Game


#Todo: Create 2 functions to check the values of the row and columns
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


print("Let's play TicTacToe!! \n"
      "Player X will go first and then Player O\n"
      "Here is the board \n")

game_board = [['_','_','_'],['_','_','_'],['_','_','_']]
for row in game_board:
    print(row)

is_game_running = True
player_X_turn = True
player_O_turn = False

while is_game_running:
    print("Please tell us the row and the column you want to write in")
    if player_X_turn:
        player_row = int(input('Player X Please enter row you want to mark on the board: '))
        player_col = int(input('Player X Please enter column you want to mark on the board: '))
        game_board[check_row(player_row)][check_column(player_col)] = 'X'
        for row in game_board:
            print(row)
        player_O_turn = True
    if player_X_turn:
        player_row = int(input('Player X Please enter row you want to mark on the board: '))
        player_col = int(input('Player X Please enter column you want to mark on the board: '))
        game_board[check_row(player_row)][check_column(player_col)] = 'X'
        for row in game_board:
            print(row)
        player_O_turn = True


#Todo: build a has won function checking the possible win conditions
#Todo: sync to Git




