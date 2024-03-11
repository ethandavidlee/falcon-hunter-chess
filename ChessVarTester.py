from ChessVar import *
import unittest


class TestHunterPiece(unittest.TestCase):
    def setUp(self):
        # Initialize the ChessGame before each test
        self._game = ChessVar()

    def test_valid_moves(self):
        """Tests a valid set of initial moves before testing the entrance and movement of a Hunter fairy piece and
        printing the final board and off board positions."""
        # Taken from Magnus Carlsen vs. Alberto Santos Flores game https://www.chess.com/games/view/16878807
        self.assertTrue(self._game.make_move('e2', 'e4'))
        self.assertTrue(self._game.make_move('e7', 'e6'))
        self.assertTrue(self._game.make_move('b2', 'b3'))
        self.assertTrue(self._game.make_move('d7', 'd5'))
        self.assertTrue(self._game.make_move('c1', 'b2'))
        self.assertTrue(self._game.make_move('d5', 'e4'))
        self.assertTrue(self._game.make_move('b1', 'c3'))
        self.assertTrue(self._game.make_move('g8', 'f6'))
        self.assertTrue(self._game.make_move('g2', 'g4'))
        self.assertTrue(self._game.make_move('h7', 'h6'))
        self.assertTrue(self._game.make_move('d1', 'e2'))
        self.assertTrue(self._game.make_move('f8', 'b4'))
        self.assertTrue(self._game.make_move('a1', 'd1'))
        self._game.get_chessboard().remove_piece('e1')
        white_king = King(color='white', name='K')
        self._game.get_chessboard().place_piece(white_king, 'c1')  # castled
        self.assertTrue(self._game.make_move('d8', 'e7'))
        self.assertTrue(self._game.make_move('c1', 'b1'))
        self.assertTrue(self._game.make_move('b4', 'a3'))
        self.assertTrue(self._game.make_move('b2', 'a1'))
        self.assertTrue(self._game.make_move('a7', 'a5'))
        self.assertTrue(self._game.make_move('c3', 'e4'))
        self.assertTrue(self._game.make_move('f6', 'e4'))
        self.assertTrue(self._game.make_move('e2', 'e4'))
        self.assertTrue(self._game.make_move('a5', 'a4'))
        self.assertTrue(self._game.make_move('a1', 'g7'))
        self.assertTrue(self._game.make_move('a4', 'b3'))
        self.assertTrue(self._game.make_move('e4', 'h7'))

        # test hunter entrance
        self.assertTrue(self._game.enter_fairy_piece('h', 'd8'))
        self.assertTrue(self._game.enter_fairy_piece('H', 'e1'))

        # test hunter can move forward like a rook
        self.assertTrue(self._game.make_move('d8', 'd4'))
        self.assertTrue(self._game.make_move('e1', 'e5'))

        # test hunter can't move backwards like a rook
        self.assertFalse(self._game.make_move('d4', 'd8'))
        self._game.make_move('h8', 'g8')
        self.assertFalse(self._game.make_move('e5', 'e1'))
        self._game.make_move('d1', 'c1')

        # test can't take own self
        self.assertFalse(self._game.make_move('d4', 'd4'))
        self._game.make_move('g8', 'h8')
        self.assertFalse(self._game.make_move('e5', 'e5'))
        self._game.make_move('c1', 'd1')

        # test can't move sideways
        self.assertFalse(self._game.make_move('d4', 'a4'))
        self._game.make_move('h8', 'g8')
        self.assertFalse(self._game.make_move('e5', 'h5'))
        self._game.make_move('d1', 'c1')

        # test hunter can move backwards diagonally
        self.assertTrue(self._game.make_move('d4', 'a7'))
        self.assertTrue(self._game.make_move('e5', 'a1'))

        # test hunter can't move forwards diagonally
        self.assertFalse(self._game.make_move('a7', 'd4'))
        self._game.make_move('g8', 'h8')
        self.assertFalse(self._game.make_move('a1', 'e5'))
        self._game.make_move('c1', 'd1')

        my_chessboard = self._game.get_chessboard().show_chessboard()
        print(my_chessboard)
        my_off_board_whites = [piece.get_name() for piece in
                               self._game.get_chessboard().get_chessboard_dict()['off_board_white']]
        my_off_board_blacks = [piece.get_name() for piece in
                               self._game.get_chessboard().get_chessboard_dict()['off_board_black']]
        print('Off_board: ' + str(my_off_board_whites) + ' ' + str(my_off_board_blacks))

        taken_white_object = self._game.get_chessboard().get_chessboard_dict()['taken_white']
        if taken_white_object:
            taken_white_names = []
            for piece in taken_white_object:
                taken_white_names.append(piece.get_name())
        else:
            taken_white_names = 'None'
        print('Taken White Pieces: ' + str(taken_white_names))

        taken_black_object = self._game.get_chessboard().get_chessboard_dict()['taken_black']
        if taken_black_object:
            taken_black_names = []
            for piece in taken_black_object:
                taken_black_names.append(piece.get_name())
        else:
            taken_black_names = 'None'
        print('Taken Black Pieces: ' + str(taken_black_names))


