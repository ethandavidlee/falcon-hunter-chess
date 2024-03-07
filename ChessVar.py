# Author: Ethan David Lee
# GitHub username: ethandavidlee
# Date: 2024/03/07
# Description: Program for a playable chess game variation called Falcon-Hunter Chess with standard chess rules, except
#           there is no check or checkmate, castling, en passant, or pawn promotion, and the addition of two pieces, the
#           Falcon and Hunter, with special rules for each. Falcons move forward like a bishop and backward like a rook,
#           while Hunters move forward like a rook and backward like a bishop. The Falcon and Hunter start the game off
#           the board and may be entered once a player loses their queen, a rook, a bishop, or a knight. Entering the
#           uses the players turn. The second 'fairy' piece may be entered any time after the player loses their second
#           queen, rook, bishop, or knight.

class ChessVar:
    """
    Represents a game of Falcon-Hunter Chess with a turn counter, managing the game's operation and movement of pieces.
    Communicates with ChessPiece and its subclasses to check proposed moves are valid for the chess pieces. Communicates
    with Chessboard to provide board information and receive updates to the board. Communicates with BoardSquare to
    check any proposed move is to a position on the board.
    """
    def __init__(self, turn=0):
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS:
        # Initializes the ChessVar class with the turn counter set to 0
        # Creates the chessboard with pieces in place by creating an instance of the Chessboard class that in turn sets
        # up the board for the beginning of the game so methods in the class can move and validate pieces.
        self._turn = turn
        chessboard = Chessboard()


    def get_game_state(self):
        """
        Checks the state of the game and returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS:
        # Checks to see if the white king piece is on the board by iterating over each square and returns and prints
        # 'BLACK_WON' if it isn't.
        # Checks to see if the black king piece is on the board by iterating over each square and returns and prints
        # 'WHITE_WON' if it isn't.
        # If both the black and white king pieces are on the board, returns 'UNFINISHED'
        pass

    def get_turn(self):
        """
        Returns the integer associated with the turn order where an even number means it's white's turn and an odd
        number means it's black's turn.
        """
        return self._turn

    def turn_order(self):
        """
        Keeps track of turn order by incrementing turn by 1 and returning the variable with the new value.
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS:
        # gets the turn variable using the getter method and increments it by 1
        pass

    def make_move(self, current_position, new_position):
        """
        Moves the piece in current_position to the new_position if the move is legal, removing any captured piece,
            updating the game state (if necessary), and updating whose turn it is.
        If the indicated move from current_position to new_position is not legal, returns message for player to try
            again (or start new game if the game state is not 'UNFINISHED')
        Returns True if the move was made, along with a message prompting th next player's turn, and False if it was
            not, along with a message prompting the current player to try again.
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS:
        # Checks if move is not legal by calling valid_move and checking that the return is False and calling
        #   get_game_state and checking if the return is WHITE_WON or BLACK_WON
        # If move is not legal, returns False
        # Else move is legal and the method:
        #   Makes the indicated move and removes any captured piece using the chessboard_positions method in the
        #       Chessboard class to update the chessboard dictionary
        #   Updates the game state if necessary by calling get_game_state
        #   Updates whose turn it is using the turn_order method
        #   Returns True and a message prompting the next player to make their move
        pass

    def valid_move(self, current_position, new_position):
        """
        Checks that the proposed move from current_position to new_position is legal. Returns True or False accordingly.
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS:
        # Check to see if the piece at the current_position is the current user's color
        # Check to see if the new_position is on the board using the check_valid_square method of the BoardSquare class
        # Check to see if the proposed move is valid for the piece in that position using the valid_moves method of the
        #   corresponding subclass of ChessPiece
        # Check to see if there are any pieces in the way that will stop the move from completing by checking each
        #   square in the chessboard dictionary that the piece will move through on its journey from current_position
        #   to new_position using
        # If the move is valid returns True
        # If the move is not valid returns False
        pass

    def enter_fairy_piece(self, fairy_piece, entry_position):
        """
        Enters the given fairy_piece on the board at the given entry_position after validating the entry with the
        valid_fairy_enter method. Updates the turn and returns True if the entry was made and False if it was not.
        """
        # If the entry is valid:
        #   Use the place_piece method in the Chessboard class to enter the fairy_piece at the entry_position
        #   Use the turn_order method to update whose turn it is
        #   Return True
        # If the entry is not valid:
        #   Return False
        pass

    def valid_fairy_enter(self, fairy_piece, entry_position):
        """
        Checks that the given fairy_piece can enter the board at the given entry_position. Returns True if the move is
        valid and False if it is not.
        """
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS:
        # Checks that the fairy_piece can enter by:
        #   Checking that the game status is UNFINISHED
        #   Checking that the proposed piece is of the player whose turn it is by calling get_turn
        #   Looking in the off_board's key of the chessboard dictionary to check piece has not already been entered
        #   Checking that the provided entry_position is within that color's first two rows using the get_row method of
        #       the BoardSquare class and checking that it is = to 1 or 2 for white and 7 or 8 for black.
        #   Iterating over the 'off_board' key in the chessboard dictionary to see how many fairy pieces are present.
        #       If there are 2, iterate over the list of pieces in the color's taken key of chessboard dictionary in the
        #           Chessboard class. If the list does not contain a queen, a rook, a bishop, or a knight, the entry is
        #           not legal.
        #       If the is 1, do the same thing but look for at least two of the high level pieces.
        #   Looking in entry_position's key of the chessboard dictionary to check it is None
        # Returns False if the entry in not legal
        # Otherwise returns True
        pass


