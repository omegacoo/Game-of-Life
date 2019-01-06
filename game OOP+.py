import random
import os
import time

class Game:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = Board(width, height)
        self.board = Board.initial_board(self.board)
        
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = []
        
    def initial_board(self):
        for x in range(self.width):
            self.state.append([Cell().value])
            for y in range(self.height):
                self.state[x].append(Cell().value)
        return self.state
    
    def render(self):
        
        print("__" * self.width + "___")
        
        for x in range(self.width):
            print('| ', end='')
            for y in range(self.height):
                if self.state[x][y] == 0:
                    print('  ', end='')
                else:
                    print('# ', end='')
                
            print('|')
            
        print("--" * self.height + "---")
    
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

board_one = Board(5,5)
board_one.initial_board()
board_one.render()