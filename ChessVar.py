# Author: Milton Molina
# GitHub username: ballinpeanut
# Date: 5/13/2024
# Description: Chess game with special rules (coded in a night version of Pycharm, piece colors flipped in light mode)

class ChessVar:
    """
    Creates the chess game (rules, movement, pieces, board).
    Has methods for moves, setup of board, displaying board, if game is over.
    Keeps track of whose turn it is.
    """

    def __init__(self):
        # initializes the board
        self._chessboard = {}
        # initialize turns to keep track of whose turn it is to play (white starts)
        self._turn = 'WHITE'
        # initialize game state
        self._game_state = 'UNFINISHED'
        self.create_board()

    def create_board(self):
        """
        Initializes the chessboard with pieces at starting positions.
        """
        chessboard = dict()
        # white pieces
        chessboard['a1'] = Rook('WHITE', '♜')
        chessboard['b1'] = Knight('WHITE', '♞')
        chessboard['c1'] = Bishop('WHITE', '♝')
        chessboard['d1'] = Queen('WHITE', '♛')
        chessboard['e1'] = King('WHITE', '♚')
        chessboard['f1'] = Bishop('WHITE', '♝')
        chessboard['g1'] = Knight('WHITE', '♞')
        chessboard['h1'] = Rook('WHITE', '♜')
        chessboard['a2'] = Pawn('WHITE', '♟')
        chessboard['b2'] = Pawn('WHITE', '♟')
        chessboard['c2'] = Pawn('WHITE', '♟')
        chessboard['d2'] = Pawn('WHITE', '♟')
        chessboard['e2'] = Pawn('WHITE', '♟')
        chessboard['f2'] = Pawn('WHITE', '♟')
        chessboard['g2'] = Pawn('WHITE', '♟')
        chessboard['h2'] = Pawn('WHITE', '♟')

        # space in between
        for col in 'abcdefgh':
            for row in range(3, 7):
                chessboard[col + str(row)] = None

        # black pieces
        chessboard['a7'] = Pawn('BLACK', '♙')
        chessboard['b7'] = Pawn('BLACK', '♙')
        chessboard['c7'] = Pawn('BLACK', '♙')
        chessboard['d7'] = Pawn('BLACK', '♙')
        chessboard['e7'] = Pawn('BLACK', '♙')
        chessboard['f7'] = Pawn('BLACK', '♙')
        chessboard['g7'] = Pawn('BLACK', '♙')
        chessboard['h7'] = Pawn('BLACK', '♙')
        chessboard['a8'] = Rook('BLACK', '♖')
        chessboard['b8'] = Knight('BLACK', '♘')
        chessboard['c8'] = Bishop('BLACK', '♗')
        chessboard['d8'] = Queen('BLACK', '♕')
        chessboard['e8'] = King('BLACK', '♔')
        chessboard['f8'] = Bishop('BLACK', '♗')
        chessboard['g8'] = Knight('BLACK', '♘')
        chessboard['h8'] = Rook('BLACK', '♖')

        self._chessboard = chessboard

    def get_turn(self):
        """
        returns whose turn it is.
        """
        return self._turn

    def get_game_state(self):
        """
        returns whether game is unfinished or has a winner (white or black).
        """
        return self._game_state

    def make_move(self, move_from, move_to):
        """
        move_from: location piece is moving from using strings (letter, number in string format ex. ('a5'))
        move_to: location piece is moving to using strings
        Moves chess piece to a legal square.
        Makes checks in order to determine piece type (movement depending on type).
        Interacts with chess pieces, get_game_state, display_board, and within_chessboard_bounds.
        Board updates accordingly
        """
        # if game is not unfinished, then it is won, therefore return false if it is won.
        if self._game_state != "UNFINISHED":
            if self._game_state == "WHITE_WON":
                print("WHITE has won")
            else:
                print("BLACK has won")
            return False

        # move outside limits of chessboard.
        if not self.within_chessboard_bounds(move_from) or not self.within_chessboard_bounds(move_to):
            print("Invalid move. This move is outside the chessboard.")
            return False

        # location being moved to contains piece of same color.
        if self._chessboard[move_to] is not None and self._chessboard[move_to].get_color() == self._turn:
            print("Same colored piece is in destination. Unable to move here. Choose a different move.")
            return False

        # if move_from is empty, return false.
        if self._chessboard.get(move_from) is None:
            print("This location does not contain a piece.")
            return False

        # attempting to move opponents piece, return false.
        if self._chessboard.get(move_from).get_color() != self._turn:
            print(f"Wrong color, you are the {self._turn} pieces.")
            return False

        # legal move, place piece in move_to location.
        elif self._chessboard[move_from].valid_move(move_from, move_to, self._chessboard):
            # if not empty and not the same color, piece must be captured.
            if self._chessboard[move_to] is not None and self._chessboard.get(move_to).get_color() != self._turn:
                # if piece in move_to is king, game is over. update game state.
                if type(self._chessboard[move_to]) == King:
                    if self._chessboard[move_from].get_color() == "WHITE":
                        self._game_state = "WHITE_WON"
                    else:
                        self._game_state = "BLACK_WON"
                    print(self._game_state)

                # capture piece, update turn
                else:
                    print(f"{self._chessboard[move_to].get_color()} captured by {self._turn}")
                    del self._chessboard[move_to]

            # movement is valid, update board
            self._chessboard[move_to] = self._chessboard[move_from]
            self._chessboard[move_from] = None

            # print if move was successful
            print(f"Successful move by {self._turn}")

            # if white piece moved, it is black pieces turn (and vice versa)
            if self._turn == "WHITE":
                self._turn = "BLACK"
            else:
                self._turn = "WHITE"

            # add turn count

            return True

        else:
            return False

    def enter_fairy_piece(self, piece, square):
        """
        piece represents either the falcon or hunter (in each color).
        square is the piece user wants to place in a given square.
        turn will end if user opts to place a fairy piece.
        interact with display_board to update piece location
        """

        # check if piece can enter at given square, if not return false
        # otherwise place piece at that square

        # movement of fairy pieces:
        # falcon: moves forward like a bishop, and backward like a rook
        # hunter: moves forward like a rook and backward like a bishop

        # can only enter first fairy piece after losing Q, or N, or R, or B
        # can only enter second fairy piece after losing second piece Q, N, R, or B
        # (only 1 queen)

        pass

    def display_board(self):
        """
        prints out chessboard with pieces located depending on location
        Interacts with create_board for initial setup
        Useful for testing
        """
        for row in range(8, 0, -1):
            # row number
            print(row, end=' ')

            # loop
            for col in 'abcdefgh':
                # piece at current position
                piece = self._chessboard.get(col + str(row))

                print('|', end='')

                # if no piece in square, print empty space
                if piece is None:
                    print('   ', end=' ')
                # otherwise, display piece
                else:
                    print(f" {piece.get_symbol()}", end=' ')

            print('|')

        # column headers
        print('    a    b    c   d    e   f    g    h')

    def within_chessboard_bounds(self, pos):
        """
        Pos: a string that gets split up using indexes, piece position
        Checks to see if move is within the chessboard limits
        """
        col, row = pos[0], pos[1]
        # print(col, row)
        return 'a' <= str(col) <= 'h' and 1 <= int(row) <= 8