class BoardSquare:
    """
    Represents a single square of the chessboard with a coordinate string that can be break down as a row and a column.
    Communicates with the ChessPiece classes and subclasses to receive the coordinate and provide the square's column
    and row, as well as the ChessBoard class. Communicates with the ChessVar class to ensure any potential new_square
    is part of the board.
    """
    def __init__(self, square):
        self._square = square

    def get_square(self):
        """Returns the square coordinate."""
        return self._square

    def set_square(self, square):
        """Receives a coordinate, checks that it is valid, and returns the coordinate as a square object."""
        if not self.check_valid_square(square):
            return False
        else:
            self._square = square

    def get_column(self):
        """Returns the square's column as a number."""
        column_alph = self._square[0].lower()
        column_num = ord(column_alph) - 96
        return column_num

    def get_row(self):
        """Returns the square's row."""
        row = int(self._square[1])
        return row

    def check_valid_square(self):
        """Checks that the square is valid by making sure that its row and column is within the board range and returns
         True or False accordingly."""
        if self.get_row() > 8 or self.get_row() < 1:
            return False
        elif self.get_column() > 8 or self.get_column() < 1:
            return False
        else:
            return True


class ChessPiece:
    """
    Represents a ChessPiece with a color and piece_type. Acts as a parent class for all piece type subclasses.
    Communicates with the Chessboard and ChessVar classes to provide the color and move habits of the piece in any
    proposed position on the board.
    """
    def __init__(self, color, piece_type, name):
        self._color = color
        self._piece_type = piece_type
        self._name = name

    def get_color(self):
        """Returns the chess piece's color"""
        return self._color

    def get_piece_type(self):
        """Returns the chess piece's type"""
        return self._piece_type

    def get_name(self):
        """Returns the chess piece's type"""
        return self._name


