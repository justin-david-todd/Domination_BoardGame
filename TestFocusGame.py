# Author: Justin David Todd
# Date: 11/17/2020
# Description: unittests for FocusGame.py

import unittest
from FocusGame import Player, Stack, Board, FocusGame


class PlayerTests(unittest.TestCase):
    """Includes unittests for Player class"""

    def test_playerCreate(self):
        """
        tests that player object is properly created with working
        get functions to access attributes.
        """
        p1 = Player(("Player_1", "R"))

        color = p1.get_color()
        name = p1.get_name()
        captured = p1.get_captured()
        reserve = p1.get_reserve()

        self.assertEqual("R", color)
        self.assertEqual("Player_1", name)
        self.assertEqual(0, captured)
        self.assertEqual(0, reserve)

    def test_playerIncDec(self):
        """
        tests that inc_captured, inc_reserve, and dec_reserve successfully increment
        and decrement the proper attributes.
        """
        p1 = Player(("Player_1", "R"))

        p1.inc_captured()
        p1.inc_captured()
        p1.inc_reserve()
        p1.inc_reserve()

        captured = p1.get_captured()
        reserve = p1.get_reserve()

        p1.dec_reserve()

        reserve2 = p1.get_reserve()

        p1.dec_reserve()

        reserve3 = p1.get_reserve()

        self.assertEqual(2, captured)
        self.assertEqual(2, reserve)
        self.assertEqual(1, reserve2)
        self.assertEqual(0, reserve3)


class StackTests(unittest.TestCase):
    """Includes unittests for Stack class"""

    def test_stackCreate(self):
        """tests that a stack object can be properly created with the necessary get methods."""
        s1 = Stack("R")
        s2 = Stack("G")

        color1 = s1.get_color()
        color2 = s2.get_color()
        stack1 = s1.get_stack()
        stack2 = s2.get_stack()
        height = s1.get_height()

        self.assertEqual("R", color1)
        self.assertEqual("G", color2)
        self.assertEqual(["R"], stack1)
        self.assertEqual(["G"], stack2)
        self.assertEqual(1, height)

    def test_stackChangeColor(self):
        """checks that set_color changes the color controlling the stack."""
        s1 = Stack("R")

        s1.set_color("G")

        color = s1.get_color()

        self.assertEqual("G", color)

    def test_stackIncDec(self):
        """checks that inc_height and dec_height methods increase and decrease the height"""
        s1 = Stack("R")

        s1.inc_height()

        height1 = s1.get_height()

        s1.dec_height()

        height2 = s1.get_height()

        self.assertEqual(2, height1)
        self.assertEqual(1, height2)

    def test_stackAdd(self):
        """
        tests that add method adds pieces to the top of the stack and
        properly changes the color in control of the stack
        """
        s1 = Stack("R")

        s1.add("G")
        s1.add("G")

        color1 = s1.get_color()
        stack1 = s1.get_stack()
        height1 = s1.get_height()

        self.assertEqual(["R", "G", "G"], stack1)
        self.assertEqual("G", color1)
        self.assertEqual(3, height1)

        s1.add("R")
        s1.add("R")

        stack2 = s1.get_stack()
        color2 = s1.get_color()
        height2 = s1.get_height()

        self.assertEqual(["R", "G", "G", "R", "R"], stack2)
        self.assertEqual("R", color2)
        self.assertEqual(5, height2)

    def test_stackOffTop(self):
        """
        tests that off_top method removes single and multiple pieces from the top of the stack.
        also tests that control of the stack is transferred to the new color on top of the stack
        also tests that removing the last piece from a stack changes the color to None
        """
        s1 = Stack("R")

        s1.add("G")
        s1.add("G")
        s1.add("R")
        s1.add("R")

        s1.off_top()

        stack1 = s1.get_stack()
        color1 = s1.get_color()
        height1 = s1.get_height()

        self.assertEqual(["R", "G", "G", "R"], stack1)
        self.assertEqual("R", color1)
        self.assertEqual(4, height1)

        s1.off_top()
        s1.off_top()

        stack2 = s1.get_stack()
        color2 = s1.get_color()
        height2 = s1.get_height()

        self.assertEqual(["R", "G"], stack2)
        self.assertEqual("G", color2)
        self.assertEqual(2, height2)

        s1.off_top()
        s1.off_top()

        stack3 = s1.get_stack()
        color3 = s1.get_color()
        height3 = s1.get_height()

        self.assertFalse(stack3)
        self.assertIsNone(color3)
        self.assertEqual(0, height3)

    def test_stackOffBottom(self):
        """
        tests that off_bottom method removes single and multiple pieces from the bottom of the stack.
        """
        s1 = Stack("R")

        s1.add("G")
        s1.add("G")
        s1.add("R")
        s1.add("R")

        s1.off_bottom()

        stack1 = s1.get_stack()
        color1 = s1.get_color()
        height1 = s1.get_height()

        self.assertEqual(["G", "G", "R", "R"], stack1)
        self.assertEqual("R", color1)
        self.assertEqual(4, height1)

        s1.off_bottom()
        s1.off_bottom()

        stack2 = s1.get_stack()
        color2 = s1.get_color()
        height2 = s1.get_height()

        self.assertEqual(["R", "R"], stack2)
        self.assertEqual("R", color2)
        self.assertEqual(2, height2)