class Piece:
    """
    Parent class for each chess piece
    Establishes color and symbol of each piece
    Allows for color access using get_color
    Creates a valid_move for its subclasses to use.
    """
    def __init__(self, color, symbol):
        self._color = color
        self._symbol = symbol

    def get_color(self):
        """returns color of Piece"""
        return self._color

    def get_symbol(self):
        """Returns ASCII symbol for the Piece"""
        return self._symbol

    def valid_move(self, move_from, move_to, chessboard):
        """
        Validates piece movement
        """
        pass


class Pawn(Piece):
    """
    Creates Pawn object
    Inherits from Piece
    """
    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        move_from: the location a piece is moving from using strings (letter, number in string format ex. ('a5'))
        move_to: the location a piece is moving to using strings
        chessboard: represents chessboard itself and position of pieces
        Create movement for Pawns.
        Only move forward, can be 2 squares if first turn or 1 square for the rest of the game.
        Can't capture pieces in front, only diagonally
        Can't jump own color pieces
        """
        # creates tuple of square location using index 0 and index 1 of the string
        from_col, from_row = (move_from[0]), int(move_from[1])
        to_col, to_row = (move_to[0]), int(move_to[1])

        # white 'increases' by 1 towards 8
        if self.get_color() == 'WHITE':
            direction = 1
            start_row = 2
        # black 'decreases' by 1 towards 1
        else:
            direction = -1
            start_row = 7

        # if in starting spot, can move 2 spots forward
        if (from_row == start_row and from_col == to_col and to_row == from_row + 2 * direction and
                chessboard[move_to] is None):
            more_than_two = abs(to_row - from_row)
            if more_than_two > 2:
                return False
            return True

        # if not, only move one square forward
        if from_col == to_col and to_row == from_row + direction:
            if chessboard[move_to] is None:
                if abs(to_row - from_row) > 1 or (to_row - from_row) * direction <= 0:
                    return False
            # if square is not empty:
            if chessboard[move_to] is not None:
                return False

            return True

        # if opponent piece in diagonal square, can capture
        elif (ord(from_col) - ord(to_col) == 1 or ord(to_col) - ord(from_col) == 1) and to_row == from_row + direction:
            if chessboard[move_to] is not None and chessboard[move_to].get_color() != self._color:
                return True
        # Cannot jump own color pieces (in main Piece class)
        return False


class Rook(Piece):
    """
     Creates movement for Rooks.
     Inherits from Piece
    """

    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        move_from: the location a piece is moving from using strings (letter, number in string format ex. ('a5'))
        move_to: the location a piece is moving to using strings
        chessboard: represents chessboard itself and position of pieces
        Moves vertically and horizontally, not diagonally.
        Forwards and backwards, cannot jump own color pieces
        """
        # creates tuple of square location using index 0 and index 1 of the string
        # ord() converts character to its ASCII equivalent (stackoverflow)
        from_col, from_row = ord(move_from[0]), int(move_from[1])
        to_col, to_row = ord(move_to[0]), int(move_to[1])

        # column movement (vertical)
        if from_col == to_col:
            if from_row < to_row:
                move = 1
            else:
                move = -1
            for row in range(from_row + move, to_row, move):
                # if
                if chessboard[move_from[0] + str(row)] is not None:
                    return False
            return True

        # row movement (horizontal)
        elif from_row == to_row:
            if from_row < to_row:
                move = 1
            else:
                move = -1
            for col in range(from_col + move, to_col, move):
                # if
                if chessboard[col + from_row] is not None:
                    return False
            return True

        else:
            return False


