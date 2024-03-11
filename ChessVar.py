# Author: Ethan David Lee
# GitHub username: ethandavidlee
# Date: 2024/03/11
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
    def __init__(self, turn=0, game_state='UNFINISHED'):
        self._turn = turn
        self._game_state = game_state
        self._chessboard = Chessboard()

    def get_game_state(self):
        """
        Checks the state of the game and returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        return self._game_state

    def set_game_state(self):
        """
        Checks the state of the game and returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        for piece in self._chessboard.get_chessboard_dict()['taken_white']:
            if piece.get_piece_type() == 'king':
                self._game_state = 'BLACK_WON'
                return self._game_state
        for piece in self._chessboard.get_chessboard_dict()['taken_black']:
            if piece.get_piece_type() == 'king':
                self._game_state = 'WHITE_WON'
                return self._game_state
        self._game_state = 'UNFINISHED'
        return self._game_state

    def get_turn(self):
        """
        Returns the color associated with the turn order where an even numbered turn order means it's white's turn and
        an odd numbered turn order means it's black's turn.
        """
        if self._turn % 2 == 0:
            return 'white'
        else:
            return 'black'

    def get_chessboard(self):
        """
        Returns an instance of the Chessboard class.
        """
        return self._chessboard

    def turn_order(self):
        """
        Keeps track of turn order by incrementing turn by 1 and returning the variable with the new value.
        """
        self._turn += 1

    def make_move(self, current_position, new_position):
        """
        Moves the piece in current_position to the new_position if the move is legal, removing any captured piece,
            updating the game state (if necessary), and updating whose turn it is.
        If the indicated move from current_position to new_position is not legal, returns message for player to try
            again (or start new game if the game state is not 'UNFINISHED')
        Returns True if the move was made, along with a message prompting th next player's turn, and False if it was
            not, along with a message prompting the current player to try again.
        """
        if self.get_game_state() != 'UNFINISHED':
            return False
        if not self.valid_move(current_position, new_position):
            return False
        else:
            self._chessboard.chessboard_position(current_position, new_position)
            self.set_game_state()
            self.turn_order()
            return True

    def valid_move(self, current_position_str, new_position_str):
        """
        Takes the strings of the current and new position and checks that the proposed move from current position to
        new position is legal. Returns True or False accordingly.
        """
        current_piece = self._chessboard.get_chessboard_dict()[current_position_str]
        current_position_obj = BoardSquare(current_position_str)
        new_position_obj = BoardSquare(new_position_str)

        if not current_piece:
            return False

        if current_piece.get_color() != self.get_turn():
            return False

        if not new_position_obj.check_valid_square():
            return False  # new position is not a valid square

        if self._chessboard.get_chessboard_dict()[new_position_str]:
            new_piece_color = self._chessboard.get_chessboard_dict()[new_position_str].get_color()
            if new_piece_color == current_piece.get_color():
                return False  # cannot take own piece

        if not current_piece.valid_moves(current_position_obj, new_position_obj):
            return False  # piece cannot move from current to new

        if not self.valid_journey(current_position_obj, new_position_obj, current_piece):
            return False  # other pieces are interrupting the journey

        else:
            return True

    def valid_journey(self, current_position_obj, new_position_obj, current_piece):
        """
        Takes the current and new position instances of the BoardSquare class as current_position_obj and
        new_position_obj and the piece at the current position as current_piece. Checks that the piece can move from
        the current to new position without another piece being in the way. Returns True or False accordingly, via
        methods for horizontal, vertical and diagonal journeys.
        """
        current_row = current_position_obj.get_row()
        new_row = new_position_obj.get_row()
        current_column = current_position_obj.get_column()
        new_column = new_position_obj.get_column()

        if current_piece.get_piece_type() == 'knight':
            return True

        if current_row == new_row:
            return self.check_horizontal_journey(current_column, new_column, current_row)

        if current_column == new_column:
            return self.check_vertical_journey(current_row, new_row, current_column)

        else:
            return self.check_diagonal_journey(current_row, new_row, current_column, new_column)

    def check_horizontal_journey(self, current_column, new_column, current_row):
        """
        Checks all positions on the current row between the current column and the new column and returns False if any
        are occupied and True if they are empty.
        """
        if new_column > current_column:
            for column in range(current_column + 1, new_column):  # start, stop
                position = f'{chr(column + 96)}{current_row}'  # convert indices to coordinates
                if not self._chessboard.get_chessboard_dict()[position]:
                    continue
                else:
                    return False
            return True
        else:
            for column in range(new_column + 1, current_column):  # start, stop
                position = f'{chr(column + 96)}{current_row}'  # convert indices to coordinates
                if not self._chessboard.get_chessboard_dict()[position]:
                    continue
                else:
                    return False
            return True

    def check_vertical_journey(self, current_row, new_row, current_column):
        """
        Checks all positions on the current column between the current row and the new row and returns False if any are
        occupied and True if they are empty.
        """
        if new_row > current_row:
            for row in range(current_row + 1, new_row):  # start, stop
                position = f'{chr(current_column + 96)}{row}'  # convert indices to coordinates
                if not self._chessboard.get_chessboard_dict()[position]:
                    continue
                else:
                    return False
            return True
        else:
            for row in range(new_row + 1, current_row):  # start, stop
                position = f'{chr(current_column + 96)}{row}'  # convert indices to coordinates
                if not self._chessboard.get_chessboard_dict()[position]:
                    continue
                else:
                    return False
            return True

    def check_diagonal_journey(self, current_row, new_row, current_column, new_column):
        """
        Checks all positions on the diagonal from the current column and row to the new column and row and returns
        False if any are occupied and True if they are empty.
        """
        if new_row > current_row:  # moving up the board
            if new_column > current_column:  # moving right
                column_loop = current_column + 1
                for row in range(current_row+1, new_row):  # start, stop, step
                    position = f'{chr(column_loop + 96)}{row}'
                    column_loop += 1
                    if not self._chessboard.get_chessboard_dict()[position]:
                        continue
                    else:
                        return False
                return True

            else:  # moving left
                column_loop = current_column - 1
                for row in range(current_row+1, new_row):  # start, stop, step
                    position = f'{chr(column_loop + 96)}{row}'
                    column_loop -= 1
                    if not self._chessboard.get_chessboard_dict()[position]:
                        continue
                    else:
                        return False
                return True

        else:  # moving down the board
            if new_column > current_column:  # moving right
                column_loop = current_column + 1
                for row in range(current_row-1, new_row, -1):  # start, stop, step
                    position = f'{chr(column_loop + 96)}{row}'
                    column_loop += 1
                    if not self._chessboard.get_chessboard_dict()[position]:
                        continue
                    else:
                        return False
                return True

            else:  # moving left
                column_loop = current_column - 1
                for row in range(current_row-1, new_row, -1):  # start, stop, step
                    position = f'{chr(column_loop + 96)}{row}'
                    column_loop -= 1
                    if not self._chessboard.get_chessboard_dict()[position]:
                        continue
                    else:
                        return False
                return True

    def enter_fairy_piece(self, fairy_piece, entry_position):
        """
        Enters the given fairy_piece on the board at the given entry_position after validating the entry with the
        valid_fairy_enter method. Updates the turn and returns True if the entry was made and False if it was not.
        """
        if self.valid_fairy_enter(fairy_piece, entry_position):
            if fairy_piece == 'F':
                white_falcon = Falcon(color='white', name='F')
                self._chessboard.place_piece(white_falcon, entry_position)

                for piece in self._chessboard.get_chessboard_dict()['off_board_white']:
                    if piece.get_name() == fairy_piece:
                        fairy_piece_object = piece
                        off_board_list = self._chessboard.get_chessboard_dict()['off_board_white']
                        off_board_list.remove(fairy_piece_object)

            if fairy_piece == 'f':
                black_falcon = Falcon(color='black', name='f')
                self._chessboard.place_piece(black_falcon, entry_position)

                for piece in self._chessboard.get_chessboard_dict()['off_board_black']:
                    if piece.get_name() == fairy_piece:
                        fairy_piece_object = piece
                        off_board_list = self._chessboard.get_chessboard_dict()['off_board_black']
                        off_board_list.remove(fairy_piece_object)

            if fairy_piece == 'H':
                white_hunter = Hunter(color='white', name='H')
                self._chessboard.place_piece(white_hunter, entry_position)

                for piece in self._chessboard.get_chessboard_dict()['off_board_white']:
                    if piece.get_name() == fairy_piece:
                        fairy_piece_object = piece
                        off_board_list = self._chessboard.get_chessboard_dict()['off_board_white']
                        off_board_list.remove(fairy_piece_object)

            if fairy_piece == 'h':
                black_hunter = Hunter(color='black', name='h')
                self._chessboard.place_piece(black_hunter, entry_position)

                for piece in self._chessboard.get_chessboard_dict()['off_board_black']:
                    if piece.get_name() == fairy_piece:
                        fairy_piece_object = piece
                        off_board_list = self._chessboard.get_chessboard_dict()['off_board_black']
                        off_board_list.remove(fairy_piece_object)

            self.turn_order()
            return True

        else:
            return False

    def valid_fairy_enter(self, fairy_piece, entry_position):
        """
        Checks that the given fairy_piece can enter the board at the given entry_position. Returns True if the move is
        valid and False if it is not.
        """
        board_square = BoardSquare(entry_position)

        if self.get_game_state() != 'UNFINISHED':
            return False

        piece_color = None
        if fairy_piece == 'H' or fairy_piece == 'F':
            piece_color = 'white'
        if fairy_piece == 'f' or fairy_piece == 'h':
            piece_color = 'black'
        if self.get_turn() != piece_color:
            return False

        off_board_pieces = []
        if piece_color == 'white':
            for piece in self._chessboard.get_chessboard_dict()['off_board_white']:
                off_board_pieces.append(piece.get_name())
            if fairy_piece not in off_board_pieces:
                return False
        if piece_color == 'black':
            for piece in self._chessboard.get_chessboard_dict()['off_board_black']:
                off_board_pieces.append(piece.get_name())
            if fairy_piece not in off_board_pieces:
                return False

        entry_row = board_square.get_row()
        if piece_color == 'white':
            if entry_row != 1 and entry_row != 2:
                return False
        if piece_color == 'black':
            if entry_row != 7 and entry_row != 8:
                return False

        fairy_count = 0
        piece_count = 0
        if piece_color == 'white':
            for __ in self._chessboard.get_chessboard_dict()['off_board_white']:
                fairy_count += 1
            for piece in self._chessboard.get_chessboard_dict()['taken_white']:
                if isinstance(piece, ChessPiece) and piece.get_name() in ['R', 'N', 'B', 'Q']:
                    piece_count += 1
        if piece_color == 'black':
            for __ in self._chessboard.get_chessboard_dict()['off_board_black']:
                fairy_count += 1
            for piece in self._chessboard.get_chessboard_dict()['taken_black']:
                if isinstance(piece, ChessPiece) and piece.get_name() in ['r', 'n', 'b', 'q']:
                    piece_count += 1
        if fairy_count == 2 and piece_count == 0:
            return False
        if fairy_count == 1 and piece_count <= 1:
            return False
        if fairy_count == 0:
            return False

        if self._chessboard.get_chessboard_dict()[entry_position]:
            return False
        else:
            return True


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
        """
        Returns the square coordinate.
        """
        return self._square

    def get_column(self):
        """
        Returns the square's column as an integer.
        """
        column_alph = self._square[0].lower()
        column_num = ord(column_alph) - 96
        return column_num

    def get_row(self):
        """
        Returns the square's row as an integer.
        """
        row = int(self._square[1])
        return row

    def check_valid_square(self):
        """
        Checks that the square is valid by making sure that its row and column is within the board range and returns
        True or False accordingly.
        """
        if self.get_row() > 8 or self.get_row() < 1 or self.get_column() > 8 or self.get_column() < 1:
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
        """
        Returns the chess piece's color.
        """
        return self._color

    def get_piece_type(self):
        """
        Returns the chess piece's type.
        """
        return self._piece_type

    def get_name(self):
        """
        Returns the chess piece's name.
        """
        return self._name


