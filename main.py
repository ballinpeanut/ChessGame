from ChessVar import *

print("Welcome to this game of Chess made by Milton Molina \n")

print("The rules are simple. Most rules of Chess apply except for the following:\n"
      " - No pawn promotion \n"
      " - No en passant \n"
      " - No check or checkmate \n"
      " - Only win by capturing the other king.")

print()

print("Furthermore, to move a piece make sure to look closely at the board. The board is created in such a manner "
      "that you can enter 'a2' (as an example).\n")

start_game = int(input("To start the game enter 1, to quit press 0: "))

while start_game not in [0, 1]:
    print("Must be 1 or 0, try again.")
    start_game = int(input("To start the game enter 1, to quit press 0: "))
print()

if start_game == 1:
    print("Chess game started!")

    game = ChessVar()

    game.display_board()

    count = 0

    print(f"It is {game.get_turn()}'s turn.\n")

    while game.get_game_state() == "UNFINISHED":
        move_from = input("Enter square you are moving from (ex. a1): ")
        move_to = input("Enter square you want to move to (ex. a3): ")

        if game.make_move(move_from, move_to) is True:
            game.display_board()
            print(f"It is now {game.get_turn()}'s turn.\n")
            count += 1
        else:
            print("Invalid move. Try again.\n")

    if game.get_game_state() == "WHITE_WON":
        print("White has won!")
    else:
        print("Black has won!")

    print(f"Game took {count} turns.")
else:
    print()
    print("See you next time!")
