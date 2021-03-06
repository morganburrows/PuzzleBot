import numpy as np

def Main():

    n = 4
    rand_array = []
    ordered_array = list(range(1,n*n))
    ordered_array.append(0)
    #print(ordered_array)


    def generate_puzzle():  #populate an NxN matrix with randomized array
        rands = np.random.choice(n*n, (n*n), replace = False)
        empty_tile = np.empty([n,n])

        for x in range(0,n):
            for y in range(0,n):
                #print(rands)
                empty_tile[x,y] = rands[0]
                rands = np.delete(rands,0)

        print(empty_tile)   #print the original random matrix
        return(empty_tile)

    def find_blank():       #locate the coordinates of the 0 tile (to be blank)
        for x in range(0,n):
            for y in range(0,n):
                #print('cord', x, y)
                #print('val', puzzle[x,y])
                if puzzle[x,y] == 0:
                    loc = (x, y)
                    return loc

    def find_number(number):    #return location of a desired number
        for x in range(0,n):
            for y in range(0,n):
                if puzzle[x,y] == number:
                    loc = (x,y)
                    return loc

    def trade_up():     #swaps the blank tile with the one above it
        blank_loc = find_blank()
        number_loc = (blank_loc[0]-1, (blank_loc[1]))
        if blank_loc[0]-1 != -1:
            if number_loc[1] == blank_loc[1] and number_loc[0] == (blank_loc[0]-1):
                holding_val = puzzle[number_loc]
                puzzle[number_loc] = puzzle[blank_loc]
                puzzle[blank_loc] = holding_val
                blank_loc = find_blank()
                print('traded up')
        else: print('error - out of bounds')
        print(puzzle)

    def trade_down():   #swaps the blank tile with the one below it
        blank_loc = find_blank()
        number_loc = ((blank_loc[0]+1),blank_loc[1])
        if blank_loc[0]+1 != n:
            if (number_loc[1] == blank_loc[1]) and (number_loc[0] == (blank_loc[0]+1)):
                holding_val = puzzle[number_loc]
                puzzle[number_loc] = puzzle[blank_loc]
                puzzle[blank_loc] = holding_val
                blank_loc = find_blank()
                print('traded down')
        else: print('error - out of bounds')
        print(puzzle)

    def trade_left():   #swaps the blank tile with the one left of it
        blank_loc = find_blank()
        number_loc = (blank_loc[0], blank_loc[1]-1)
        if blank_loc[1]-1 != -1:
            if (number_loc[1]+1) == blank_loc[1] and number_loc[0] == blank_loc[0]:
                holding_val = puzzle[number_loc]
                puzzle[number_loc] = puzzle[blank_loc]
                puzzle[blank_loc] = holding_val
                blank_loc = find_blank()
                print('traded left')
        else: print('error - out of bounds')
        print(puzzle)

    def trade_right():  #swaps the blank tile with the one right of it
        blank_loc = find_blank()
        number_loc = (blank_loc[0], blank_loc[1]+1)
        if blank_loc[1]+1 != n:
            if (number_loc[1]-1) == blank_loc[1] and number_loc[0] == blank_loc[0]:
                holding_val = puzzle[number_loc]
                puzzle[number_loc] = puzzle[blank_loc]
                puzzle[blank_loc] = holding_val
                blank_loc = find_blank()
                print('traded right')
        else: print('error - out of bounds')
        print(puzzle)

    def check_solved(): #checks puzzle against ordered NxN array
        a = 0
        for x in range(0,n):
            for y in range(0,n):
                if puzzle[x,y] != ordered_array[a]:
                    return False
                else: a += 1
        if a == n*n:
            return True

    #begin algorithm

    #process: order array from lowest to highest
    #method: 0 is blank space, ignore in ordering.
    #space can be thought of as 2x2 and 2x4/4x2 "circular" sets of 4 and 8 respectively
    #goal of a "reorder" should be to rotate the circular set to bring the smallest number
    #in the set to the desired position.

    def puzzle_bot():
        #first order of business: make bot bring 1 to position 1
        for current_number in range (1,n*n):
            solved = False
            for x in range(0,n):
                if solved == False:
                    for y in range(0,n):
                        print('searching for', current_number)
                        if puzzle[x,y] == current_number:
                            loc = puzzle[x,y]
                            #
                            make_ordered(current_number, (x,y), ordered_array)
                            #
                            print('-----> solved for', loc)
                            solved = True
                            break
                elif solved == True:
                    solved = False
                    break
                    #print('break failed')

    def pbot():
        for number in range(1,n*n):
            location = find_number(number)
            print(location, puzzle[location])

    def make_ordered(current_number, location, key_array):
        print(current_number, location, key_array[current_number-1])
        if current_number == 1:
            print('bring up')
            print('bring left')




    #process execution order
    puzzle = generate_puzzle()
    find_blank()
    puzzle_bot()

    running = False
    while running:
        key_in = input('Puzz:')
        if key_in == "quit":
            break
        elif key_in == 'w':
            trade_up()
        elif key_in == 's':
            trade_down()
        elif key_in == 'a':
            trade_left()
        elif key_in == 'd':
            trade_right()
        elif key_in == '':
            print(puzzle)
        if check_solved() == True or key_in == 'winstate':
            print('PUZZLE SOLVED')
            key_in = input('PLAY AGAIN? (Y/N)\n')
            if key_in == "Y" or key_in == "y":
                puzzle  = generate_puzzle()
            elif key_in == "N" or key_in == "n":
                print('Thanks For Playing!')
                break



Main()