class Rook(ChessPiece):
    """
    Represents a Rook (castle) chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get
    columns and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary when setting up the board. Communicates with ChessVar to share the pieces movement style.
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

        column_difference = abs(new_column - current_column)
        row_difference = abs(new_row - current_row)

        if column_difference == 0 and row_difference == 0:
            return False
        if new_column == current_column or new_row == current_row:
            return True
        else:
            return False


class Knight(ChessPiece):
    """
    Represents a Knight chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary when setting up the board. Communicates with ChessVar to share the pieces movement style.
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
    Represents a Bishop chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary when setting up the board. Communicates with ChessVar to share the pieces movement style.
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

        if column_difference == 0 and row_difference == 0:
            return False
        if column_difference == row_difference:
            return True
        else:
            return False


class Queen(ChessPiece):
    """
    Represents a Queen chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary when setting up the board. Communicates with ChessVar to share the pieces movement style.
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

        if column_difference == 0 and row_difference == 0:
            return False
        if new_column == current_column or new_row == current_row:
            return True
        if column_difference == row_difference:
            return True
        else:
            return False


class King(ChessPiece):
    """
    Represents a King chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary when setting up the board. Communicates with ChessVar to share the pieces movement style.
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
        if column_difference == 0 and row_difference == 0:
            return False
        else:
            return True


