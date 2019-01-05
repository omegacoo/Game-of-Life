import random
import copy
import os
import time

class Board:
 
    def __init__(self, name):
        self.name = name
    
    def dead_state(self, width, height):              #create a grid of dead cells
        dead_board = []
        
        for y in range(height):
            dead_board.append([0])
            for n in range(width-1):
                dead_board[y].append(0)
        
        return dead_board
    
    def random_state(self, width, height):            #create a grid of live and dead cells randomly
        state = self.dead_state(width, height)
        
        for y in range(height):
            for x in range(width):
                state[y][x] = random.randint(0, 1)
        
        return state
    
    def test_neighbors_no_wrap(self, state, x, y):
        if x == -1 or y == -1:                        
            return 0                                  
        else:
            try:
                return state[y][x]
            except:
                return 0
    
    def test_neighbors_with_wrap(self, state, x, y):
            try:
                return state[y][x]
            except:
                return 0
            
    def get_neighbors(self, state, x, y):             #check number of live neighbors
        live_neighbors = 0
        
        live_neighbors += self.test_neighbors_no_wrap(state, x-1, y-1)
        live_neighbors += self.test_neighbors_no_wrap(state, x, y-1)
        live_neighbors += self.test_neighbors_no_wrap(state, x+1, y-1)
        live_neighbors += self.test_neighbors_no_wrap(state, x-1, y)
        live_neighbors += self.test_neighbors_no_wrap(state, x+1, y)
        live_neighbors += self.test_neighbors_no_wrap(state, x-1, y+1)
        live_neighbors += self.test_neighbors_no_wrap(state, x, y+1)
        live_neighbors += self.test_neighbors_no_wrap(state, x+1, y+1)
    
        return live_neighbors
    
    def next_board_state(self, state):                      #calculate the next board
        height = len(state)                           
        width = len(state[0])                         
        new_state = copy.deepcopy(state)              
        
        for y in range(height):
            for x in range(width):
                
                live_neighbors = self.get_neighbors(state, x, y)
                
                #if each element for 0-1 live neighbors kill it
                if live_neighbors == 0 or live_neighbors == 1:
                    new_state[y][x] = 0
                
                if live_neighbors == 2 or live_neighbors == 3:
                    
                    #if each element for 3 live neighbors
                    if state [y][x] == 0 and live_neighbors == 3:
                        new_state[y][x] = 1 
                    
                #if each element for >3 live neighbors kill it
                if live_neighbors > 3:
                    new_state[y][x] = 0      
                    
                    
        return new_state
    
    def render(self, state):                               #make it pretty
        height = len(state)
        width = len(state[0])
        
        for y in range(height):
            for x in range(width):
                if state[y][x] == 0:
                    state[y][x] = ' '
                else:
                    state[y][x] = '#'
        
        print("__" * width + "___")
        
        for y in range(height):
            print('| ', end='')
            for x in range(width):
                print(str(state[y][x]) + ' ', end='')
            print('|')
            
        
        print("--" * width + "---")
        
        return
    
    def run(self, width, height):
        
        os.system('cls')
        state = Board.random_state(self, width, height)
        new_state = copy.deepcopy(state)
        Board.render(self, new_state)
        x = 0
        print('>> ' + str(x))
        last_state = []
        
        while True:
            time.sleep(1)
            os.system('cls')
            state = Board.next_board_state(self, state)
            new_state = copy.deepcopy(state)
            Board.render(self, new_state)
            x += 1
            print('>> ' + str(x))
            if new_state == last_state:
                break
            last_state = copy.deepcopy(new_state)


initial_state = Board('')
initial_state.run(10,10)