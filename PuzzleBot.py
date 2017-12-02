import numpy as np

def Main():

    n = 4

    solved_tile_map = np.matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')

    rands = np.random.choice(n*n, (n*n), replace = False)
    empty_tile = np.empty([n,n])

    for x in range(0,n):
        for y in range(0,n):
            empty_tile[x,y] = rands[0]
            rands = np.delete(rands,0)
            print(rands)




    print(empty_tile)

Main()
