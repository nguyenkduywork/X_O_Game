import random

# 1. create a board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# 2. create a function to print the board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# 3. create a function to check if the game is over
def game_over():
    if check_winner() or check_tie():
        return True
    else:
        return False


# 4. create a function to check if there is a winner
def check_winner():
    # check rows
    if board[0] == board[1] == board[2] != "-":
        return True
    elif board[3] == board[4] == board[5] != "-":
        return True
    elif board[6] == board[7] == board[8] != "-":
        return True
    # check columns
    elif board[0] == board[3] == board[6] != "-":
        return True
    elif board[1] == board[4] == board[7] != "-":
        return True
    elif board[2] == board[5] == board[8] != "-":
        return True
    # check diagonals
    elif board[0] == board[4] == board[8] != "-":
        return True
    elif board[2] == board[4] == board[6] != "-":
        return True
    else:
        return False


# 5. create a function to check if there is a tie
def check_tie():
    if "-" not in board:
        return True
    else:
        return False


# 6. create a function to check if the player's move is valid
def check_player_move(player_move):
    if board[player_move] == "-":
        return True
    else:
        return False


# 7. create a function to check if the computer's move is valid
def check_computer_move(computer_move):
    if board[computer_move] == "-":
        return True
    else:
        return False


# 8. create a function to check if the player wants to play again
def play_again():
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        return True
    else:
        return False


# 9. Clear the board
def clear_board():
    for i in range(len(board)):
        board[i] = "-"

def choose_tile():
    if input("Do you want to play as x? (y/n): ") == "y":
        return ["x", "o"]
    else:
        return ["o", "x"]


def go_first():
    if input("Do you want to go first? (y/n): ") == "y":
        return True
    else:
        return False


def play_game():
    clear_board()
    # choose the tile
    player_tile, computer_tile = choose_tile()
    # check if the player wants to go first
    if go_first():
        turn = "player"
    else:
        turn = "computer"
    # play the game
    while not game_over():
        if turn == "player":
            print_board()
            player_move = int(input("Enter your move (0-8): "))
            if check_player_move(player_move):
                board[player_move] = player_tile
                turn = "computer"
            else:
                print("Invalid move!")
        else:
            computer_move = random.randint(0, 8)
            if check_computer_move(computer_move):
                board[computer_move] = computer_tile
                turn = "player"
    # check if there is a winner
    if check_winner():
        print_board()
        if turn == "player":
            print("Computer wins!")
        else:
            print("Player wins!")
    else:
        print("Tie!")
    # check if the player wants to play again
    if play_again():
        play_game()


# Play the game
play_game()
