import pygame
import sudoku



global screen
global running



def sudoku_update(sudoku_map):
    pass



if __name__ == "__main__":
    screen = pygame.display.set_mode(size=(600, 400), flags=0, depth=0, display=0)
    pygame.display.set_caption('Sudoku')
    running = True
    print("Starting game loop\n")

    sudoku_map = sudoku.sudoku_create()
    print(sudoku_map[2][5])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event. type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #sudoku_update()


        pygame.display.update()

























#
