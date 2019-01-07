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
        self.board = Board(self.width, self.height).board
        self.counter = 0
        self.render()
        print('> ' + str(self.counter))
        while True:
            self.last_board = copy.deepcopy(self.board)
            self.board = self.next_board()
            if self.last_board == self.board or self.last_board == self.next_board():#end on repeated board states
                break
            time.sleep(1)
            os.system('cls')
            self.render()
            self.counter += 1
            print('> ' + str(self.counter))

    def keep_on(self):
        answer = input('Continue? Y/N | ')
        if answer == 'N' or answer == 'n':
            quit()

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
        self.new_board = copy.deepcopy(self.board)
        for x in range(self.width):
            for y in range(self.height):
                alive = self.live_neighbors(x,y)

                if alive == 0 or alive == 1:
                    self.new_board[x][y].kill()
                if alive == 3 and self.new_board[x][y].is_alive() == False:
                    self.new_board[x][y].resurrect()
                if alive > 3:
                    self.new_board[x][y].kill()
        return self.new_board


    def live_neighbors(self, x, y):
        list_of_neighbors = self.board.get_neighbors(x,y)
        alive = 0
        for i in range(len(list_of_neighbors)):
            if i == True:
                alive += 1
        return alive

class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self.start_board()

    def start_board(self):
        for x in range(self.width):
            self.board.append([Cell()])
            for y in range(self.height):
                self.board[x].append(Cell())
        return self.board

    def get_cell(self, x, y):
        try:
            return self.board[x][y].is_alive()
        except:
            pass

    def get_neighbors(self, x, y):
        neighbors = []

        neighbors.append(self.get_cell(x-1, y-1))
        neighbors.append(self.get_cell(x, y-1))
        neighbors.append(self.get_cell(x+1, y-1))
        neighbors.append(self.get_cell(x-1, y))
        neighbors.append(self.get_cell(x+1, y))
        neighbors.append(self.get_cell(x-1, y+1))
        neighbors.append(self.get_cell(x, y+1))
        neighbors.append(self.get_cell(x+1, y+1))

        return neighbors


class Cell():

    def __init__(self):
        self.value = random.randint(0,1)

    def kill(self):
        self.value = 0

    def resurrect(self):
        self.value = 1

    def is_alive(self):
        return self.value == 1

Game(5,5)