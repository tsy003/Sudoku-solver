import random
import math

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
    for i in range(num_preset):
        # Get random x and y position
        x = random.randint(0, size)
        y = random.randint(0, size)

        # Place a random number at x and y position
        map[x][y] = random.randint(0, size)

        sudoku_is_valid(map)

        # Get 3x3 grid location
        grid_index = sudoku_get_grid_index(x, y)


    return map

def _sudoku_horizontal_vertical_valid_check(map):
    # Note:
        # Solved here might not actually be solved
        # since it might not have checked if 3x3 grid is valid yet.
    map_len = len(map)

    solved = True

    # Horizontal and vertical check
    for x in range(map_len):
        for y in range(map_len):
            if map[x][y] == 0:
                # Uninitialized
                solved = False
                continue

            # Check if the same number occurs twice on the horizontal line.
            for next_x in range(x+1, map_len):
                if map[x][y] == map[next_x][y]:
                    return (False, False)

            # Check if the same number occurs twice on the vertical line.
            for next_y in range(y+1, map_len):
                if map[x][y] == map[x][next_y]:
                    return (False, False)

def sudoku_is_valid(map):
    """
        Checks if the given sudoku map is valid, ie. consist of unique numbers.
        Order checked:
            Horizontal & Vertical -> 3x3 grid

        Returns boolean touple as (valid, is_solved), e.g: Return (True, False)
    """

    # Check vorizontal and vertical lines on the sudoku map
    valid, solved = _sudoku_horizontal_vertical_valid_check(map)
    if not valid:
        return (False, False)

    # Check 3x3 grid
    for i in range(9):
        grid = sudoku_get_grid(map, i)
        # For each grid, check if it's valid.
        valid, solved_grid = _sudoku_horizontal_vertical_valid_check(grid)
        if not valid:
            return (False, False)
        elif not solved_grid:
            solved = False

    return (valid, solved)






def sudoku_get_grid(map, grid_index):
    """
        Returns the grid corresponding to the grid index as a 2d list.
    """
    # Calculate starting x and y for the given grid index
    sx = (grid_index % 3) * 3
    sy = math.floor(grid_index / 3) * 3

    grid_map = []
    for x in range(sx, sx+3):
        new = []
        for y in range(sy, sy+3):
            new.append(map[x][y])

        grid_map.append(new)

    return grid_map

def sudoku_get_grid_index(x, y):
    """
        Returns the corresponding 3x3 grid index
        from the x and y position in the sudoku map.
    """
    if x >= 0 and x <= 2:
        grid_x = 0
    elif x >= 3 and x <= 5:
        grid_x = 1
    else:
        grid_x = 2

    if y >= 0 and y <= 2:
        grid_y = 0
    elif y >= 3 and y <= 5:
        grid_y = 1
    else:
        grid_y = 2

    return grid_x+(3*grid_y)
















#
