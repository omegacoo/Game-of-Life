import random
import os
import time

class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.new_state = []
        self.board = Board(width, height)
        self.board = Board.initial_board(self.board)
        self.render()
        self.board = self.next_board_state()


    def render(self):
        print("__" * self.width + "___")
        for x in range(self.width):
            print('| ', end='')
            for y in range(self.height):
                if self.board[x][y] == 0:
                    print('  ', end='')
                else:
                    print('# ', end='')
            print('|')
        print("--" * self.width + "---")

    def next_board_state(self):
        self.new_state = []

        for x in range(self.width):
            for y in range(self.height):

                live_neighbors = Board.get_neighbors(self.board, x, y)

                if live_neighbors == 0 or live_neighbors == 1:
                    self.new_state[x][y] = 0

                if self.new_state[x][y] == 0 and live_neighbors == 3:
                    self.new_state[x][y] = 1

                if live_neighbors > 3:
                    self.new_state[x][y] = 0

        return self.new_state


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = []
        self.initial_board()

    def initial_board(self):
        for x in range(self.width):
            self.state.append([Cell().value])
            for y in range(self.height):
                self.state[x].append(Cell().value)
        return self.state

    def test_neighbors_no_wrap(self, x, y):
        if x == -1 or y == -1:
            return 0
        else:
            return self.state[x][y]

    def get_neighbors(self, x, y):
        live_neighbors = 0

        live_neighbors += self.test_neighbors_no_wrap(x-1, y-1)
        live_neighbors += self.test_neighbors_no_wrap(x, y-1)
        live_neighbors += self.test_neighbors_no_wrap(x+1, y-1)
        live_neighbors += self.test_neighbors_no_wrap(x-1, y)
        live_neighbors += self.test_neighbors_no_wrap(x+1, y)
        live_neighbors += self.test_neighbors_no_wrap(x-1, y+1)
        live_neighbors += self.test_neighbors_no_wrap(x, y+1)
        live_neighbors += self.test_neighbors_no_wrap(x+1, y+1)

        return live_neighbors

class Cell:

    def __init__(self):
        self.value = random.randint(0, 1)

    def is_it_alive(self, value):
        if self.value == 0:
            return False
        else:
            return True

    def kill(self):
        self.value = 0

    def resurrect(self):
        self.value = 1


board_one = Game(10,10)