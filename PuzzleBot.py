import numpy as np

def Main():

    n = 4
    zero_loc = (0,0)
    ordered_array = []

    def generate_order():
        for x in range(0,n*n):
            ordered_array.append(x)

    def generate_puzzle():
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

    def find_number():
        for x in range(0,n):
            for y in range(0,n):
                if puzzle[x,y] == number:
                    number_loc = (x,y)


    puzzle = generate_puzzle()
    find_blank()
    generate_order()
    print(ordered_array)
    #blank_loc = find_blank()


Main()
