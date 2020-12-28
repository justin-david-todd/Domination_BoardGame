# Author: Justin David Todd
# Date: 11/22/2020
# Description: Creates a playable "Focus" ("Domination" Game), but on a 6x6 board,
# for two players, and a player wins if they capture six or more pieces.


class Player:
    """
    Creates a player object associated with a name, color, and with a count of reserve and captured pieces.
    Referenced in the FocusGame class to represent a player.
    """

    def __init__(self, player):
        """
        takes a tuple with two strings (name, color)
        creates a new player with that name and color
        """
        self._name = player[0]
        self._color = player[1]
        self._captured = 0
        self._reserve = 0

    def get_color(self):
        """Returns the player's color"""
        return self._color

    def get_name(self):
        """Returns the player's name"""
        return self._name

    def get_captured(self):
        """Returns number of pieces player has captured"""
        return self._captured

    def get_reserve(self):
        """Returns number of pieces player has in reserve"""
        return self._reserve

    def inc_captured(self):
        """Increments the number of pieces player has captured"""
        self._captured += 1

    def inc_reserve(self):
        """Increments the number of pieces player has in reserve"""
        self._reserve += 1

    def dec_reserve(self):
        """Decrements the number of pieces player has in reserve"""
        self._reserve -= 1


class Stack:
    """
    Represents a stack on the board. May contain 0 to 5 pieces and can be moved by a player
    whose piece is on top.
    Referenced by Board and FocusGame classes to represent a space on the board holding multiple pieces.
    """

    def __init__(self, color):
        """creates a Stack object containing one piece of the specified color."""
        self._color = color    # the player allowed to move the stack
        self._stack = [color]   # the contents of the stack
        self._height = 1             # how many pieces are in a stack

    def get_color(self):
        """returns the color of the player who is allowed to move the stack"""
        return self._color

    def get_stack(self):
        """returns the list of the stack's contents (bottom piece at index 0)"""
        return self._stack

    def get_height(self):
        """returns the number of pieces in the stack"""
        return self._height

    def set_color(self, color):
        """changes the color currently in control of the stack"""
        self._color = color

    def inc_height(self):
        """adds one to the height of the stack"""
        self._height += 1

    def dec_height(self):
        """reduces the height of the stack by one"""
        self._height -= 1

    def off_top(self):
        """
        removes a piece from the top of the stack
        if the last piece was removed, changes the color controlling the stack to None.
        """
        del self._stack[-1]
        self.dec_height()
        if self._height == 0:
            self._color = None
        else:
            self.set_color(self._stack[-1])

    def off_bottom(self):
        """removes a piece from the bottom of the stack"""
        del self._stack[0]
        self.dec_height()

    def add(self, color):
        """
        takes a piece's color and adds that colored piece to the top of the stack, giving control of the stack
        to that color.
        """
        self._stack.append(color)
        self.inc_height()
        self.set_color(color)


class Board:
    """
    Takes two colors.
    Represents a 6x6 board of made up of 36 Stack objects associated with those two colors.
    Referenced by FocusGame class to represent the 6x6 playing field
    References the Stack class, as each space on the board contains a Stack representing multiple pieces
    in the same space
    """

    def __init__(self, color1, color2):
        """
        Takes two colors, creates a 6x6 board made of six lists within a list.
        Each inner list is filled with Stack objects each containing one piece,
        The colors of the pieces are split evenly between to colors in the following pattern:
        X  X  O  O  X  X
        O  O  X  X  O  O
        X  X  O  O  X  X
        O  O  X  X  O  O
        X  X  O  O  X  X
        O  O  X  X  O  O
        The board's coordinates are set up so that the upper-left space is (0,0)
        and the lower-right corner is (5,5).
        The Stack at each space may be accessed by coordinates.
        An image of the board showing the color controlling each stack can be printed out.
        """
        self._board = [[], [], [], [], [], []]
        for row in range(0, 6, 2):
            self._board[row].append(Stack(color1))
            self._board[row].append(Stack(color1))
            self._board[row].append(Stack(color2))
            self._board[row].append(Stack(color2))
            self._board[row].append(Stack(color1))
            self._board[row].append(Stack(color1))
        for row in range(1, 6, 2):
            self._board[row].append(Stack(color2))
            self._board[row].append(Stack(color2))
            self._board[row].append(Stack(color1))
            self._board[row].append(Stack(color1))
            self._board[row].append(Stack(color2))
            self._board[row].append(Stack(color2))

    def get_board(self):
        """returns the board"""
        return self._board

    def get_stack(self, coord):
        """Takes a tuple with the board coordinates, returns the Stack object at that coordinate."""
        row = coord[0]
        column = coord[1]
        return self.get_board()[row][column]

    def get_colored_board(self):
        """
        Created a version of the board that contains the color in control of each space
        instead of the Stack object in that space.
        """
        colored_board = []
        for row in range(0, 6):
            colored_row = []
            for column in range(0,6):
                space_color = self.get_stack((row, column)).get_color()
                if space_color is None:
                    space_color = " "
                colored_row.append(space_color)
            colored_board.append(colored_row)
        return colored_board

    def print_board(self):
        """
        prints out a list for each row containing the colors in each space of the row
        if no color, prints " ".
        """
        for row in range(0, 6):
            print(self.get_colored_board()[row])


