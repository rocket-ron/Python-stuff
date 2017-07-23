import random


class MarblesBoard:
    """A marbles board game

    In a particular board game, there are N spaces in a row, numbered 0 through N - 1 from left to right.
    There are also N marbles, numbered 0 through N - 1, initially placed in their corresponding spaces.

    There are two moves available on the board once it has been set up:
    Switch: Switch the marbles in positions 0 and 1, and
    Rotate: Move the marble in position 0 to position N - 1, and move all other marbles one space to the left (one index lower).

    The objective is to arrange the marbles in order, with each marble i in position i.

    To set up the Marbles Board, create an instance of the MarblesBoard class and then call the class like a function with a
    variable number of integers in any sequence. """

    def __init__(self):
        """ Create a new instance of the Marble board list object"""
        self._board = []
        return

    def __call__(self, *args):
        """ Place the initial objects into the Marble Board"""
        """ Clear the current board if there's anything in it """
        del self._board[:]
        for arg in args:
            if arg not in self._board:
                self._board.append(arg)
            else:
                print('Illegal board setup: there can only be 1 of each marble, but you have put in duplicates')
        return

    def __str__(self):
        return ' '.join(str(position) for position in self._board)

    def __repr__(self):
        return ' '.join(str(position) for position in self._board)

    def switch(self):
        """ Switch the first and second items in the list"""
        if len(self._board) > 1:
            a = self._board[0]
            self._board[0] = self._board[1]
            self._board[1] = a
        return

    def rotate(self):
        """Move the item at the beginning of the list to the end of the list"""
        if len(self._board) > 1:
            self._board.append(self._board.pop(0))
        return

    def is_solved(self):
        """ Check to see if the board is in order from right to left, lowest to highest"""
        s = True
        for i in range(0, len(self._board) - 1):
            if self._board[i] > self._board[i + 1]:
                s = False
                break
        return s

    def first_two_marbles(self):
        """Return the first two marbles on the board. If there are less than two, return just the one marble"""
        if len(self._board) > 1:
            return (self._board[0], self._board[1])
        elif len(self._board) == 1:
            return (self._board[0])
        else:
            return None

    def create_board(self, size):
        """ create a MarbleBoard of size and randomly populate with marbles """
        del self._board[:]
        self._board = random.sample(range(0, size), size)
        return


class Solver:
    """Solve a MarblesBoard game in the least possible moves
    Given a populated MarblesBoard object, call the switch(), rotate() and is_solved() methods until the
    MarblesBoard indicates is_solved() is True """

    def __init__(self, board):
        self._board = board
        self._moves = 0
        return

    def __str__(self):
        return str(self._board)

    def __repr__(self):
        return str(self._board)

    def solve(self):
        """ Solve the Marbles board
        The strategy is to look at the first two marbles and decide the move based on what they are.
        If one of the first two marbles is 0, then we are restricted to a rotate move.
        Otherwise we will switch the two marbles if the first is larger than the second, and
        we will rotate the marbles if the second is larger than the first.

        Each time we make a move we increment the move counter and print out the state of the board.
        We don't stop until the board indicates that it is solved. """

        while not self._board.is_solved():
            firstTwoMarbles = self._board.first_two_marbles()
            if 0 in firstTwoMarbles:
                """ all we can do is a rotate move in this case """
                self._board.rotate()
            elif firstTwoMarbles[0] > firstTwoMarbles[1]:
                """ if the first marble is greater than the second marble, switch them """
                self._board.switch()
            else:
                self._board.rotate()
            self._moves += 1
            print(self._board)
        print('Solved in {0} moves'.format(self._moves))
