from time import sleep
player1 = "X"
player2 = "O"
player = player1
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
def instructions(board): #These below are the instructions.
  print("Welcome to Noughts and Crosses!")
  sleep(2)
  print("Player 1 will be crosses. Player 2 will be noughts.")
  sleep(2)
  print("Enter the number 1 to 9 to choose a location on the grid")
  sleep(2)
  print("to place your nought or cross!")
  sleep(2)
  print("These are the positions on the grid:")
  sleep(2)
def displayboard(board):
    print(" ", "1", "│", "2", "│", "3")
    print(" ───┼───┼───")
    print(" ", "4", "│", "5", "│", "6")
    print(" ───┼───┼───")
    print(" ", "7", "│", "8", "│", "9") #This code displays the board layout.
def swapplayer(player):
  if player == player1:
    player = player2
  elif player == player2:
    player = player1
  return player #This changes it between player 1 and player 2.
def move(board, player1, player2):
  print(f"Where do you want to place your {player}?")
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
    #This still increases the turncount. I don't know how to change this.
  print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
  print(" ───┼───┼───")
  print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
  print(" ───┼───┼───")
  print(" ", board[2][0], "│", board[2][1], "│", board[2][2])
  print("") #This displays the board with the new O's or X's on it.
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
    return won #This code above checks for certain patterns of O's or X's.
instructions(board)
displayboard(board)
turncount = 0
while turncount < 9:
  move(board, player1, player2)
  turncount = turncount + 1
  if check_win(board, "X") == True:
    print("Player 1 wins!")
    break
  elif check_win(board, "O") == True:
    print("Player 2 wins!")
    break #This checks for O's or X's, and displays which player won.
  elif turncount == 9 and check_win != True:
    print("It's a draw.") #This code is for if no one has won.
  player = swapplayer(player)
check_win(board, player)