class Knight(Piece):
    """
     Creates movement for Knights.
     Inherits from Piece
    """
    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        move_from: the location a piece is moving from using strings (letter, number in string format ex. ('a5'))
        move_to: the location a piece is moving to using strings
        chessboard: represents chessboard itself and position of pieces
        Moves in L-shape (2 squares in one direction and then 1 square left or right).
        Moves forwards and backwards, cannot jump own color pieces
        """
        # creates tuple of square location using index 0 and index 1 of the string
        # ord() converts character to its ASCII equivalent (stackoverflow)
        from_col, from_row = ord(move_from[0]), int(move_from[1])
        to_col, to_row = ord(move_to[0]), int(move_to[1])

        abs_row = abs(to_row - from_row)
        abs_col = abs(to_col - from_col)

        if abs_row == 2 and abs_col == 1:
            if chessboard[move_to] is None or chessboard[move_to].get_color() != self.get_color():
                return True
        elif abs_col == 2 and abs_row == 1:
            if chessboard[move_to] is None or chessboard[move_to].get_color() != self.get_color():
                return True
        return False


class Bishop(Piece):
    """
     Creates movement for Bishops.
     Inherits from Piece
    """
    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        move_from: the location a piece is moving from using strings (letter, number in string format ex. ('a5'))
        move_to: the location a piece is moving to using strings
        chessboard: represents chessboard itself and position of pieces
        Moves diagonally (in the shape of an x), cannot jump own color pieces
        Forward and backward
        """
        # creates tuple of square location using index 0 and index 1 of the string
        # ord() converts character to its ASCII equivalent (stackoverflow)
        from_col, from_row = ord(move_from[0]), int(move_from[1])
        to_col, to_row = ord(move_to[0]), int(move_to[1])

        abs_row = abs(to_row - from_row)
        abs_col = abs(to_col - from_col)

        if abs_row == abs_col:
            if to_row > from_row:
                row_direction = 1
            else:
                row_direction = -1
            if to_col > from_col:
                col_direction = 1
            else:
                col_direction = -1

            curr_col, curr_row = from_col + col_direction, from_row + row_direction
            while curr_col != to_col or curr_row != to_row:
                if chessboard[chr(curr_col) + str(curr_row)] is not None:
                    if chessboard[chr(curr_col) + str(curr_row)].get_color() == self.get_color():
                        return False
                    return True
                curr_col += col_direction
                curr_row += row_direction
            return True

        return False


