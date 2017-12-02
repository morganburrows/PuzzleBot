import numpy as np

def Main():

    n = 4
    zero_loc = (0,0)

    #solved_tile_map = np.matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')

    def rand_puzzle_generator():
        rands = np.random.choice(n*n, (n*n), replace = False)
        empty_tile = np.empty([n,n])

        for x in range(0,n):
            for y in range(0,n):
                empty_tile[x,y] = rands[0]
                rands = np.delete(rands,0)
                #print(rands)

        print(empty_tile)
        return(empty_tile)

    def find_blank():
        for x in range(0,n):
            for y in range(0,n):
                #print('cord', x, y)
                #print('val', puzzle[x,y])
                if puzzle[x,y] == 0:
                    zero_loc = (x, y)
                    #print('success', zero_x, zero_y)



    puzzle = rand_puzzle_generator()
    find_blank()
    #blank_loc = find_blank()


Main()