class BoardTests(unittest.TestCase):
    """Includes unittests for Board class"""

    def test_boardRow0(self):
        """
        tests that Row 0 of the board initiates correctly with a Stack of the correct color
        in each space and that the get_stack method can retrieve each Stack.
        """
        b1 = Board("R", "G")

        stack1 = b1.get_stack((0, 0)).get_color()
        stack2 = b1.get_stack((0, 1)).get_color()
        stack3 = b1.get_stack((0, 2)).get_color()
        stack4 = b1.get_stack((0, 3)).get_color()
        stack5 = b1.get_stack((0, 4)).get_color()
        stack6 = b1.get_stack((0, 5)).get_color()

        self.assertEqual("R", stack1)
        self.assertEqual("R", stack2)
        self.assertEqual("G", stack3)
        self.assertEqual("G", stack4)
        self.assertEqual("R", stack5)
        self.assertEqual("R", stack6)

    def test_boardRow1(self):
        """
        tests that Row 1 of the board initiates correctly with a Stack of the correct color
        in each space and that the get_stack method can retrieve each Stack.
        """
        b1 = Board("R", "G")

        stack1 = b1.get_stack((1, 0)).get_color()
        stack2 = b1.get_stack((1, 1)).get_color()
        stack3 = b1.get_stack((1, 2)).get_color()
        stack4 = b1.get_stack((1, 3)).get_color()
        stack5 = b1.get_stack((1, 4)).get_color()
        stack6 = b1.get_stack((1, 5)).get_color()

        self.assertEqual("G", stack1)
        self.assertEqual("G", stack2)
        self.assertEqual("R", stack3)
        self.assertEqual("R", stack4)
        self.assertEqual("G", stack5)
        self.assertEqual("G", stack6)

    def test_boardRow2(self):
        """
        tests that Row 2 of the board initiates correctly with a Stack of the correct color
        in each space and that the get_stack method can retrieve each Stack.
        """
        b1 = Board("R", "G")

        stack1 = b1.get_stack((2, 0)).get_color()
        stack2 = b1.get_stack((2, 1)).get_color()
        stack3 = b1.get_stack((2, 2)).get_color()
        stack4 = b1.get_stack((2, 3)).get_color()
        stack5 = b1.get_stack((2, 4)).get_color()
        stack6 = b1.get_stack((2, 5)).get_color()

        self.assertEqual("R", stack1)
        self.assertEqual("R", stack2)
        self.assertEqual("G", stack3)
        self.assertEqual("G", stack4)
        self.assertEqual("R", stack5)
        self.assertEqual("R", stack6)

    def test_boardRow3(self):
        """
        tests that Row 3 of the board initiates correctly with a Stack of the correct color
        in each space and that the get_stack method can retrieve each Stack.
        """
        b1 = Board("R", "G")

        stack1 = b1.get_stack((3, 0)).get_color()
        stack2 = b1.get_stack((3, 1)).get_color()
        stack3 = b1.get_stack((3, 2)).get_color()
        stack4 = b1.get_stack((3, 3)).get_color()
        stack5 = b1.get_stack((3, 4)).get_color()
        stack6 = b1.get_stack((3, 5)).get_color()

        self.assertEqual("G", stack1)
        self.assertEqual("G", stack2)
        self.assertEqual("R", stack3)
        self.assertEqual("R", stack4)
        self.assertEqual("G", stack5)
        self.assertEqual("G", stack6)

    def test_boardRow4(self):
        """
        tests that Row 0 of the board initiates correctly with a Stack of the correct color
        in each space and that the get_stack method can retrieve each Stack.
        """
        b1 = Board("R", "G")

        stack1 = b1.get_stack((4, 0)).get_color()
        stack2 = b1.get_stack((4, 1)).get_color()
        stack3 = b1.get_stack((4, 2)).get_color()
        stack4 = b1.get_stack((4, 3)).get_color()
        stack5 = b1.get_stack((4, 4)).get_color()
        stack6 = b1.get_stack((4, 5)).get_color()

        self.assertEqual("R", stack1)
        self.assertEqual("R", stack2)
        self.assertEqual("G", stack3)
        self.assertEqual("G", stack4)
        self.assertEqual("R", stack5)
        self.assertEqual("R", stack6)

    def test_boardRow5(self):
        """
        tests that Row 5 of the board initiates correctly with a Stack of the correct color
        in each space and that the get_stack method can retrieve each Stack.
        """
        b1 = Board("R", "G")

        stack1 = b1.get_stack((5, 0)).get_color()
        stack2 = b1.get_stack((5, 1)).get_color()
        stack3 = b1.get_stack((5, 2)).get_color()
        stack4 = b1.get_stack((5, 3)).get_color()
        stack5 = b1.get_stack((5, 4)).get_color()
        stack6 = b1.get_stack((5, 5)).get_color()

        self.assertEqual("G", stack1)
        self.assertEqual("G", stack2)
        self.assertEqual("R", stack3)
        self.assertEqual("R", stack4)
        self.assertEqual("G", stack5)
        self.assertEqual("G", stack6)