class Pawn(ChessPiece):
    """
    Represents a Pawn chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary when setting up the board. Communicates with ChessVar to share the pieces movement style.
    """
    def __init__(self, color, name, chessboard):
        super().__init__(color, "pawn", name)
        self._chessboard = chessboard

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
        row_difference = (new_row - current_row)

        # if there is a piece at the new square straight ahead (because pawns can't take forward)
        if column_difference == 0 and self._chessboard.get_chessboard_dict()[new_square.get_square()]:
            return False

        # if there is a piece diagonal one, the pawn can move and take it
        if column_difference == 1 and self._chessboard.get_chessboard_dict()[new_square.get_square()]:
            if self.get_color() == 'white' and row_difference == 1:
                return True
            if self.get_color() == 'black' and row_difference == -1:
                return True

        if self.get_color() == 'white':
            if current_square.get_row() == 2:
                if column_difference == 0 and (row_difference == 1 or row_difference == 2):
                    return True
                else:
                    return False
            else:
                if column_difference == 0 and row_difference == 1:
                    return True
                else:
                    return False

        else:  # black
            if current_square.get_row() == 7:
                if column_difference == 0 and (row_difference == -1 or row_difference == -2):
                    return True
                else:
                    return False
            else:
                if column_difference == 0 and row_difference == -1:
                    return True
                else:
                    return False


