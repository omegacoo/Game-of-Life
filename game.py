import random
import copy
import os
import time

def dead_state(width, height): #create a grid of dead cells
    dead_board = []
    
    for i in range(height):
        dead_board.append([0])
        for n in range(width-1):
            dead_board[i].append(0)
    
    return dead_board

def random_state(width, height): #create a grid of live and dead cells randomly
    state = dead_state(width, height)
    
    for element in range(height):
        for i in range(width):
            state[element][i] = random.randint(0, 1)
    
    return state

def next_board_state(state):
    height = len(state)
    width = len(state[0])
    new_state = copy.deepcopy(state)
    
    for i in range(height):
        for x in range(width):
            #check number of live neighbors
            live_neighbors = 0
            
            if i == 0 and x == 0: #top left corner
                if state[i][x+1] == 1:
                    live_neighbors += 1
                if state[i+1][x] == 1:
                    live_neighbors += 1
                if state[i+1][x+1] == 1:
                    live_neighbors += 1
                    
            elif i == 0 and x == width - 1: #top right corner
                if state[i][x-1] == 1:
                    live_neighbors += 1
                if state[i+1][x] == 1:
                    live_neighbors += 1
                if state[i+1][x-1] == 1:
                    live_neighbors += 1
            
            elif i == height - 1 and x == 0: #bottom left corner
                if state[i-1][x] == 1:
                    live_neighbors += 1
                if state[i-1][x+1] == 1:
                    live_neighbors += 1
                if state[i][x+1] == 1:
                    live_neighbors += 1
                    
            elif i == height - 1 and x == width - 1: #bottom right corner
                if state[i-1][x-1] == 1:
                    live_neighbors += 1
                if state[i-1][x] == 1:
                    live_neighbors += 1
                if state[i][x-1] == 1:
                    live_neighbors += 1
                    
            elif i == 0: #top row
                if state[i][x-1] == 1:
                    live_neighbors += 1
                if state[i][x+1] == 1:
                    live_neighbors += 1
                if state[i+1][x-1] == 1:
                    live_neighbors += 1
                if state[i+1][x] == 1:
                    live_neighbors += 1
                if state[i+1][x+1] == 1:
                    live_neighbors += 1
                    
            elif x == 0: #left column
                if state[i-1][x] == 1:
                    live_neighbors += 1
                if state[i-1][x+1] == 1:
                    live_neighbors += 1
                if state[i][x+1] == 1:
                    live_neighbors += 1
                if state[i+1][x] == 1:
                    live_neighbors += 1
                if state[i+1][x+1] == 1:
                    live_neighbors += 1
                        
            elif x == width - 1: #right column
                if state[i-1][x-1] == 1:
                    live_neighbors += 1
                if state[i-1][x] == 1:
                    live_neighbors += 1
                if state[i][x-1] == 1:
                    live_neighbors += 1
                if state[i+1][x-1] == 1:
                    live_neighbors += 1
                if state[i+1][x] == 1:
                    live_neighbors += 1
            
            elif i == height - 1: #bottom row
                if state[i][x-1] == 1:
                    live_neighbors += 1
                if state[i-1][x-1] == 1:
                    live_neighbors += 1
                if state[i-1][x] == 1:
                    live_neighbors += 1
                if state[i-1][x+1] == 1:
                    live_neighbors += 1
                if state[i][x+1] == 1:
                    live_neighbors += 1
                    
            else:
                if state[i-1][x-1] == 1:
                    live_neighbors += 1
                if state[i-1][x] == 1:
                    live_neighbors += 1
                if state[i-1][x+1] == 1:
                    live_neighbors += 1
                if state[i][x-1] == 1:
                    live_neighbors += 1
                if state[i][x+1] == 1:
                    live_neighbors += 1
                if state[i+1][x-1] == 1:
                    live_neighbors += 1
                if state[i+1][x] == 1:
                    live_neighbors += 1
                if state[i+1][x+1] == 1:
                    live_neighbors += 1
                    
            #if each element for 0-1 live neighbors kill it
            if live_neighbors == 0 or live_neighbors == 1:
                new_state[i][x] = 0
                
            #if each element for 2-3 live neighbors leave it
            if live_neighbors == 2 or live_neighbors == 3:
                #if each element for 3 live neighbors
                if state [i][x] == 0 and live_neighbors == 3:
                    new_state[i][x] = 1 
                
            #if each element for >3 live neighbors kill it
            if live_neighbors > 3:
                new_state[i][x] = 0      
                
                
    return new_state
    
def render(state):
    height = len(state)
    width = len(state[0])
    
    for i in range(height):
        for x in range(width):
            if state[i][x] == 0:
                state[i][x] = ' '
            else:
                state[i][x] = '#'
    
    print("__" * width + "___")
    
    for i in range(height):
        print('| ', end='')
        for x in range(width):
            print(str(state[i][x]) + ' ', end='')
        print('|')
        
    
    print("--" * width + "---")
    
    return

os.system('cls')
state = random_state(5,5)
new_state = copy.deepcopy(state)
render(new_state)
x = 0
print('>> ' + str(x))
last_state = []

while True:
        time.sleep(1)
        os.system("cls")
        state = next_board_state(state)
        new_state = copy.deepcopy(state)
        render(new_state)
        x += 1
        print('>> ' + str(x))
        if new_state == last_state:
            break
        last_state = copy.deepcopy(new_state)