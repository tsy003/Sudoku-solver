import math
import random
import sudoku



def solve(map, update_step=1):
    return _solve_steps(map, update_step, 0, 0)


def _solve_steps(map, update_step, steps, level):
    # Returns:
    #   0: Not solved
    #   1: Solved
    #   2: Given number of steps done (frame_step)

    print("level: %d, steps: %d" % (level, steps))

    if level >= 81:
        # Solved
        return 1
    elif steps >= update_step:
        # The number of specified steps has been done,
        # return out of the solve recursion loop
        # such that the graphics can be updated for the user.
        print("steps done")
        return 2

    # Calculate x and y from recursion level.
    # Each level is the next tile.
    x = level % 9
    y = 0
    if level != 0:
        y = math.floor(level / 9)

    number, preset = map[x][y]

    if preset:
        return _solve_steps(map, update_step, steps, level+1)

    for new_number in range(number, 10):
        if new_number == 0:
            continue


        map[x][y] = (new_number, preset)
        # Check if the new number is valid in the map
        valid, solved = sudoku.sudoku_is_valid(map)

        if solved:
            return 1
        elif valid:
            if new_number != number:
                # Only increase the step count when trying a new number
                # (new combination)
                steps += 1
            solved = _solve_steps(map, update_step, steps, level+1)
            if solved == 1 or solved == 2:
                return solved


    # No valid number possible on this tile
    # Return back to previous tile and try another combination
    map[x][y] = (0, preset)
    return 0






















#
