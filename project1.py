import random
import datetime

# This is the source code for my CodeAcademy Final Project. I will be making a game.
# The game is Battleship. It has two players, each with their own board. They will have 6 
# ships each, each will have varying lengths from 2 - 6. 
# The players will decide who goes first by guessing a number between 1 and 10. 
# Whoever is closest will go first. 

# Player class holds certain paramters specific to a player
class Player:
    def __init__(self, name, number, board):
        # name is player name, number is 1-10
        # turn will be determined outside the class.
        # setup is the players board
        self.name = name
        self.number = number
        self.board = board

# Board class to setup playing boards for each player and perform action on boards.
# size refers to game board size, it will be an int refering to int x int
# ships is number of ships not sunk
# setup is placement of ships on a 2d array of chars
class Board:
    def __init__(self, size, configuration, ships= 1):
        self.size = size # game board size, i.e. size x size
        self.ships = ships # number of non-sunk ships
        self.configuration = configuration # placement of ships- 2d char array/ list

# a ship has a size that corresponds to the number of hits it can take
class Ship:
    def __init__(self, size):
        self.size = size


# This function takes in two players and decides who goes first
def who_goes_first(player1, player2):
    # initialize a random number between 1 and 10
    random_num = random.randint(1, 10)
    # compute some calculations
    player1num = abs(random_num - int(player1.number))
    player2num = abs(random_num - int(player2.number))

    # whichever number was closest to the random will go first
    if player1num > player2num:
        return player2.name
    else:
        return player1.name


# Start game by greeting players and asking for information 
def greet_and_initialize():

    print("Hello players!.\n Before we begin please tell me your")
    print(" name and a number between 1 and 10.")
    player1_name = input("Player 1 name: ")
    player1_number = input("Player 1 number: ")

    player2_name = input("Pleyer 2 name: ")
    player2_number = input("Player 2 number: ")

    # check to make sure the numbers are not the same
    if (player1_number == player2_number):
        player2_number = input("Please enter a different number: ")

    # initialize our players... take input for name and number
    player1 = Player(player1_name, player1_number, None) 
    player2 = Player(player2_name, player2_number, None)

    # Decide how big the board should be
    game_board_size = input("How big should the board be? ")

    first = who_goes_first(player1, player2)

    return [player1, player2, game_board_size, first]

# This function initializes the game boards/ configuration
def place_ships():
    pass


def create_board(size):
    rows, cols = (int(size), int(size))
    board = []

    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        board.append(col)
    return board

def assign_ship(board, coordinates):
    board[coordinates[0]][coordinates[1]] = 1


# This function calls on other functions to simulate hitting other ships and missing ships.
# It is the main function for the actual game play.
def play_game(player1, player2, first):
    starting_player = ""
    if first == player1.name:
        starting_player = player1.name
    else:
        starting_player = player2.name

    print("Let's begin! " + starting_player + " goes first...\n")

    while player1.win != 1 or player2.win != 1:
        row = input("Enter a row: ")
        col = input("Enter a column: ")
        turn = 1

        if turn == 1:
            if player1.board[row][col] == 1:
                print("HIT!")
                player1.board[row][col] = -1
                player1.hits -= 1
                turn += 1

                if player1.hits == 0:
                    # player 2 wins
                    player2.win = 1
            else:
                print("Miss :( ")

        else:
            if player2.board[row][col] == 1:
                print("HIT!")
                player2.board[row][col] = -1
                player2.hits -= 1
                turn -= 1

                if player2.hits == 0:
                    player1.win = 1
            else:
                print("Miss :( ")

    # Announce the winner
    winning_player = ""
    if player1.win == 1:
        winning_player = player1.name
    else:
        winning_player = player2.name
    print("Congratulations {}, you won the game !!!".format(winning_player) )









# Initializing GAME ------------------------------------------------------------------------------------------------------------------------------------------------
# Start the game
players = greet_and_initialize()

# make players
p1 = players[0]
p2 = players[1]

#make board
p1.board = create_board(players[2])
p2.board = create_board(players[2])

# set ships on board
# call function to randomly assign ships?
assign_ship(p1.board, [0,0])
print(p1.board)

# start playing
play_game(p1, p2, players[3])

date = datetime.time(5, 30, 6)