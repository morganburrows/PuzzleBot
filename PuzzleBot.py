import numpy as np

def Main():

    n = 4
    ordered_array = []

    def generate_order():   #generate a random N length array
        for x in range(0,n*n):
            ordered_array.append(x)

    def generate_puzzle():  #populate an NxN matrix with randomized array
        rands = np.random.choice(n*n, (n*n), replace = False)
        empty_tile = np.empty([n,n])

        for x in range(0,n):
            for y in range(0,n):
                empty_tile[x,y] = rands[0]
                rands = np.delete(rands,0)
                #print(rands)

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

    def trade_up():
        number_loc = find_number(9)
        blank_loc = find_blank()
        #print(number_loc, blank_loc)
        print(number_loc[0], (blank_loc[0]-1))
        if number_loc[1] == blank_loc[1] and number_loc[0] == (blank_loc[0]-1):
            print(number_loc[0], (blank_loc[0]-1))
            holding_loc = number_loc
            puzzle[number_loc] = puzzle[blank_loc]
            puzzle[blank_loc] = puzzle[holding_loc]
            print(number_loc, blank_loc, holding_loc)
        else: print('error')

    #def trade_down():
    #def trade_left():
    #def trade_right():


    puzzle = generate_puzzle()
    find_blank()
    generate_order()
    trade_up()
    print(puzzle)


Main()
