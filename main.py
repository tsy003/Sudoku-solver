import pygame
import sudoku
import sudoku_solver
import random
import math

"""
    Increase the solve speed by increasing fps and/or update_render_step.

"""


global screen
global running
global sudoku_map
global font_comic_sans

screen_width = 1200
screen_height = 800
grid_size = 9
fps = 30
update_render_step = 1
game_time = 0.0 # Time since start of the game

# Padding sudoku board on the main window screen in pixels
pad_left = 90
pad_right = 90
pad_top = 100
pad_bot = 100
pad_offset = 0
pad_3x3 = 6


class Button():
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def render(self, text_colour):
        mx, my = pygame.mouse.get_pos()
        if self.mouse_over(mx, my):
            pygame.draw.rect(screen, (30, 30, 30), (self.x, self.y, self.w, self.h), width=1)

        text_surf = font_comic_sans.render(self.text, False, text_colour)
        text_width, text_height = font_comic_sans.size(self.text)
        # Offset to middle
        text_offset_x = (self.w / 2) - (text_width/2)
        text_offset_y = (self.h / 2) - (text_height/2)
        screen.blit(text_surf, (self.x+text_offset_x, self.y+text_offset_y))

    def mouse_over(self, mx, my):
        if mx >= self.x and mx <= self.x + self.w and my >= self.y and my <= self.y + self.h:
            return True
        return False

    def update(self):
        pass

class QuitButton(Button):
    def __init__(self, text, x, y, w, h):
        super().__init__(text, x, y, w, h)

    def update(self):
        global running
        x, y = pygame.mouse.get_pos()
        if self.mouse_over(x, y) and pygame.mouse.get_pressed(5)[0]:
            running = False




def sudoku_render(clock, buttons):
    screen.fill((0, 0, 0))

    # Render all text/buttons
    for i in buttons:
        i.render((255, 255, 255))

    # Render fps text at (0, 0)
    text_surf = font_comic_sans.render("fps " + str(round(clock.get_fps())), False, (255, 255, 255))
    screen.blit(text_surf, (10, 5))



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
            text_colour = (0, 0, 0) if not preset else (255, 255, 255)

            if val != 0:
                text_surf = font_comic_sans.render(str(val), False, text_colour)
                text_width, text_height = font_comic_sans.size(str(val))
                # Text offset to middle of a tile
                text_offset_x = (width / 2) - (text_width/2)
                text_offset_y = (height / 2) - (text_height/2)
                screen.blit(text_surf, (xpos+text_offset_x, ypos+text_offset_y))

                # Draw green circle
                if not preset:
                    pygame.draw.rect(screen, (0, 255, 0), (xpos, ypos, width, height), width=1)

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

def sudoku_update(buttons):
    for i in buttons:
        i.update()

if __name__ == "__main__":
    pygame.font.init()

    screen = pygame.display.set_mode(size=(screen_width, screen_height), flags=0, depth=0, display=0)
    pygame.display.set_caption('Sudoku')
    running = True
    print("Starting game loop\n")

    sudoku_map = sudoku.sudoku_create(num_preset=5)
    font_comic_sans = pygame.font.SysFont('Comic Sans MS', 30)
    solve = 2

    clock = pygame.time.Clock()
    game_time = 0.0

    title_btn = Button("Sudoku", x=0, y=0, w=screen_width, h=screen_height/10)
    quit_btn = QuitButton("Quit game", x=screen_width-200, y=screen_height-85, w=180, h=80)
    buttons = [title_btn, quit_btn]

    while running:
        delta = clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event. type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        # Run the sudoku solver as long as solve == 2
        if solve == 2:
            solve = sudoku_solver.solve(sudoku_map, update_step=update_render_step)
            if solve == 1:
                print("Sudoku solved")
                print(sudoku_map)
            elif solve == 0:
                print("sudoku not solvable")

        sudoku_update(buttons)
        sudoku_render(clock, buttons)
        pygame.display.flip()

























#
