import random
import copy
import os
import time

class Cell():
    
    def __init__(self):
        self.value = random.randint(0,1)
        
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
                for y in range(self.height):
                    self.state[x].append(Cell())
    
    def __eq__(self, other):
        return self.state == other.state
    
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
        self.run()
    
    def run(self):
        x = 0
        self.board = Board(self.width, self.height)
        while True:    
            os.system('cls')
            self.render()
            print('>> ' + str(x))
            x += 1
            time.sleep(1)
            self.board = self.next_board()
            
        
    def keep_on(self):
        answer = input('Continue? Y/N | ')
        if answer == 'N' or answer == 'n':
            quit()
        
    def live_neighbors(self, x, y):
        alive = 0
        for cell in self.board.get_neighbors(x, y):
            if cell.is_alive() == True:
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
                if self.board.state[x][y].is_alive() == False:
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