class Queen(Piece):
    """
    Creates movement for Queens.
    Inherits from Piece
    """

    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        move_from: the location a piece is moving from using strings (letter, number in string format ex. ('a5'))
        move_to: the location a piece is moving to using strings
        chessboard: represents chessboard itself and position of pieces
        Move in any direction but can't jump over own color pieces.
        Diagonal like a Bishop
        Vertical and horizontal like a Rook
        """
        # creates tuple of square location using index 0 and index 1 of the string
        # ord() converts character to its ASCII equivalent (stackoverflow)
        from_col, from_row = ord(move_from[0]), int(move_from[1])
        to_col, to_row = ord(move_to[0]), int(move_to[1])

        abs_row = abs(to_row - from_row)
        abs_col = abs(to_col - from_col)

        # column movement (vertical)
        if from_col == to_col:
            if from_row < to_row:
                move = 1
            else:
                move = -1
            for row in range(from_row + move, to_row, move):
                # if
                if chessboard[move_from[0] + str(row)] is not None:
                    return False
            return True

        # row movement (horizontal)
        elif from_row == to_row:
            if from_row < to_row:
                move = 1
            else:
                move = -1
            for col in range(from_col + move, to_col, move):
                # if
                if chessboard[col + from_row] is not None:
                    return False
            return True

        # diagonal movement
        elif abs_row == abs_col:
            if to_row > from_row:
                row_direction = 1
            else:
                row_direction = -1
            if to_col > from_col:
                col_direction = 1
            else:
                col_direction = -1

            curr_col, curr_row = from_col + col_direction, from_row + row_direction
            while curr_col != to_col or curr_row != to_row:
                if chessboard[chr(curr_col) + str(curr_row)] is not None:
                    if chessboard[chr(curr_col) + str(curr_row)].get_color() == self.get_color():
                        return False
                    return True
                curr_col += col_direction
                curr_row += row_direction
            return True

        return False


class King(Piece):
    """
    Creates movement for Kings.
    Inherits from Piece
    """

    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        move_from: the location a piece is moving from using strings (letter, number in string format ex. ('a5'))
        move_to: the location a piece is moving to using strings
        chessboard: represents chessboard itself and position of pieces
        Move one square at a time in any direction, cannot jump own color pieces
        """
        # creates tuple of square location using index 0 and index 1 of the string
        # ord() converts character to its ASCII equivalent (stackoverflow)
        from_col, from_row = ord(move_from[0]), int(move_from[1])
        to_col, to_row = ord(move_to[0]), int(move_to[1])

        abs_row = abs(to_row - from_row)
        abs_col = abs(to_col - from_col)

        if abs_row <= 1 and abs_col <= 1:
            if chessboard[move_to] is None or chessboard[move_to].get_color() != self.get_color():
                return True


class Falcon(Piece):
    """
    Creates movement for Falcons.
    Inherits from Piece
    """

    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        Moves forward like a Bishop, backward like a Rook
        Cannot jump own color pieces
        """
    pass


class Hunter(Piece):
    """
    Creates movement for Hunters
    Inherits from Piece
    """

    def __init__(self, color, symbol):
        super().__init__(color, symbol)

    def valid_move(self, move_from, move_to, chessboard):
        """
        Moves forward like a Rook, backward like a Bishop
        Cannot jump own color pieces
        """
    pass


def main():
    """
    Testing function
    """
    game = ChessVar()
    game.get_game_state()
    game.make_move('d1', 'b3')

    game.display_board()
    print(game.get_turn())
    print(game.get_game_state())


if __name__ == '__main__':
    main()
