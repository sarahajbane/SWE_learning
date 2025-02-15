### INTERACTIVE
##titanic_row = input('Enter a number from 0-9 for the inital titanic row')
##titanic_col = input('Enter a number from 0-9 for the inital titanic column')
##iceberg_row = input('Enter a number from 0-9 for the inital iceberg row')
##iceberg_col = input('Enter a number from 0-9 for the inital iceberg row')
##titanic_pos = [int(titanic_row), int(titanic_col)]
##iceberg_pos = [int(iceberg_row), int(iceberg_col)]
##grid_size = input('Enter a number from 1-20 to determine gridsize')
##ocean =  int(grid_size)

# NON INTERACTIVE:

ocean =  10
titanic_row = 4
titanic_col = 8
iceberg_row = 4
iceberg_col = 4
iceberg_pos = [iceberg_row, iceberg_col]
titanic_pos = []


def auto_pilot_next_step(titanic_row,titanic_col,ocean):
    r = titanic_row
    c = titanic_col
    global titanic_pos
    titanic_pos = [r,c]
    draw_ocean(ocean,titanic_pos,iceberg_pos)
    print("* * * * * * * * * * *")
    while r in range(ocean) and c in range(ocean):
        if c >= 0 and get_cell(r, c - 1) == '🧊': 
            if r > 0 and get_cell(r - 1, c) != '🧊':    # if ship next to ice, move north
                titanic_pos[0] = titanic_pos[0]-1 
                draw_ocean(ocean,titanic_pos,iceberg_pos)
                print("* * * * * * * * * * *")
               
            elif r == 0 and get_cell(r - 1, c) == '🧊': # if north & next to ice, move south
                titanic_pos[0] = titanic_pos[0] +1 
                draw_ocean(ocean,titanic_pos,iceberg_pos)
                print("* * * * * * * * * * *")
        else:                                       # if all clear, move ship west
            titanic_pos[1]= titanic_pos[1]-1 
            draw_ocean(ocean,titanic_pos,iceberg_pos)
            print("* * * * * * * * * * *")
        r,c = titanic_pos
                     
def get_cell(iceberg_row, iceberg_col):
    if [iceberg_row, iceberg_col] == iceberg_pos:
        return '🧊'
    else:
        return '🌊'
    
def draw_ocean(ocean,titanic_pos,iceberg_pos):
    o = int(ocean)
    for row in range(o):
        for col in range(o):
            if [row, col] == titanic_pos:
                print('🚢', end='')
            elif [row, col] == iceberg_pos:
                print('🧊', end='')
            else:
                print('🌊', end='')
        print()
    if titanic_pos[1] < 0:
        print("* * * * * * * * * * *")
        print('Congratulations, you saved the Titanic!') 
        
auto_pilot_next_step(titanic_row,titanic_col,ocean)



## Next steps:
## add multiple icebergs & ships (3 & 3 / 15*15  grid)
## def manual_pilot() to use arrow inputs for single ship
## 
## def NORTH SOUTH WEST EAST separately to move ship and call in the pilot functions
## optional:
## (randint req for multiple moving icebergs i.e. randomwalk)
## def own randint() function
## include random integers in a range for start positions instead of user inputs
## include random integers in a range for number of icebergs    
