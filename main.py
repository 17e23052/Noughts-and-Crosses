board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
player = "X"
def displayboard(board):
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
    print(" ───┼───┼───")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
    print(" ───┼───┼───")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2])
displayboard(board)
def check_win(board, player):
    won = False
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        won = True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        won = True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        won = True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        won = True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        won = True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        won = True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        won = True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        won = True
    print(f"Won = {won}")
check_win(board, player)