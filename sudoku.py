import random
import math

def sudoku_create(size=9, num_preset=10):
    """ @params:
        size:           Grid size for the sudoku map. Default 9x9
        num_preset:     Defines the amount of numbers preset in the sudoku map.

        Returns a 9x9 grid as a 2D list of touples (number, preset)
            number is the initialized number set in the sudoku map
            and preset is a boolean verifying it (useful when solving the sudoku).

        Note the sudoku might not be solvable.
    """
    if size > 12 or size%3 != 0 or num_preset >= (size*size)-1:
        return None

    # Init 2d list
    map = []
    for x in range(size):
        new = []
        for y in range(size):
            new.append((0, False))
        map.append(new)

    # Add preset numbers
    for i in range(num_preset+1):
        max_loops = 10000 # Max loop tries to avoid any infinite loop
        for _ in range(max_loops):
            # Get random x and y position
            x = random.randint(0, size-1)
            y = random.randint(0, size-1)

            # Place a random number at x and y position
            map[x][y] = (random.randint(1, size-1), True)
            valid, solved = sudoku_is_valid(map)
            if not valid:
                # Remove if not valid
                map[x][y] = (0, False)
            else:
                break


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
            if map[x][y][0] == 0:
                # Uninitialized
                solved = False
                continue

            # Check if the same number occurs twice on the horizontal line.
            for next_x in range(x+1, map_len):
                if map[x][y][0] == map[next_x][y][0]:
                    return (False, False)

            # Check if the same number occurs twice on the vertical line.
            for next_y in range(y+1, map_len):
                if map[x][y][0] == map[x][next_y][0]:
                    return (False, False)
    return (True, solved)

def _sudoku_3x3_valid_check(grid):
    solved = True
    for number, preset in grid:
        if number == 0:
            solved = False
            continue
        if preset:
            continue
        c = grid.count((number, False))
        if c > 1:
            return (False, False)
    return (True, solved)


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
        valid, solved_grid = _sudoku_3x3_valid_check(grid) #_sudoku_horizontal_vertical_valid_check(grid)
        if not valid:
            return (False, False)
        elif not solved_grid:
            solved = False

    return (valid, solved)






def sudoku_get_grid(map, grid_index):
    """
        Returns the grid corresponding to the grid index as a 1D list.
    """
    # Calculate starting x and y for the given grid index
    sx = (grid_index % 3) * 3
    sy = math.floor(grid_index / 3) * 3

    grid_map = []
    for x in range(sx, sx+3):
        #new = []
        for y in range(sy, sy+3):
            grid_map.append(map[x][y])

        #grid_map.append(new)

    return grid_map

def sudoku_get_grid_index(x, y):
    """
        Returns the corresponding 3x3 grid index
        from the x and y position in the sudoku map.
    """

    if x == 0:
        grid_x = 0
    else:
        grid_x = math.floor(x / 3)
    if y == 0:
        grid_y = 0
    else:
        grid_y = math.floor(y / 3)

    # if x >= 0 and x <= 2:
    #     grid_x = 0
    # elif x >= 3 and x <= 5:
    #     grid_x = 1
    # else:
    #     grid_x = 2
    #
    # if y >= 0 and y <= 2:
    #     grid_y = 0
    # elif y >= 3 and y <= 5:
    #     grid_y = 1
    # else:
    #     grid_y = 2

    return grid_x+(3*grid_y)
















#
