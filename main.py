from time import sleep
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
def instructions(board):
  print("Welcome to Noughts and Crosses!")
  sleep(2)
  print("Player 1 will be noughts, and player 2 will be crosses.")
  sleep(2)
  print("Enter the number 1 to 9 to choose a location on the grid")
  sleep(2)
  print("To place your O or X on the board!")
  sleep(2)
  print("These are the positions on the grid:")
  sleep(2)
def displayboard(board):
    print(" ", "1", "│", "2", "│", "3")
    print(" ───┼───┼───")
    print(" ", "4", "│", "5", "│", "6")
    print(" ───┼───┼───")
    print(" ", "7", "│", "8", "│", "9")
player = "X"
def move(board, player):
  print("Where do you want to place your cross?")
  position = input()
  if position == "1":
    board[0][0] = player
  elif position == "2":
    board[0][1] = player
  elif position == "3":
    board[0][2] = player
  elif position == "4":
    board[1][0] = player
  elif position == "5":
    board[1][1] = player
  elif position == "6":
    board[1][2] = player
  elif position == "7":
    board[2][0] = player
  elif position == "8":
    board[2][1] = player
  elif position == "9":
    board[2][2] = player
  else:
    print("Invalid input")
  print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
  print(" ───┼───┼───")
  print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
  print(" ───┼───┼───")
  print(" ", board[2][0], "│", board[2][1], "│", board[2][2])
def check_win(board, player):
    won = False
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        won = True
        return won
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
instructions(board)
displayboard(board)
move(board, player)
check_win(board, player)
if check_win(board, "O") == True:
  print("Player 1 wins!")
elif check_win(board, "X") == True:
  print("Player 2 wins!")