class TestFalconPiece(unittest.TestCase):
    def setUp(self):
        # Initialize the ChessGame before each test
        self._game = ChessVar()

    def test_valid_moves(self):
        """Tests a valid set of initial moves before testing the entrance and movement of a Hunter fairy piece and
        printing the final board and off board positions."""
        # Taken from Magnus Carlsen vs. Alberto Santos Flores game https://www.chess.com/games/view/16878807
        self.assertTrue(self._game.make_move('e2', 'e4'))
        self.assertTrue(self._game.make_move('e7', 'e6'))
        self.assertTrue(self._game.make_move('b2', 'b3'))
        self.assertTrue(self._game.make_move('d7', 'd5'))
        self.assertTrue(self._game.make_move('c1', 'b2'))
        self.assertTrue(self._game.make_move('d5', 'e4'))
        self.assertTrue(self._game.make_move('b1', 'c3'))
        self.assertTrue(self._game.make_move('g8', 'f6'))
        self.assertTrue(self._game.make_move('g2', 'g4'))
        self.assertTrue(self._game.make_move('h7', 'h6'))
        self.assertTrue(self._game.make_move('d1', 'e2'))
        self.assertTrue(self._game.make_move('f8', 'b4'))
        self.assertTrue(self._game.make_move('a1', 'd1'))
        self._game.get_chessboard().remove_piece('e1')
        white_king = King(color='white', name='K')
        self._game.get_chessboard().place_piece(white_king, 'c1')  # castled
        self.assertTrue(self._game.make_move('d8', 'e7'))
        self.assertTrue(self._game.make_move('c1', 'b1'))
        self.assertTrue(self._game.make_move('b4', 'a3'))
        self.assertTrue(self._game.make_move('b2', 'a1'))
        self.assertTrue(self._game.make_move('a7', 'a5'))
        self.assertTrue(self._game.make_move('c3', 'e4'))
        self.assertTrue(self._game.make_move('f6', 'e4'))
        self.assertTrue(self._game.make_move('e2', 'e4'))
        self.assertTrue(self._game.make_move('a5', 'a4'))
        self.assertTrue(self._game.make_move('a1', 'g7'))
        self.assertTrue(self._game.make_move('a4', 'b3'))
        self.assertTrue(self._game.make_move('e4', 'h7'))

        # test hunter entrance
        self.assertTrue(self._game.enter_fairy_piece('f', 'd7'))
        self.assertTrue(self._game.enter_fairy_piece('F', 'e2'))

        # test falcon can move forward like a bishop
        self.assertTrue(self._game.make_move('d7', 'a4'))
        self.assertTrue(self._game.make_move('e2', 'c4'))

        # test falcon can't move backwards like a bishop
        self.assertFalse(self._game.make_move('a4', 'd7'))
        self._game.make_move('h8', 'g8')
        self.assertFalse(self._game.make_move('c4', 'e2'))
        self._game.make_move('d1', 'c1')

        # test can't take own self
        self.assertFalse(self._game.make_move('a4', 'a4'))
        self._game.make_move('g8', 'h8')
        self.assertFalse(self._game.make_move('c4', 'c4'))
        self._game.make_move('c1', 'd1')

        # test can't move sideways
        self.assertFalse(self._game.make_move('a4', 'b4'))
        self._game.make_move('h8', 'g8')
        self.assertFalse(self._game.make_move('c4', 'd4'))
        self._game.make_move('d1', 'c1')

        # test falcon can move backwards like a rook
        self.assertTrue(self._game.make_move('a4', 'a7'))
        self.assertTrue(self._game.make_move('c4', 'c3'))

        # test hunter can't move forwards like a rook
        self.assertFalse(self._game.make_move('a7', 'a4'))
        self._game.make_move('g8', 'h8')
        self.assertFalse(self._game.make_move('c3', 'c4'))
        self._game.make_move('c1', 'd1')

        my_chessboard = self._game.get_chessboard().show_chessboard()
        print(my_chessboard)
        my_off_board_whites = [piece.get_name() for piece in
                               self._game.get_chessboard().get_chessboard_dict()['off_board_white']]
        my_off_board_blacks = [piece.get_name() for piece in
                               self._game.get_chessboard().get_chessboard_dict()['off_board_black']]
        print('Off_board: ' + str(my_off_board_whites) + ' ' + str(my_off_board_blacks))

        taken_white_object = self._game.get_chessboard().get_chessboard_dict()['taken_white']
        if taken_white_object:
            taken_white_names = []
            for piece in taken_white_object:
                taken_white_names.append(piece.get_name())
        else:
            taken_white_names = 'None'
        print('Taken White Pieces: ' + str(taken_white_names))

        taken_black_object = self._game.get_chessboard().get_chessboard_dict()['taken_black']
        if taken_black_object:
            taken_black_names = []
            for piece in taken_black_object:
                taken_black_names.append(piece.get_name())
        else:
            taken_black_names = 'None'
        print('Taken Black Pieces: ' + str(taken_black_names))


