import random
import copy
import os
import time

class Game():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        while True:
            self.run()
            self.keep_on()
            os.system('cls')

    def run(self):
        self.board = Board(self.width, self.height).starting_board()
        self.counter = 0
        self.render()
        print('> ' + str(self.counter))
        while True:
            self.last_board = copy.deepcopy(self.board)
            self.board = self.next_board()
            if self.last_board == self.board:
                break
            else:
                pass
            time.sleep(1)
            os.system('cls')
            self.render()
            self.counter += 1
            print('> ' + str(self.counter))

    def keep_on(self):
        answer = input('Continue? Y/N | ')
        if answer == 'N':
            quit()
        else:
            return True

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

    def next_board(self):
        self.new_state = copy.deepcopy(self.board)
        for x in range(self.width):
            for y in range(self.height):
                self.live_neighbors = self.get_neighbors(x, y)

                if self.live_neighbors == 0 or self.live_neighbors == 1:
                    self.new_state[x][y] = 0

                if self.board[x][y] == 0 and self.live_neighbors == 3:
                    self.new_state[x][y] = 1

                if self.live_neighbors > 3:
                    self.new_state[x][y] = 0
        return self.new_state

    def test_neighbors_no_wrap(self, x, y):
        if x == -1 or x == self.width or y == -1 or y == self.height:
            return 0
        else:
            try:
                return self.board[x][y]
            except:
                return 0

    def get_neighbors(self, x, y):
        self.live_neighbors = 0

        self.live_neighbors += self.test_neighbors_no_wrap(x-1, y-1)
        self.live_neighbors += self.test_neighbors_no_wrap(x, y-1)
        self.live_neighbors += self.test_neighbors_no_wrap(x+1, y-1)
        self.live_neighbors += self.test_neighbors_no_wrap(x-1, y)
        self.live_neighbors += self.test_neighbors_no_wrap(x+1, y)
        self.live_neighbors += self.test_neighbors_no_wrap(x-1, y+1)
        self.live_neighbors += self.test_neighbors_no_wrap(x, y+1)
        self.live_neighbors += self.test_neighbors_no_wrap(x+1, y+1)

        return self.live_neighbors

class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = []
        self.starting_board()

    def starting_board(self):
        for x in range(self.width):
            self.state.append([Cell().value])
            for y in range(self.height):
                self.state[x].append(Cell().value)
        return self.state


class Cell():

    def __init__(self):
        self.value = random.randint(0,1)

board = Game(5,5)
