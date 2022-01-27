import pygame
import sudoku
import sudoku_solver
import random




global screen
global running
global sudoku_map
global font_comic_sans

screen_width = 1200
screen_height = 800
grid_size = 9

# Padding sudoku board on the main window screen in pixels
pad_left = 300
pad_right = 20
pad_top = 20
pad_bot = 20
pad_offset = 0
pad_3x3 = 6



def sudoku_render():
    screen.fill((0, 0, 0))


    width = round((screen_width-pad_left-pad_right - pad_offset*grid_size - pad_3x3*2) / grid_size)
    height = round((screen_height-pad_top-pad_bot - pad_offset*grid_size - pad_3x3*2) / grid_size)

    # mid and dark aubergine colour
    colours = ((94, 39, 80), (44, 0, 30))

    xpos = pad_left
    for x in range(9):

        ypos = pad_top
        for y in range(9):
            # Render bg box
            pygame.draw.rect(screen, colours[(x+y)%2], (xpos, ypos, width, height))

            # Render text if it has been set
            val, preset = sudoku_map[x][y]
            if val != 0:
                text_surf = font_comic_sans.render(str(val), False, (0, 0, 0))
                text_width, text_height = font_comic_sans.size(str(val))
                # Text offset to middle of a tile
                text_offset_x = (width / 2) - (text_width/2)
                text_offset_y = (height / 2) - (text_height/2)
                screen.blit(text_surf, (xpos+text_offset_x, ypos+text_offset_y))

            ypos += height+pad_offset
            # Add 3x3 grid padding
            if y != 0 and y % 3 == 2:
                ypos += pad_3x3

        xpos += width+pad_offset
        # Add 3x3 grid padding
        # (must be added before every modulo 0 since it takes effect on the next loop)
        # thus we get x % 3 == 2
        if x != 0 and x % 3 == 2:
            xpos += pad_3x3





if __name__ == "__main__":
    pygame.font.init()

    screen = pygame.display.set_mode(size=(screen_width, screen_height), flags=0, depth=0, display=0)
    pygame.display.set_caption('Sudoku')
    running = True
    print("Starting game loop\n")

    sudoku_map = sudoku.sudoku_create(num_preset=5)
    font_comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
    solve = 2

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event. type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        # Run the sudoku solver as long as solve == 2
        if solve == 2:
            solve = sudoku_solver.solve(sudoku_map, update_step=20)
            if solve == 1:
                print("Sudoku solved")
                print(sudoku_map)
            elif solve == 0:
                print("sudoku not solvable")
        sudoku_render()
        pygame.display.flip()

























#