class FocusGame:
    """
    Represents a game of Focus (Domination). Played on a 6x6 board with two players.
    A player wins if they capture six or more pieces, or their opponent is out
    of valid moves.
    References the Player class to keep track of whose turn it is and how many pieces
    each player has captured or in reserve.
    References the Board and Stack classes to keep track of the game board and how many pieces are in each space.
    """

    def __init__(self, player_a, player_b):
        """
        takes two tuples each with two string elements (player_name, color)
        creates two players each with the entered name and color
        initializes a board for the players,
        then allows them to play a focus game until one of them wins.
        **Note: Either player may begin the game. After that, only the player whose turn it is
        may make a move.
        """
        self._playerA = Player(player_a)
        self._playerB = Player(player_b)
        self._board = Board(player_a[1], player_b[1])
        self._last_player = None
        self._game_state = "PLAYING"

    def get_player_a(self):
        """returns the Player object in _playerA"""
        return self._playerA

    def get_player_b(self):
        """returns the Player object in _playerB"""
        return self._playerB

    def get_other_player(self, player):
        """returns the opponent of the player entered"""
        if player == self.get_player_a():
            return self.get_player_b()
        if player == self.get_player_b():
            return self.get_player_a()

    def get_board(self):
        """returns the Board object _board"""
        return self._board

    def get_last_player(self):
        """returns the player who last made a move"""
        return self._last_player

    def get_game_state(self):
        """returns the current game state"""
        return self._game_state

    def set_game_state(self, new_state):
        """takes a string and sets the game_state to that string"""
        self._game_state = new_state

    def set_last_player(self, player):
        """
        takes a player object
        changes the last player to the player entered
        """
        self._last_player = player

    def get_player_from_name(self, player_name):
        """takes a player_name, returns the player object associated with that name"""
        if player_name == self.get_player_a().get_name():
            return self.get_player_a()
        if player_name == self.get_player_b().get_name():
            return self.get_player_b()

    def player_win(self, player):
        """
        takes a player object
        returns that player as the winner
        changes the game state to won
        """
        self.set_game_state(player.get_name() + " Wins")
        return player.get_name() + " Wins"

    def verify_move(self, player, dst):
        """
        Takes a player and a destination coordinate.
        Verifies the following for any move:
        -the game is not won
        -it is that player's turn
        -the destination is on the board
        If the move is invalid, returns False, otherwise True
        """
        if self.get_game_state() != "PLAYING":  # prevents move if game is won
            return False

        for num in dst:                         # checks destination is on board
            if num < 0 or num > 5:
                return False

        if self._last_player == player:         # prevents move by player not on their turn
            return False

        return True

    def verify_stack_move(self, player, src, dst, num_pieces):
        """
        Takes a Player, number of pieces to be moved, a tuple of destination
        board coordinates, and a tuple of source board coordinates.
        Verifies the following for single/multiple moves:
        -the source stack is on the board
        -the source and destination stacks are not the same
        -the source stack belongs to the player
        -the move is not diagonal
        -the move is not further than the number of pieces moved.
        -the number of pieces to be moved is not less than zero
         and not greater than the available pieces.
        If the move is invalid, returns False, otherwise True
        """
        for num in src:                                  # checks source is on board
            if num < 0 or num > 5:
                return False

        if src == dst:                                   # checks src and dst are not the same.
            return False

        src_stack = self.get_board().get_stack(src)

        if num_pieces < 1 or num_pieces > src_stack.get_height():
            return False                                # prevents moving too many or too few pieces

        if src_stack.get_color() != player.get_color():  # prevents move of stack that player doesn't control
            return False

        if src[0] != dst[0] and src[1] != dst[1]:        # prevents diagonal moves
            return False

        if src[0] == dst[0]:                             # prevents a move of too many spaces
            move_distance = src[1] - dst[1]
        else:
            move_distance = src[0] - dst[0]
        if move_distance < 0:
            move_distance *= -1
        if move_distance != num_pieces:
            return False

        return True

    def check_endgame(self, player):
        """
        takes a player and checks if they have any valid moves
        if not, the other player wins.
        """
        color = player.get_color()              # checks if player make a single/multiple move
        for row in self._board.get_board():
            for stack in row:
                if color == stack.get_color():
                    return 0
        if player.get_reserve() > 0:            # checks if player can make a reserve move
            return 0
        return 1                                # returns 1 if player has no valid moves

    def next_turn(self, player):
        """
        takes a player who just took a turn,
        makes it the other player's turn, and checks whether that player has
        any legal moves
        """
        self.set_last_player(player)

    def move_piece(self, player_name, src, dst, num_pieces):
        """
        takes a player_name, two tuples with board coordinates in the format (row, column),
        and the number of pieces to be moved.
        allows a player to make a single or multiple move.
        the player_name is the name of the player taking a turn.
        the first tuple is the source coordinate of the stack to be moved from.
        the second tuple is the destination coordinate of the stack to be moved to.
        returns False if move invalid, else
        returns "successfully moved"
        """
        player = self.get_player_from_name(player_name)

        if not self.verify_move(player, dst):
            return False

        if not self.verify_stack_move(player, src, dst, num_pieces):
            return False

        src_stack = self.get_board().get_stack(src)
        dst_stack = self.get_board().get_stack(dst)
        pieces_moved = []

        for piece in range(0, num_pieces):
            pieces_moved.insert(0, src_stack.get_stack()[-1])   # saves pieces to be moved
            src_stack.off_top()                     # takes moved pieces off the source stack

        for piece in pieces_moved:                  # adds the saved pieces to the destination stack
            dst_stack.add(piece)

        while dst_stack.get_height() > 5:           # removes the bottom piece if stack higher than five
            if dst_stack.get_stack()[0] == player.get_color():
                player.inc_reserve()                # reserves removed pieces owned by the player
            else:
                player.inc_captured()               # captures removed pieces owned by opponent
                if player.get_captured() >= 6:
                    return self.player_win(player)
            dst_stack.off_bottom()
        self.next_turn(player)
        if self.check_endgame(self.get_other_player(player)) == 1:
            return self.player_win(player)

        return "successfully moved"

    def reserved_move(self, player_name, coord):
        """
        takes a player name and a tuple representing a location on the board
        places a piece from the player's reserve on a stack on the board
        """
        player = self.get_player_from_name(player_name)
        color = player.get_color()

        if player.get_reserve() < 1:              # prevents move if no pieces in reserve
            return False

        if not self.verify_move(player, coord):
            return False

        dst_stack = self.get_board().get_stack(coord)

        dst_stack.add(color)

        while dst_stack.get_height() > 5:       # removes the bottom piece if stack higher than five
            if dst_stack.get_stack()[0] == player.get_color():
                player.inc_reserve()            # reserves removed pieces owned by the player
            else:
                player.inc_captured()           # captures removed pieces owned by opponent
                if player.get_captured() >= 6:
                    return self.player_win(player)
            dst_stack.off_bottom()

        player.dec_reserve()
        self.next_turn(player)
        if self.check_endgame(self.get_other_player(player)) == 1:
            return self.player_win(player)
        return "successfully moved"

    def show_pieces(self, coord):
        """
        takes a tuple representing a position on the board
        returns a list containing the color of each piece at that position
        index 0 being the bottom of the stack and index 5 the top of the stack.
        """
        return self.get_board().get_stack(coord).get_stack()

    def show_reserve(self, player_name):
        """takes a player's name, returns the number of pieces in their reserve"""
        return self.get_player_from_name(player_name).get_reserve()

    def show_captured(self, player_name):
        """takes a player's name, returns the number of pieces in their reserve"""
        return self.get_player_from_name(player_name).get_captured()
