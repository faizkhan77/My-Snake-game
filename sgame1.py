import pygame
from pygame.locals import *

# making the window and the block

def draw_block():                # this draw_block function
    surface.fill((50, 153, 168))       # coloring background again everytime block is made5+
    # so the previous block get erased
    surface.blit(block, (block_x, block_y))      # drawing the block above the surface
    pygame.display.flip()            # important function to call out the drawings


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))   # size of window put inside "surface" variable
    surface.fill((50, 153, 168))   # coloring the background of game with rgb code

    block = pygame.image.load("resources/block.jpg").convert()   # importing image of the block and put inside "block" variable
    block_x = 100      # x axis of block stored in variable
    block_y = 100      # y axis of block stored in variable
    surface.blit(block, (block_x, block_y))  # drawing the block above the surface with .blit() functiom

    pygame.display.flip()  # important function to call out the drawings

running = True

while running:
    for event in pygame.event.get():      # from pygame.local
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:       # if ESCAPE key is pressed, the loop should stop
                running = False

            if event.key == K_UP:
                block_y = block_y - 10
                draw_block()        # when u do any changes to drawing always call this draw_block() function
            if event.key == K_DOWN:
                block_y = block_y + 10
                draw_block()
            if event.key == K_LEFT:
                block_x = block_x - 10
                draw_block()
            if event.key == K_RIGHT:
                block_x = block_x + 10
                draw_block()

        elif event.type == QUIT:
            running = False








