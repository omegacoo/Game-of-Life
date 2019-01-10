import random
import copy
import os
import time
import json

class Cell():
    
    def __init__(self):
        self.value = random.randint(0,1)
        
    def __eq__ (self, other): 
        return self.is_alive() == other.is_alive()
        
    def die(self):
        self.value = 0
        
    def live(self):
        self.value = 1
    
    def is_alive(self):
        return self.value == 1

class Board():
    
    def __init__(self, width, height, state = []):
        self.width = width
        self.height = height
        self.state = state
        if self.state == []:
            for x in range(self.width):
                self.state.append([Cell()])
                for y in range(self.height-1):
                    self.state[x].append(Cell())
                    
    def __eq__(self, other):
        return self.state == other.state
    
    def to_list(self, state_list):
        new_list = state_list
        for x in range(len(state_list)):
            for y in range(len(state_list[x])):
                new_list[x][y] = self.state[x][y].is_alive()
        return new_list
    
    def unserialize(saved_list):
        saved_list = json.loads(saved_list)
        return saved_list
    
    def to_state(saved_list):
        new_state = Board.unserialize(saved_list)
        for x in range(len(new_state)):
            for y in range(len(new_state[x])):
                if new_state[x][y]:
                    new_state[x][y] = Cell().live()
                else:
                    new_state[x][y] = Cell().die()
        return new_state
    
    def serialize(self):
        state_list = self.to_list(self.state)
        state_serial = json.dumps(state_list)
        return state_serial
    
    def get_cell(self, x, y):
        return self.state[x][y]
    
    def clone(self):
        return Board(self.width, self.height, copy.deepcopy(self.state))
    
    def test_for_neighbors(self, x, y):
        if x == -1 or y == -1 or x == self.width or y == self.height:
            cell = Cell()
            cell.die()
            return cell
        else:
            try:
                return self.state[x][y]
            except:
                cell = Cell()
                cell.die()
                return cell
        
    def get_neighbors(self, x, y):
        neighbors = []
        
        neighbors.append(self.test_for_neighbors(x-1,y-1))
        neighbors.append(self.test_for_neighbors(x,y-1))
        neighbors.append(self.test_for_neighbors(x+1,y-1))
        neighbors.append(self.test_for_neighbors(x-1,y))
        neighbors.append(self.test_for_neighbors(x+1,y))
        neighbors.append(self.test_for_neighbors(x-1,y+1))
        neighbors.append(self.test_for_neighbors(x,y+1))
        neighbors.append(self.test_for_neighbors(x+1,y+1))
        
        return neighbors

class Game():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.keep_on()
    
    def run(self, width, height, state = []):
        x = 0
        self.board = Board(width, height, state)
        self.board_zero = self.board.clone()
        while True:
            os.system('cls')
            self.render()
            print('>> ' + str(x))
            x += 1
            time.sleep(.5)
            last_board = self.board
            self.board = self.next_board()
            next_board = self.next_board()
            if last_board == self.board or last_board == next_board: 
                break
        self.keep_on()
            
        
    def keep_on(self):
        answer = input(
'''Please select from the following options:
    1)New Random Board
    2)Repeat Last Board
    3)Save Last Board
    4)Load a Saved Board
    5)Quit
>''')
        if answer == '1':
            self.run(self.width, self.height, state = [])
        elif answer == '2':
            try:
                self.run(self.width, self.height, self.board_zero.state)
            except:
                print('No Game to Repeat')
                time.sleep(3)
                os.system('cls')
                self.keep_on()
        elif answer == '3':
            f = open('saved_boards.txt','w+')
            f.write(self.board_zero.serialize())    
            f.close()
            os.system('cls')
            self.keep_on()
        elif answer == '4':
            f = open('saved_boards.txt', 'r')
            if f.mode == 'r':
                saved_state = f.read()
            self.board = Board.to_state(saved_state)
            self.run(len(self.board), len(self.board[0]))
        elif answer == '5':
            quit()        
        else:
            print('Not a Valid Selection. Please try again.')
            time.sleep(3)
            os.system('cls')
            self.keep_on()
    
    def live_neighbors(self, x, y):
        alive = 0
        for cell in self.board.get_neighbors(x, y):
            if cell.is_alive():
                alive += 1
        return alive
    
    def next_board(self):
        new_board = self.board.clone()
        
        for x in range(self.width):
            for y in range(self.height):
                
                if self.live_neighbors(x,y) == 0 or self.live_neighbors(x,y) == 1:
                    new_board.get_cell(x,y).die()
                elif self.live_neighbors(x,y) == 3 and not new_board.get_cell(x,y).is_alive():
                    new_board.get_cell(x,y).live()
                elif self.live_neighbors(x,y) > 3:
                    new_board.get_cell(x,y).die()
        
        return new_board

    def render(self):
        temp_board = self.board.clone()
        for x in range(self.width):
            for y in range(self.height):
                if not self.board.state[x][y].is_alive():
                    temp_board.state[x][y] = ' '
                else:
                    temp_board.state[x][y] = '#'
        
        print("__" * self.width + "___")
        
        for x in range(self.width):
            print('| ', end='')
            for y in range(self.height):
                print(str(temp_board.state[x][y]) + ' ', end='')
            print('|')
            
        
        print("--" * self.width + "---")


Game(5,5)