import random

def sudoku_create(size=9, num_preset=4):
    """ @params:
        size:           Grid size for the sudoku map. Default 9x9
        num_preset:     Defines the amount of numbers preset in the sudoku map.
    """
    if size > 12 or size%3 != 0 or num_preset >= (size*size)-1:
        return None

    # Init 2d list
    map = []
    for x in range(size):
        new = []
        for y in range(size):
            new.append(0)
        map.append(new)

    # Add preset numbers
    

    return map