class TestSecondEnter(unittest.TestCase):
    def setUp(self):
        # Initialize the ChessGame before each test
        self._game = ChessVar()

    def test_valid_moves(self):
        """Tests a valid set of initial moves before testing the entrance and second entrance of fairy pieces."""
        # Taken from Magnus Carlsen vs. Alberto Santos Flores game https://www.chess.com/games/view/16878807
        self.assertTrue(self._game.make_move('e2', 'e4'))
        self.assertTrue(self._game.make_move('e7', 'e6'))
        self.assertTrue(self._game.make_move('b2', 'b3'))
        self.assertTrue(self._game.make_move('d7', 'd5'))
        self.assertTrue(self._game.make_move('c1', 'b2'))
        self.assertTrue(self._game.make_move('d5', 'e4'))
        self.assertTrue(self._game.make_move('b1', 'c3'))
        self.assertTrue(self._game.make_move('g8', 'f6'))
        self.assertTrue(self._game.make_move('g2', 'g4'))
        self.assertTrue(self._game.make_move('h7', 'h6'))
        self.assertTrue(self._game.make_move('d1', 'e2'))
        self.assertTrue(self._game.make_move('f8', 'b4'))
        self.assertTrue(self._game.make_move('a1', 'd1'))
        self._game.get_chessboard().remove_piece('e1')
        white_king = King(color='white', name='K')
        self._game.get_chessboard().place_piece(white_king, 'c1')  # castled
        self.assertTrue(self._game.make_move('d8', 'e7'))
        self.assertTrue(self._game.make_move('c1', 'b1'))
        self.assertTrue(self._game.make_move('b4', 'a3'))
        self.assertTrue(self._game.make_move('b2', 'a1'))
        self.assertTrue(self._game.make_move('a7', 'a5'))
        self.assertTrue(self._game.make_move('c3', 'e4'))
        self.assertTrue(self._game.make_move('f6', 'e4'))
        self.assertTrue(self._game.make_move('e2', 'e4'))
        self.assertTrue(self._game.make_move('a5', 'a4'))
        self.assertTrue(self._game.make_move('a1', 'g7'))
        self.assertTrue(self._game.make_move('a4', 'b3'))
        self.assertTrue(self._game.make_move('e4', 'h7'))

        # test hunter entrance
        self.assertTrue(self._game.enter_fairy_piece('h', 'd8'))
        self.assertTrue(self._game.enter_fairy_piece('H', 'e1'))

        # test falcon entrance with one major piece taken
        self.assertFalse(self._game.enter_fairy_piece('f', 'a7'))
        self._game.make_move('e8', 'f8')
        self.assertFalse(self._game.enter_fairy_piece('F', 'a1'))
        self._game.make_move('f1', 'd3')

        # test falcon entrance with two major pieces taken
        self._game.make_move('h8', 'h7')
        self._game.make_move('d3', 'h7')
        self.assertTrue(self._game.enter_fairy_piece('f', 'a7'))
        self.assertTrue(self._game.enter_fairy_piece('F', 'a1'))

        my_chessboard = self._game.get_chessboard().show_chessboard()
        print(my_chessboard)
        my_off_board_whites = [piece.get_name() for piece in
                               self._game.get_chessboard().get_chessboard_dict()['off_board_white']]
        my_off_board_blacks = [piece.get_name() for piece in
                               self._game.get_chessboard().get_chessboard_dict()['off_board_black']]
        print('Off_board: ' + str(my_off_board_whites) + ' ' + str(my_off_board_blacks))

        taken_white_object = self._game.get_chessboard().get_chessboard_dict()['taken_white']
        if taken_white_object:
            taken_white_names = []
            for piece in taken_white_object:
                taken_white_names.append(piece.get_name())
        else:
            taken_white_names = 'None'
        print('Taken White Pieces: ' + str(taken_white_names))

        taken_black_object = self._game.get_chessboard().get_chessboard_dict()['taken_black']
        if taken_black_object:
            taken_black_names = []
            for piece in taken_black_object:
                taken_black_names.append(piece.get_name())
        else:
            taken_black_names = 'None'
        print('Taken Black Pieces: ' + str(taken_black_names))


if __name__ == '__main__':
    unittest.main()