class FocusGameTests(unittest.TestCase):
    """Includes unittests for FocusGame class"""

    def test_focusGameCreate(self):
        """
        tests that init method creates a game with two players, a board
        and correctly initialized current player, last_player, and state
        with appropriate get methods for each.
        """

        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a().get_name()
        playerb = game.get_player_b().get_name()
        colora = game.get_player_a().get_color()
        colorb = game.get_player_b().get_color()
        last_player = game.get_last_player()
        board = game.get_board().get_colored_board()

        self.assertEqual("Jim", playera)
        self.assertEqual("Gary", playerb)
        self.assertEqual("R", colora)
        self.assertEqual("G", colorb)
        self.assertIsNone(last_player)
        self.assertEqual(
            [["R", "R", "G", "G", "R", "R"],
             ["G", "G", "R", "R", "G", "G"],
             ["R", "R", "G", "G", "R", "R"],
             ["G", "G", "R", "R", "G", "G"],
             ["R", "R", "G", "G", "R", "R"],
             ["G", "G", "R", "R", "G", "G"]], board
        )

    def test_get_other_player(self):
        """
        tests that the method get_other_player returns
        the player opposite from the player entered
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result1 = game.get_other_player(playera)
        result2 = game.get_other_player(playerb)

        self.assertEqual(playerb, result1)
        self.assertEqual(playera, result2)

    def test_GetSet_Last(self):
        """Checks the get and set method for _last_player"""
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playerb = game.get_player_b()

        game.set_last_player(playerb)

        last = game.get_last_player()

        self.assertEqual(playerb, last)

    def test_GetSet_GameState(self):
        """checks te get and set method for _game_state"""
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        result1 = game.get_game_state()

        game.set_game_state(game.get_player_a().get_name() + " Won")

        result2 = game.get_game_state()

        self.assertEqual("PLAYING", result1)
        self.assertEqual("Jim Won", result2)

    def test_player_from_name(self):
        """tests that get_player_from_name method retrieves the correct player object"""
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result1 = game.get_player_from_name("Jim")
        result2 = game.get_player_from_name("Gary")

        self.assertEqual(playera, result1)
        self.assertEqual(playerb, result2)

    def test_win_method(self):
        """
        tests that player_win method appropriately changes the game_state.
        tests that same method returns appropriate string.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.player_win(playera)

        self.assertEqual("Jim Wins", game.get_game_state())
        self.assertEqual("Jim Wins", result)

        result = game.player_win(playerb)

        self.assertEqual("Gary Wins", game.get_game_state())
        self.assertEqual("Gary Wins", result)

    def test_verify_move_success(self):
        """
        tests verify move returns True for various legal moves.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.verify_move(playera, (0, 0))      # tests first turn moves
        self.assertTrue(result)
        result = game.verify_move(playerb, (5, 5))
        self.assertTrue(result)

        game.set_last_player(playerb)                   # tests moves on playera turn

        result = game.verify_move(playera, (0, 0))
        self.assertTrue(result)
        result = game.verify_move(playera, (5, 5))
        self.assertTrue(result)
        result = game.verify_move(playera, (0, 5))
        self.assertTrue(result)
        result = game.verify_move(playera, (5, 0))
        self.assertTrue(result)
        result = game.verify_move(playera, (3, 3))
        self.assertTrue(result)
        result = game.verify_move(playera, (5, 3))
        self.assertTrue(result)

        game.set_last_player(playera)                   # tests moves on playerb turn

        result = game.verify_move(playerb, (0, 0))
        self.assertTrue(result)
        result = game.verify_move(playerb, (5, 5))
        self.assertTrue(result)
        result = game.verify_move(playerb, (0, 5))
        self.assertTrue(result)
        result = game.verify_move(playerb, (5, 0))
        self.assertTrue(result)
        result = game.verify_move(playerb, (3, 3))
        self.assertTrue(result)
        result = game.verify_move(playerb, (5, 3))
        self.assertTrue(result)

    def test_verify_move_game_over(self):
        """
        tests verify_move method returns False if
        -game is won
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        game.set_game_state("Jim Wins")

        result = game.verify_move(playera, (0, 0))
        self.assertFalse(result)

        result = game.verify_move(playerb, (5, 5))
        self.assertFalse(result)

    def test_verify_move_wrong_turn(self):
        """
        tests verify_move method returns False if
        -not player's turn
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        game.set_last_player(playera)

        result = game.verify_move(playera, (0, 0))
        self.assertFalse(result)

        game.set_last_player(playerb)

        result = game.verify_move(playerb, (5, 5))
        self.assertFalse(result)

    def test_verify_move_dst_off_board(self):
        """
        tests verify_move method returns False if
        -destination is not on the board
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.verify_move(playera, (-1, 0))
        self.assertFalse(result)
        result = game.verify_move(playerb, (0, -1))
        self.assertFalse(result)
        result = game.verify_move(playera, (6, 0))
        self.assertFalse(result)
        result = game.verify_move(playerb, (0, 6))
        self.assertFalse(result)
        result = game.verify_move(playera, (-1, 5))
        self.assertFalse(result)
        result = game.verify_move(playerb, (5, -1))
        self.assertFalse(result)
        result = game.verify_move(playera, (6, 5))
        self.assertFalse(result)
        result = game.verify_move(playerb, (5, 6))
        self.assertFalse(result)
        result = game.verify_move(playera, (-1, 3))
        self.assertFalse(result)
        result = game.verify_move(playerb, (3, -1))
        self.assertFalse(result)
        result = game.verify_move(playera, (6, 3))
        self.assertFalse(result)
        result = game.verify_move(playerb, (3, 6))
        self.assertFalse(result)

    def test_verify_stack_move_single_success(self):
        """
        tests verify_stack_move method returns True for various legal single moves
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.verify_stack_move(playera, (0, 0), (1, 0), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 1), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playerb, (5, 0), (4, 0), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playerb, (5, 0), (5, 1), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 5), (1, 5), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 5), (0, 4), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playerb, (5, 5), (4, 5), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playerb, (5, 5), (5, 4), 1)
        self.assertTrue(result)

    def test_verify_stack_move_multi_success(self):
        """
        tests verify_stack_move method returns True for various legal multiple moves
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 4):
            game.get_board().get_stack((0, 0)).add("R")

        result = game.verify_stack_move(playera, (0, 0), (1, 0), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (2, 0), 2)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (3, 0), 3)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (4, 0), 4)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (5, 0), 5)
        self.assertTrue(result)

        result = game.verify_stack_move(playera, (0, 0), (0, 1), 1)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 2), 2)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 3), 3)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 4), 4)
        self.assertTrue(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 5), 5)
        self.assertTrue(result)

    def test_verify_stack_move_src_off_board(self):
        """
        tests verify_stack_move method returns False if:
        -source coordinates are off board
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.verify_stack_move(playera, (-1, 0), (0, 0), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playerb, (0, -1), (0, 0), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (6, 0), (6, 0), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playerb, (5, -1), (5, -1), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (-1, 5), (-1, 5), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playerb, (0, 6), (0, 5), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (6, 5), (5, 5), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playerb, (5, 6), (5, 5), 1)
        self.assertFalse(result)

    def test_verify_stack_move_null_move(self):
        """
        tests verify_stack_move method returns False if:
        -source and destination coordinates are the same.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.verify_stack_move(playera, (0, 0), (0, 0), 1)
        self.assertFalse(result)

    def test_verify_stack_move_wrong_player(self):
        """
        tests verify_stack_move method returns False if:
        -the player controls the stack
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.verify_stack_move(playerb, (0, 0), (0, 0), 1)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("G")

        result = game.verify_stack_move(playera, (0, 0), (0, 0), 1)
        self.assertFalse(result)

    def test_verify_stack_move_diagonal(self):
        """
        tests verify_stack_move method returns False if:
        -the player controls the stack
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.verify_stack_move(playera, (0, 0), (1, 1), 1)
        self.assertFalse(result)

    def test_verify_stack_move_distance(self):
        """
        tests verify_stack_move method returns False if:
        -the player controls the stack
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 4):
            game.get_board().get_stack((0, 0)).add("R")

        result = game.verify_stack_move(playera, (0, 0), (0, 2), 1)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 3), 2)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 4), 3)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 0), (0, 5), 4)
        self.assertFalse(result)

    def test_verify_stack_num_pieces(self):
        """
        tests verify_stack_move method returns False if:
        -the number of pieces moved is too great
        -the number of pieces moved is too small
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 1):
            game.get_board().get_stack((0, 1)).off_top()
        for i in range(0, 1):
            game.get_board().get_stack((0, 2)).add("R")
        for i in range(0, 2):
            game.get_board().get_stack((0, 3)).add("R")
        for i in range(0, 3):
            game.get_board().get_stack((0, 4)).add("R")
        for i in range(0, 4):
            game.get_board().get_stack((0, 5)).add("R")

        result = game.verify_stack_move(playera, (0, 0), (1, 0), 0)     # checks num_pieces too small
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 1), (1, 1), 0)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 0), (1, 0), -1)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 1), (1, 1), -1)
        self.assertFalse(result)

        result = game.verify_stack_move(playera, (0, 0), (1, 0), 0)     # checks num_pieces too great
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 1), (1, 1), 2)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 2), (1, 2), 3)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 3), (1, 3), 4)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 4), (1, 4), 5)
        self.assertFalse(result)
        result = game.verify_stack_move(playera, (0, 5), (1, 5), 6)
        self.assertFalse(result)

    def test_endgame_success(self):
        """
        tests that check_endgame method returns 0 if player still has pieces on the board or 1
        or more in reserve.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board().get_board()

        for row in board:
            for space in row:
                space.add("R")

        game.get_board().get_stack((5, 5)).add("G")

        result = game.check_endgame(playerb)    # checks playerb with one space on the board
        self.assertEqual(0, result)

        for row in board:
            for space in row:
                space.add("G")

        game.get_board().get_stack((5, 5)).add("R")

        result = game.check_endgame(playera)    # checks playera with one space on the board
        self.assertEqual(0, result)

        for row in board:
            for space in row:
                space.add("R")

        playerb.inc_reserve()

        result = game.check_endgame(playerb)    # checks playerb with pieces in reserve
        self.assertEqual(0, result)

        playerb.inc_reserve()

        result = game.check_endgame(playerb)
        self.assertEqual(0, result)

        for row in board:
            for space in row:
                space.add("G")

        playera.inc_reserve()

        result = game.check_endgame(playera)    # checks playera with pieces in reserve
        self.assertEqual(0, result)

        playera.inc_reserve()

        result = game.check_endgame(playera)
        self.assertEqual(0, result)

    def test_endgame(self):
        """
        tests that check_endgame returns 1 if a player has no valid moves
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board().get_board()

        for row in board:
            for space in row:
                space.add("R")

        result = game.check_endgame(playerb)

        self.assertEqual(1, result)

    def test_nxt_turn(self):
        """test next_turn method changes last_player to input player"""
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        game.next_turn(playera)

        result = game.get_last_player()

        self.assertEqual(playera, result)

    def test_move_piece_start(self):
        """
        tests move_piece method allows either player may start the game,
        last_player is set to the player making the move
        and returns "successfully moved" when executed.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.move_piece("Jim", (0, 0), (1, 0), 1)
        self.assertEqual("successfully moved", result)
        self.assertEqual(game.get_last_player(), playera)

        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.move_piece("Gary", (1, 0), (2, 0), 1)
        self.assertEqual("successfully moved", result)
        self.assertEqual(game.get_last_player(), playerb)

    def test_move_piece_alt_turns(self):
        """Tests that players can alternate turns using move_piece method"""
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.move_piece("Jim", (0, 0), (1, 0), 1)
        self.assertEqual("successfully moved", result)
        result = game.move_piece("Gary", (1, 1), (1, 0), 1)
        self.assertEqual("successfully moved", result)
        result = game.move_piece("Jim", (2, 0), (3, 0), 1)
        self.assertEqual("successfully moved", result)
        result = game.move_piece("Gary", (3, 1), (2, 1), 1)
        self.assertEqual("successfully moved", result)

    def test_single_move(self):
        """
        tests that move_pieces method can make legal single moves
        and adjust the source and destination stack sizes correctly,
        including from and too multi-sized stacks.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board()

        result = game.move_piece("Jim", (0, 0), (1, 0), 1)  # tests single move by playera to stack of size 1
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack((0, 0)).get_stack()
        result2 = board.get_stack((1, 0)).get_stack()

        self.assertEqual([], result1)
        self.assertEqual(["G", "R"], result2)

        result = game.move_piece("Gary", (1, 1), (1, 0), 1)  # tests single move by playerb to stack of size 2
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack((1, 1)).get_stack()
        result2 = board.get_stack((1, 0)).get_stack()

        self.assertEqual([], result1)
        self.assertEqual(["G", "R", "G"], result2)

        result = game.move_piece("Jim", (0, 1), (0, 0), 1)  # tests single move by playera to stack of size 0
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack((0, 1)).get_stack()
        result2 = board.get_stack((0, 0)).get_stack()

        self.assertEqual([], result1)
        self.assertEqual(["R"], result2)

        result = game.move_piece("Gary", (1, 0), (0, 0), 1)  # tests single move by playerb from stack of size 3
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack((1, 0)).get_stack()
        result2 = board.get_stack((0, 0)).get_stack()

        self.assertEqual(["G", "R"], result1)
        self.assertEqual(["R", "G"], result2)

    def test_multi_move(self):
        """
        tests move_piece method:
        returns "successfully moved" for moving stacks of 1-5 pieces.
        updates source and destination stacks correctly.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board()

        for piece in range(0, 4):
            board.get_stack((0, 0)).add("R")

        for piece in range(0, 3):
            board.get_stack((0, 1)).add("G")

        src = (0, 0)    # tests two piece move
        dst = (2, 0)
        num = 2
        result = game.move_piece("Jim", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack(src).get_stack()
        result2 = board.get_stack(dst).get_stack()

        self.assertEqual(["R", "R", "R"], result1)
        self.assertEqual(["R", "R", "R"], result2)

        src = (0, 1)  # tests four piece move
        dst = (0, 5)
        num = 4
        result = game.move_piece("Gary", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack(src).get_stack()
        result2 = board.get_stack(dst).get_stack()

        self.assertEqual([], result1)
        self.assertEqual(["R", "R", "G", "G", "G"], result2)

        src = (2, 0)  # tests three piece move
        dst = (5, 0)
        num = 3
        result = game.move_piece("Jim", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack(src).get_stack()
        result2 = board.get_stack(dst).get_stack()

        #self.assertEqual([], result1)
        #self.assertEqual(["R", "R", "G", "R", "R"], result2)

    def test_stack_height_adjust(self):
        """
        tests that move_piece method adjusts stack contents correctly
        if a stack's height exceeds 5; for both single and multi moves.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board()

        board.get_stack((0, 0)).add("G")  # sets (0, 0) to RGRGG
        board.get_stack((0, 0)).add("R")
        board.get_stack((0, 0)).add("G")
        board.get_stack((0, 0)).add("G")

        board.get_stack((0, 2)).add("R")  # sets (0, 2) to GRRR
        board.get_stack((0, 2)).add("R")
        board.get_stack((0, 2)).add("R")

        board.get_stack((1, 0)).add("R")  # puts R piece on (1, 0)

        board.get_stack((3, 2)).add("G")  # puts 3 G pieces on (3, 2)
        board.get_stack((3, 2)).add("G")
        board.get_stack((3, 2)).add("G")

        src = (1, 0)  # tests 1 piece move, single stack overflow
        dst = (0, 0)
        num = 1
        result = game.move_piece("Jim", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack(src).get_stack()
        result2 = board.get_stack(dst).get_stack()

        self.assertEqual(["G"], result1)
        self.assertEqual(["G", "R", "G", "G", "R"], result2)

        src = (3, 2)  # tests 3 piece move, with 2 piece stack overflow
        dst = (0, 2)
        num = 3
        result = game.move_piece("Gary", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = board.get_stack(src).get_stack()
        result2 = board.get_stack(dst).get_stack()

        self.assertEqual(["R"], result1)
        self.assertEqual(["R", "R", "G", "G", "G"], result2)

    def test_capture(self):
        """
        tests that move_piece method captures single and multiple pieces
        and adjusts the player's reserve and captured totals accordingly.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board()

        board.get_stack((1, 5)).add("G")  # sets (0, 0) to RGRGG
        board.get_stack((1, 5)).add("R")
        board.get_stack((1, 5)).add("G")
        board.get_stack((1, 5)).add("G")

        src = (0, 5)                      # tests single capture
        dst = (1, 5)
        num = 1
        game.move_piece("Jim", src, dst, num)

        result1 = playera.get_captured()
        result2 = playera.get_reserve()

        self.assertEqual(1, result1)
        self.assertEqual(0, result2)

        board.get_stack((0, 0)).add("R")  # sets (0, 0) to RRRRR
        board.get_stack((0, 0)).add("R")
        board.get_stack((0, 0)).add("R")
        board.get_stack((0, 0)).add("R")

        board.get_stack((5, 0)).add("G")  # sets (5, 0) to GGGGG
        board.get_stack((5, 0)).add("G")
        board.get_stack((5, 0)).add("G")
        board.get_stack((5, 0)).add("G")

        src = (5, 0)                      # tests five piece capture
        dst = (0, 0)
        num = 5
        result = game.move_piece("Gary", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = playerb.get_captured()
        result2 = playerb.get_reserve()

        self.assertEqual(5, result1)
        self.assertEqual(0, result2)

    def test_reserve(self):
        """
        tests that move_piece method reserves single and multiple pieces
        and adjusts the player's reserve and captured totals accordingly.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board()

        board.get_stack((0, 0)).add("G")  # sets (0, 0) to RGRGG
        board.get_stack((0, 0)).add("R")
        board.get_stack((0, 0)).add("G")
        board.get_stack((0, 0)).add("G")

        board.get_stack((0, 1)).add("R")  # puts an R piece on (0, 1)

        src = (0, 1)                      # tests single reserve
        dst = (0, 0)
        num = 1
        result = game.move_piece("Jim", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = playera.get_captured()
        result2 = playera.get_reserve()

        self.assertEqual(0, result1)
        self.assertEqual(1, result2)

        board.get_stack((0, 2)).add("G")  # sets (0, 2) to GGGG
        board.get_stack((0, 2)).add("G")
        board.get_stack((0, 2)).add("G")

        board.get_stack((4, 2)).add("G")  # puts 4 G pieces on (4, 2)
        board.get_stack((4, 2)).add("G")
        board.get_stack((4, 2)).add("G")
        board.get_stack((4, 2)).add("G")

        src = (4, 2)                      # tests triple reserve
        dst = (0, 2)
        num = 4
        result = game.move_piece("Gary", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = playerb.get_captured()
        result2 = playerb.get_reserve()

        self.assertEqual(0, result1)
        self.assertEqual(3, result2)

    def test_capture_reserve(self):
        """
        tests that move_piece method captures and reserves pieces simultaneously
        and adjusts the player's reserve and captured totals accordingly.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board()

        board.get_stack((0, 2)).add("R")  # sets (0, 2) to GRGRG
        board.get_stack((0, 2)).add("G")
        board.get_stack((0, 2)).add("R")
        board.get_stack((0, 2)).add("G")

        board.get_stack((5, 2)).add("G")  # sets (5, 2) to GGGGG
        board.get_stack((5, 2)).add("G")
        board.get_stack((5, 2)).add("G")
        board.get_stack((5, 2)).add("G")

        src = (5, 2)  # tests 2 capture, 3 reserve
        dst = (0, 2)
        num = 5
        result = game.move_piece("Gary", src, dst, num)
        self.assertEqual("successfully moved", result)

        result1 = playerb.get_captured()
        result2 = playerb.get_reserve()

        self.assertEqual(2, result1)
        self.assertEqual(3, result2)

    def test_moveFail_wrong_turn(self):
        """
        tests that move_piece method returns False if:
        -a player takes two turns in a row
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        result = game.move_piece("Jim", (0, 0), (1, 0), 1)
        self.assertEqual("successfully moved", result)
        result = game.move_piece("Jim", (0, 1), (1, 1), 1)
        self.assertFalse(result)

    def test_moveFail_src_off_board(self):
        """
        tests that move_piece method returns False if:
        - source is off board
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        result = game.move_piece("Jim", (0, -1), (0, 0), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (-1, 0), (0, 0), 1)
        self.assertFalse(result)

        result = game.move_piece("Jim", (5, -1), (5, 0), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (6, 0), (5, 0), 1)
        self.assertFalse(result)

        result = game.move_piece("Jim", (0, 6), (0, 5), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (-1, 5), (0, 5), 1)
        self.assertFalse(result)

        result = game.move_piece("Jim", (6, 5), (5, 5), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (5, 6), (5, 5), 1)
        self.assertFalse(result)

    def test_moveFail_dst_off_board(self):
        """
        tests that move_piece method returns False if:
        - destination is off board
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        result = game.move_piece("Jim", (0, 0), (0, -1), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (0, 0), (-1, 0), 1)
        self.assertFalse(result)

        result = game.move_piece("Jim", (5, 0), (5, -1), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (5, 0), (6, 0), 1)
        self.assertFalse(result)

        result = game.move_piece("Jim", (0, 5), (0, 6), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (0, 5), (-1, 5), 1)
        self.assertFalse(result)

        result = game.move_piece("Jim", (5, 5), (6, 5), 1)
        self.assertFalse(result)
        result = game.move_piece("Jim", (5, 5), (5, 6), 1)
        self.assertFalse(result)

    def test_moveFail_null_move(self):
        """
        tests that move_piece method returns False if:
        - player tries to move zero spaces
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        result = game.move_piece("Jim", (0, 0), (0, 0), 1)
        self.assertFalse(result)
        result = game.move_piece("Gary", (5, 5), (5, 5), 1)
        self.assertFalse(result)

    def test_moveFail_num_pieces(self):
        """
        tests that move_piece method returns False if:
        - player tries to move to many or too few pieces
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        game.get_board().get_stack((0, 0)).off_top()        # checks move with 0 pieces (source)

        result = game.move_piece("Jim", (0, 0), (0, 1), 1)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")         # checks move with 1 piece

        result = game.move_piece("Jim", (0, 0), (0, 1), 2)
        self.assertFalse(result)

        result = game.move_piece("Jim", (0, 0), (0, 1), 0)  # checks 0 piece move
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")         # checks move with 2 pieces

        result = game.move_piece("Jim", (0, 0), (0, 1), 3)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")         # checks move with 3 pieces

        result = game.move_piece("Jim", (0, 0), (0, 1), 4)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")         # checks move with 4 pieces

        result = game.move_piece("Jim", (0, 0), (0, 1), 5)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")         # checks move with 5 pieces

        result = game.move_piece("Jim", (0, 0), (0, 1), 6)
        self.assertFalse(result)

    def test_moveFail_diagonal(self):
        """
        tests that move_piece method returns False if:
        - move is diagonal
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        game.get_board().get_stack((0, 0)).add("R")

        result = game.move_piece("Jim", (0, 0), (1, 1), 2)
        self.assertFalse(result)

        result = game.move_piece("Jim", (0, 0), (1, 1), 1)
        self.assertFalse(result)

    def test_moveFail_stack_control(self):
        """
        tests that move_piece method returns False if:
        - source stack is not player's
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        result = game.move_piece("Jim", (1, 0), (0, 0), 1)
        self.assertFalse(result)

        result = game.move_piece("Gary", (0, 0), (1, 0), 1)
        self.assertFalse(result)

    def test_moveFail_distance(self):
        """
        tests that move_piece method returns False if:
        - spaces moved is greater than number of pieces to move
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        game.get_board().get_stack((0, 0)).off_top()  # checks move with 1 horizontal distance

        result = game.move_piece("Jim", (0, 0), (0, 1), 0)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")  # checks move with 2 horizontal distance

        result = game.move_piece("Jim", (0, 0), (0, 2), 1)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")  # checks move with 3 horizontal distance

        result = game.move_piece("Jim", (0, 0), (0, 3), 2)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")  # checks move with 4 vertical distance

        result = game.move_piece("Jim", (0, 0), (4, 0), 3)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")  # checks move with 5 vertical distance

        result = game.move_piece("Jim", (0, 0), (5, 0), 4)
        self.assertFalse(result)

        game.get_board().get_stack((0, 0)).add("R")  # checks move with 6 distance

        result = game.move_piece("Jim", (0, 0), (6, 0), 5)
        self.assertFalse(result)

    def test_winning_move(self):
        """
        tests that move_piece method returns "<player> Wins" if six pieces are captured
        and changes game_state to "<Player> Wins".
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        board = game.get_board()

        for i in range(0, 5):
            game.get_player_a().inc_captured()

        for i in range(0, 4):
            board.get_stack((0, 2)).add("G")        # sets (0, 2) to GGGGG

        result = game.move_piece("Jim", (0, 1), (0, 2), 1)   # tests win for first player

        self.assertEqual(6, game.get_player_a().get_captured())
        self.assertEqual("Jim Wins", result)
        self.assertEqual("Jim Wins", game.get_game_state())

        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        board = game.get_board()

        for i in range(0, 5):
            game.get_player_b().inc_captured()  # sets playerb to 5 captured

        for i in range(0, 4):
            board.get_stack((0, 1)).add("R")   # sets (0, 1) to RRRRR

        result = game.move_piece("Gary", (0, 2), (0, 1), 1)  # tests win for second player

        self.assertEqual(6, game.get_player_b().get_captured())
        self.assertEqual("Gary Wins", result)
        self.assertEqual("Gary Wins", game.get_game_state())

    def test_winning_overkill(self):
        """
        tests that move_piece method returns "<player> Wins" if move will capture more
        than six pieces and changes game_state to "<Player> Wins".
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        board = game.get_board()

        for i in range(0, 5):
            game.get_player_a().inc_captured()      # sets playera to 5 captured

        for i in range(0, 4):
            board.get_stack((0, 3)).add("G")        # sets (0, 4) to GGGGG
            board.get_stack((0, 0)).add("R")        # sets (0, 4) to RRRRR

        result = game.move_piece("Jim", (0, 0), (0, 3), 3)  # tests win for first player

        self.assertEqual(6, game.get_player_a().get_captured())
        self.assertEqual("Jim Wins", result)
        self.assertEqual("Jim Wins", game.get_game_state())

        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        board = game.get_board()

        for i in range(0, 5):
            game.get_player_b().inc_captured()  # sets playerb to 5 captured

        for i in range(0, 4):
            board.get_stack((0, 0)).add("R")  # sets (0, 1) to RRRRR
            board.get_stack((0, 3)).add("G")  # sets (0, 4) to GGGGG

        result = game.move_piece("Gary", (0, 3), (0, 0), 3)  # tests win for second player

        self.assertEqual(6, game.get_player_b().get_captured())
        self.assertEqual("Gary Wins", result)
        self.assertEqual("Gary Wins", game.get_game_state())

    def test_moveFail_gameOver(self):
        """
        test that move_piece method returns False if game is over.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        board = game.get_board()

        for i in range(0, 5):
            game.get_player_b().inc_captured()  # sets playerb to 5 captured

        for i in range(0, 4):
            board.get_stack((0, 1)).add("R")  # sets (0, 1) to RRRRR

        game.move_piece("Gary", (0, 2), (0, 1), 1)  # tests win for second player

        result = game.move_piece("Jim", (2, 0), (2, 1), 1)
        self.assertFalse(result)

    def test_reserve_move_success(self):
        """
        tests that reserve_move method returns "successfully moved" when a valid move is made.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        playera.inc_reserve()
        playerb.inc_reserve()

        result = game.reserved_move("Jim", (0, 0))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Gary", (0, 0))
        self.assertEqual("successfully moved", result)

    def test_reserve_move_alt_turns(self):
        """tests that reserve_move method can cause a piece to go into reserve"""
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 4):
            playera.inc_reserve()
            playerb.inc_reserve()

        result = game.reserved_move("Jim", (0, 0))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Gary", (4, 4))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Jim", (3, 3))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Gary", (5, 0))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Jim", (3, 5))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Gary", (0, 5))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Jim", (5, 3))
        self.assertEqual("successfully moved", result)

        result = game.reserved_move("Gary", (5, 5))
        self.assertEqual("successfully moved", result)

    def test_reserve_move_reserve(self):
        """
        tests that reserve_move method can cause a piece to go into a player's reserve pieces
        and adjusts the stack's height accordingly
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 4):
            game.get_board().get_stack((0, 0)).add("R")
            game.get_board().get_stack((5, 5)).add("G")
            playera.inc_reserve()
            playerb.inc_reserve()

        game.reserved_move("Jim", (0, 0))

        game.reserved_move("Gary", (5, 5))

        result = playera.get_reserve()
        self.assertEqual(4, result)

        result = playerb.get_reserve()
        self.assertEqual(4, result)

        game.reserved_move("Jim", (0, 0))           # tests multiple reserve moves
        game.reserved_move("Gary", (5, 5))
        game.reserved_move("Jim", (0, 0))
        game.reserved_move("Gary", (5, 5))
        game.reserved_move("Jim", (0, 0))

        result = playera.get_reserve()
        self.assertEqual(4, result)

        result = game.get_board().get_stack((0, 0)).get_stack()
        self.assertEqual(["R", "R", "R", "R", "R"], result)

    def test_reserve_move_capture(self):
        """
        tests that reserve_move method can cause a piece to go into a player's captured pieces
        and adjusts the stack's height accordingly
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 4):
            game.get_board().get_stack((0, 0)).add("R")
            game.get_board().get_stack((5, 5)).add("G")
            playera.inc_reserve()
            playerb.inc_reserve()

        game.reserved_move("Jim", (5, 5))

        game.reserved_move("Gary", (0, 0))

        result = playera.get_captured()
        self.assertEqual(1, result)

        result = playerb.get_captured()
        self.assertEqual(1, result)

        result = game.get_board().get_stack((0, 0)).get_stack()
        self.assertEqual(["R", "R", "R", "R", "G"], result)

    def test_reserve_move_win(self):
        """
        tests that reserve_move method returns "<player Wins>" when a player has captures 6 pieces.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 7):
            game.get_board().get_stack((0, 0)).add("R")
            game.get_board().get_stack((5, 5)).add("G")
            playera.inc_reserve()
            playerb.inc_reserve()

        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))

        result = playera.get_captured()
        self.assertEqual(6, result)

        result = game.reserved_move("Jim", (0, 0))
        self.assertFalse(result)

    def test_reserveFail_no_reserve(self):
        """
        tests that reserve_move method returns False if:
        - the player has no pieces in reserve
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        game.reserved_move("Jim", (5, 5))
        result = game.reserved_move("Jim", (0, 0))
        self.assertFalse(result)

        game.reserved_move("Gary", (5, 5))
        result = game.reserved_move("Gary", (0, 0))
        self.assertFalse(result)

    def test_reserveFail_wrong_turn(self):
        """
        tests that reserve_move method returns False if:
        - a player tries to take two turns in a row.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 7):
            game.get_board().get_stack((0, 0)).add("R")
            game.get_board().get_stack((5, 5)).add("G")
            playera.inc_reserve()
            playerb.inc_reserve()

        game.reserved_move("Jim", (5, 5))
        result = game.reserved_move("Jim", (0, 0))
        self.assertFalse(result)

        game.reserved_move("Gary", (5, 5))
        result = game.reserved_move("Gary", (0, 0))
        self.assertFalse(result)

    def test_reserveFail_gameOver(self):
        """
        tests that reserve_move method returns False if:
        - the game is over
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 7):
            game.get_board().get_stack((0, 0)).add("R")
            game.get_board().get_stack((5, 5)).add("G")
            playera.inc_reserve()
            playerb.inc_reserve()

        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (5, 5))
        game.reserved_move("Gary", (0, 0))
        game.reserved_move("Jim", (0, 0))

        result = playera.get_captured()
        self.assertEqual(6, result)

        result = game.reserved_move("Gary", (5, 5))
        self.assertFalse(result)

    def test_reserveFail_dst_off_board(self):
        """
        tests that reserve_move method returns False if:
        - the destination coordinates are off the board.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        for i in range(0, 7):
            game.get_board().get_stack((0, 0)).add("R")
            game.get_board().get_stack((5, 5)).add("G")
            playera.inc_reserve()
            playerb.inc_reserve()

        result = game.reserved_move("Jim", (-1, 0))
        self.assertFalse(result)
        result = game.reserved_move("Gary", (0, -1))
        self.assertFalse(result)

        result = game.reserved_move("Jim", (6, 0))
        self.assertFalse(result)
        result = game.reserved_move("Gary", (5, -1))
        self.assertFalse(result)

        result = game.reserved_move("Jim", (-1, 5))
        self.assertFalse(result)
        result = game.reserved_move("Gary", (0, 6))
        self.assertFalse(result)

        result = game.reserved_move("Jim", (6, 5))
        self.assertFalse(result)
        result = game.reserved_move("Gary", (5, 6))
        self.assertFalse(result)

    def test_show_pieces(self):
        """
        tests show piece returns the list of the pieces in a stack in the correct order
        if there are no pieces, returns an empty list.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        board = game.get_board()

        board.get_stack((0, 2)).add("R")  # sets (0, 2) to GRGRG
        board.get_stack((0, 2)).add("G")
        board.get_stack((0, 2)).add("R")
        board.get_stack((0, 2)).add("G")

        board.get_stack((1, 2)).add("G")  # sets (1, 2) to RGGGG
        board.get_stack((1, 2)).add("G")
        board.get_stack((1, 2)).add("G")
        board.get_stack((1, 2)).add("G")

        board.get_stack((0, 0)).off_top()  # sets (0, 0) to empty

        result = game.show_pieces((0, 2))
        self.assertEqual(["G", "R", "G", "R", "G"], result)
        result = game.show_pieces((1, 2))
        self.assertEqual(["R", "G", "G", "G", "G"], result)
        result = game.show_pieces((0, 0))
        self.assertEqual([], result)

    def test_show_reserved(self):
        """
        tests show_reserved method returns 0 if a player's reserve is empty and
        otherwise, the number of reserved pieces.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        playera.inc_reserve()
        playera.inc_reserve()
        playera.inc_reserve()

        result = game.show_reserve("Jim")
        self.assertEqual(3, result)

        result = game.show_reserve("Gary")
        self.assertEqual(0, result)

    def test_show_captured(self):
        """
        tests show_reserved method returns 0 if a player's captured is empty and
        otherwise, the number of captured pieces.
        """
        game = FocusGame(("Jim", "R"), ("Gary", "G"))

        playera = game.get_player_a()
        playerb = game.get_player_b()

        playerb.inc_captured()
        playerb.inc_captured()
        playerb.inc_captured()

        result = game.show_captured("Jim")
        self.assertEqual(0, result)

        result = game.show_captured("Gary")
        self.assertEqual(3, result)