class Rook(ChessPiece):
    """
    Represents a Rook (castle) chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns and
    rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """
    def __init__(self, color, name):
        super().__init__(color, "rook", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of the rook/castle piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        if new_column == current_column or new_row == current_row:
            return True
        else:
            return False


class Knight(ChessPiece):
    """
    Represents a Knight chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """
    def __init__(self, color, name):
        super().__init__(color, "knight", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of the knight piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if column_difference == 1 and row_difference == 2 or column_difference == 2 and row_difference == 1:
            return True
        else:
            return False


class Bishop(ChessPiece):
    """
    Represents a Bishop chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns and
    rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """
    def __init__(self, color, name):
        super().__init__(color, "bishop", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of the bishop piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if column_difference == row_difference:
            return True
        else:
            return False


class Queen(ChessPiece):
    """
    Represents a Queen chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns and
    rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """
    def __init__(self, color, name):
        super().__init__(color, "queen", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of the queen piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if new_column == current_column or new_row == current_row:
            return True
        elif column_difference == row_difference:
            return True
        else:
            return False


class King(ChessPiece):
    """
    Represents a King chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns and
    rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """
    def __init__(self, color, name):
        super().__init__(color, "king", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of the king piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if column_difference > 1 or row_difference > 1:
            return False
        else:
            return True


class Pawn(ChessPiece):
    """
    Represents a Pawn chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns and
    rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """
    def __init__(self, color, name):
        super().__init__(color, "pawn", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of a pawn piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if (self.get_color() == 'white' and current_square.get_row() == 2 or self.get_color() == 'black' and
                current_square.get_row() == 7):
            if column_difference == 0 and row_difference == 1 or 2:
                return True
            else:
                return False
        else:
            if column_difference == 0 and row_difference == 1:
                return True
            else:
                return False


class Hunter(ChessPiece):
    """
    Represents a Hunter chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns and
    rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """

    def __init__(self, color, name):
        super().__init__(color, "hunter", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of the hunter piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if self.get_color() == 'white':
            if new_column - current_column >= 0:  # if white moving forward
                if new_column == current_column or new_row == current_row:  # move like a rook
                    return True
                else:
                    return False
            else:  # if white moving backwards
                if column_difference == row_difference:  # move like a bishop
                    return True
                else:
                    return False
        else:
            if new_column - current_column <= 0:  # if black moving forward
                if new_column == current_column or new_row == current_row:  # move like a rook
                    return True
                else:
                    return False
            else:  # if black moving backwards
                if column_difference == row_difference:  # move like a bishop
                    return True
                else:
                    return False


class Falcon(ChessPiece):
    """
    Represents a Falcon chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns and
    rows to define the pieces movement methods. Communicates with Chessboard for to be added to the chessboard
    dictionary at the relevant position key. Communicates with ChessVar to share the pieces movement methodology.
    """

    def __init__(self, color, name):
        super().__init__(color, "falcon", name)

    def valid_moves(self, current_square, new_square):
        """
        Defines the movement method of the falcon piece. Returns True if the proposed move from current_square to
        new_square is valid for the piece type. Returns False if the proposed move is not valid.
        """
        current_column = current_square.get_column()
        current_row = current_square.get_row()

        new_column = new_square.get_column()
        new_row = new_square.get_row()

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if self.get_color() == 'white':
            if new_column - current_column >= 0:  # if white moving forward
                if column_difference == row_difference:  # move like a bishop
                    return True
                else:
                    return False
            else:  # if white moving backwards
                if new_column == current_column or new_row == current_row:  # move like a rook
                    return True
                else:
                    return False
        else:
            if new_column - current_column <= 0:  # if black moving forward
                if column_difference == row_difference:  # move like a bishop
                    return True
                else:
                    return False
            else:  # if black moving backwards
                if new_column == current_column or new_row == current_row:  # move like a rook
                    return True
                else:
                    return False


class Chessboard:
    """
    Represents the entire chess board and manages each position on the board. Communicates with ChessPiece and its
    subclasses to place chess pieces on the board in a chessboard dictionary with coordinates as the keys. Communicates
    with ChessVar to provide board information and receive updates to the board. Communicates with BoardSquare to get
    and set the columns and rows of each position on the board.
    """
    def __init__(self):
        self._chessboard = {
            'off_board_white': [],
            'off_board_black': [],
            'taken_white': [],
            'taken_black': []
        }  # initialize dictionary that maps positions to pieces
        self.setup_new_game()  # initialize the board with pieces for the start of the game

    def get_chessboard(self):
        return self._chessboard

    def setup_new_game(self):
        """Sets up chess board for the start of the game"""
        white_rook = Rook(color='white', name='R')
        self.place_piece(white_rook, 'a1')
        white_knight = Knight(color='white', name='N')
        self.place_piece(white_knight, 'b1')
        white_bishop = Bishop(color='white', name='B')
        self.place_piece(white_bishop, 'c1')
        white_queen = Queen(color='white', name='Q')
        self.place_piece(white_queen, 'd1')
        white_king = King(color='white', name='K')
        self.place_piece(white_king, 'e1')
        self.place_piece(white_bishop, 'f1')
        self.place_piece(white_knight, 'g1')
        self.place_piece(white_rook, 'h1')

        P = Pawn(color='white', name='P')
        self.place_piece(P, 'a2')
        self.place_piece(P, 'b2')
        self.place_piece(P, 'c2')
        self.place_piece(P, 'd2')
        self.place_piece(P, 'e2')
        self.place_piece(P, 'f2')
        self.place_piece(P, 'g2')
        self.place_piece(P, 'h2')

        self.place_piece(None, 'a3')
        self.place_piece(None, 'b3')
        self.place_piece(None, 'c3')
        self.place_piece(None, 'd3')
        self.place_piece(None, 'e3')
        self.place_piece(None, 'f3')
        self.place_piece(None, 'g3')
        self.place_piece(None, 'h3')

        self.place_piece(None, 'a4')
        self.place_piece(None, 'b4')
        self.place_piece(None, 'c4')
        self.place_piece(None, 'd4')
        self.place_piece(None, 'e4')
        self.place_piece(None, 'f4')
        self.place_piece(None, 'g4')
        self.place_piece(None, 'h4')

        self.place_piece(None, 'a5')
        self.place_piece(None, 'b5')
        self.place_piece(None, 'c5')
        self.place_piece(None, 'd5')
        self.place_piece(None, 'e5')
        self.place_piece(None, 'f5')
        self.place_piece(None, 'g5')
        self.place_piece(None, 'h5')

        self.place_piece(None, 'a6')
        self.place_piece(None, 'b6')
        self.place_piece(None, 'c6')
        self.place_piece(None, 'd6')
        self.place_piece(None, 'e6')
        self.place_piece(None, 'f6')
        self.place_piece(None, 'g6')
        self.place_piece(None, 'h6')

        pawn = Pawn(color='black', name='p')
        self.place_piece(pawn, 'a7')
        self.place_piece(pawn, 'b7')
        self.place_piece(pawn, 'c7')
        self.place_piece(pawn, 'd7')
        self.place_piece(pawn, 'e7')
        self.place_piece(pawn, 'f7')
        self.place_piece(pawn, 'g7')
        self.place_piece(pawn, 'h7')

        black_rook = Rook(color='black', name='r')
        self.place_piece(black_rook, 'a8')
        black_knight = Knight(color='black', name='n')
        self.place_piece(black_knight, 'b8')
        black_bishop = Bishop(color='black', name='b')
        self.place_piece(black_bishop, 'c8')
        black_queen = Queen(color='black', name='q')
        self.place_piece(black_queen, 'd8')
        black_king = King(color='black', name='k')
        self.place_piece(black_king, 'e8')
        self.place_piece(black_bishop, 'f8')
        self.place_piece(black_knight, 'g8')
        self.place_piece(black_rook, 'h8')

        self._chessboard['off_board_white'] = []
        white_falcon = Falcon(color='white', name='F')
        self._chessboard['off_board_white'].append(white_falcon)
        white_hunter = Falcon(color='white', name='H')
        self._chessboard['off_board_white'].append(white_hunter)
        self._chessboard['off_board_black'] = []
        black_falcon = Falcon(color='black', name='f')
        self._chessboard['off_board_black'].append(black_falcon)
        black_hunter = Falcon(color='black', name='h')
        self._chessboard['off_board_black'].append(black_hunter)

        self._chessboard['taken_white'] = []
        self._chessboard['taken_black'] = []


    def take_piece(self, chess_piece, position=None):
        if position == None:
            if chess_piece.get_color() == 'white':
                self._chessboard['taken_white'].append(chess_piece)
            else:
                self._chessboard['taken_black'].append(chess_piece)
        else:
            pass

    def place_piece(self, chess_piece, position):
        """Places the chess piece on the board at the given position."""
        self._chessboard[position] = chess_piece

    def chessboard_position(self, current_position, new_position):
        """Updates the position keys of the chessboard dictionary when a move is made. Removes any piece in the given
        new_position and adds it to the taken position key, and removes the piece in the given current_position and adds
        it to the new_position key. Returns True when the dictionary is updated."""
        # DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIO:
        # Takes the self._chessboard dictionary and updates it every time a move is made by:
        #   adding any piece at the new position key to the list at the 'taken' key of the chessboard dictionary
        #   removing any piece at the new position key (we have already checked that this piece is the opposing color)
        #       using the remove_piece method
        #   adding the moving piece to the new position key using the place_piece method
        #   removing the moving piece from the old position key using the remove_piece method
        pass

    def show_chessboard(self):
        """Returns a readable chess board for printing with each chess piece listed in its position."""
        columns = 8
        rows = 8
        chessboard_representation = ""
        for row in range(rows - 1, -1, -1):  # iterate through in reverse order (start, stop, step)
            for column in range(columns):
                position = BoardSquare(f'{chr(column + 97)}{row + 1}')  # Convert indices to coordinates
                piece = self._chessboard[position.get_square()]
                if piece:
                    chessboard_representation += f'{piece.get_name()}'
                else:
                    chessboard_representation += '-'
                chessboard_representation += " "
            chessboard_representation += "\n"  # insert a new line after each row
        return chessboard_representation


chessboard = Chessboard()
my_chessboard = chessboard.show_chessboard()
print(my_chessboard)
my_off_board_whites = [piece.get_name() for piece in chessboard.get_chessboard()['off_board_white']]
my_off_board_blacks = [piece.get_name() for piece in chessboard.get_chessboard()['off_board_black']]
print('Offboard: ' + str(my_off_board_whites) + ' ' + str(my_off_board_blacks))

taken_white_object = chessboard.get_chessboard()['taken_white']
if taken_white_object:
    taken_white_name = taken_white_object.get_name()
else:
    taken_white_name = 'None'
print('Taken White Pieces: ' + taken_white_name)
taken_black_object = chessboard.get_chessboard()['taken_black']
if taken_black_object:
    taken_black_names = (piece.get_name() for piece in taken_black_object)
else:
    taken_black_name = 'None'
print('Taken Black Pieces: ' + taken_black_name)