class Hunter(ChessPiece):
    """
    Represents a Hunter chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary off board positions when setting up the board and adding the fairy piece to the board proper
    via the enter_fairy_piece method of ChessVar. Communicates with ChessVar to share the pieces movement style.
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

        abs_column_difference = abs(new_column - current_column)
        row_difference = new_row - current_row
        abs_row_difference = abs(new_row - current_row)

        if self.get_color() == 'white':
            if row_difference > 0:  # if white moving forward
                if current_column == new_column:  # move like a rook
                    return True
                else:
                    return False
            else:  # if white moving backwards (or level)
                if abs_row_difference == abs_column_difference:  # move like a bishop
                    return True
                else:
                    return False
        else:  # black
            if row_difference < 0:  # if black moving forward
                if current_column == new_column:  # move like a rook
                    return True
                else:
                    return False
            else:  # if black moving backwards (or level)
                if abs_row_difference == abs_column_difference:  # move like a bishop
                    return True
                else:
                    return False


class Falcon(ChessPiece):
    """
    Represents a Falcon chess piece. Inherits from ChessPiece. Communicates with the BoardSquare class to get columns
    and rows to define the pieces movement style. Communicates with Chessboard for the pieces to be added to the
    chessboard dictionary off board positions when setting up the board and adding the fairy piece to the board proper
    via the enter_fairy_piece method of ChessVar. Communicates with ChessVar to share the pieces movement style.
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

        abs_column_difference = abs(new_column - current_column)
        row_difference = new_row - current_row
        abs_row_difference = abs(new_row - current_row)

        if self.get_color() == 'white':
            if row_difference > 0:  # if white moving forward
                if abs_row_difference == abs_column_difference:  # move like a bishop
                    return True
                else:
                    return False
            else:  # if white moving backwards
                if current_column == new_column:  # move like a rook
                    return True
                else:
                    return False
        else:
            if row_difference < 0:  # if black moving forward
                if abs_row_difference == abs_column_difference:  # move like a bishop
                    return True
                else:
                    return False
            else:  # if black moving backwards
                if current_column == new_column:  # move like a rook
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
        self._chessboard_dict = {}  # initialize dictionary that maps positions to pieces
        self.setup_new_game()  # initialize the board with pieces for the start of the game
        self._board_square = BoardSquare(None)

    def get_chessboard_dict(self):
        """
        Returns the chessboard dictionary.
        """
        return self._chessboard_dict

    def setup_new_game(self):
        """
        Sets up chess board for the start of the game.
        """
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

        white_pawn = Pawn(color='white', name='P', chessboard=self)
        self.place_piece(white_pawn, 'a2')
        self.place_piece(white_pawn, 'b2')
        self.place_piece(white_pawn, 'c2')
        self.place_piece(white_pawn, 'd2')
        self.place_piece(white_pawn, 'e2')
        self.place_piece(white_pawn, 'f2')
        self.place_piece(white_pawn, 'g2')
        self.place_piece(white_pawn, 'h2')

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

        black_pawn = Pawn(color='black', name='p', chessboard=self)
        self.place_piece(black_pawn, 'a7')
        self.place_piece(black_pawn, 'b7')
        self.place_piece(black_pawn, 'c7')
        self.place_piece(black_pawn, 'd7')
        self.place_piece(black_pawn, 'e7')
        self.place_piece(black_pawn, 'f7')
        self.place_piece(black_pawn, 'g7')
        self.place_piece(black_pawn, 'h7')

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

        self._chessboard_dict['off_board_white'] = []
        white_falcon = Falcon(color='white', name='F')
        self._chessboard_dict['off_board_white'].append(white_falcon)
        white_hunter = Hunter(color='white', name='H')
        self._chessboard_dict['off_board_white'].append(white_hunter)

        self._chessboard_dict['off_board_black'] = []
        black_falcon = Falcon(color='black', name='f')
        self._chessboard_dict['off_board_black'].append(black_falcon)
        black_hunter = Hunter(color='black', name='h')
        self._chessboard_dict['off_board_black'].append(black_hunter)

        self._chessboard_dict['taken_white'] = []
        self._chessboard_dict['taken_black'] = []

    def place_piece(self, chess_piece, position):
        """
        Places the chess piece on the board at the given position.
        """
        self._chessboard_dict[position] = chess_piece

    def remove_piece(self, position):
        """
        Removes the chess piece at the given position from the board.
        """
        self._chessboard_dict[position] = None

    def take_piece(self, chess_piece):
        """
        Takes a chess_piece object and adds it to the appropriate taken_white or taken_black list keys of the chessboard
        dictionary depending on the pieces color.
        """
        if chess_piece.get_color() == 'white':
            self._chessboard_dict['taken_white'].append(chess_piece)
        else:
            self._chessboard_dict['taken_black'].append(chess_piece)

    def chessboard_position(self, current_position, new_position):
        """
        Updates the position keys of the chessboard dictionary when a move is made. Removes any piece in the given
        new_position and adds it to the taken position key, and removes the piece in the given current_position and adds
        it to the new_position key. Returns True when the dictionary is updated.
        """
        # removes any piece at the new position from the board and adds it to the appropriate 'taken' list
        if self._chessboard_dict[new_position]:
            taken_piece = self._chessboard_dict[new_position]
            self.take_piece(taken_piece)
            self.remove_piece(new_position)

        # add the chess piece to the new position and removes from the old position
        chess_piece = self._chessboard_dict[current_position]
        self.place_piece(chess_piece, new_position)
        self.remove_piece(current_position)

    def show_chessboard(self):
        """
        Returns a readable chessboard for printing with each chess piece listed in its position.
        """
        columns = 8
        rows = 8
        chessboard_representation = ""
        for row in range(rows - 1, -1, -1):  # iterate through in reverse order (start, stop, step)
            for column in range(columns):
                position = f'{chr(column + 97)}{row + 1}'  # Convert indices to coordinates
                piece = self._chessboard_dict[position]
                if piece:
                    chessboard_representation += f'{piece.get_name()}'
                else:
                    chessboard_representation += '-'
                chessboard_representation += " "
            chessboard_representation += "\n"  # insert a new line after each row
        return chessboard_representation
