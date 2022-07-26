import pygame
from pygame.locals import *
import time
# making the block\snake move by its own and we only change the direction



class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100  # x axis of block stored in variable
        self.y = 100  # y axis of block stored in variable
        self.direction = "up"

    def draw(self):
        self.parent_screen.fill((50, 153, 168))             # making the surface we fill with colour a parent screen
        self.parent_screen.blit(self.block, (self.x, self.y))  # the block we made on surface to parent screen
        pygame.display.flip()                               # important function to call out the drawings

# MOVEMENTS FUNCTIONS -------------------------------------------------------
    def move_up(self):
        self.direction = "up"   # changing direction to up

    def move_down(self):
        self.direction = "down"      # changing direction to down

    def move_left(self):
        self.direction = "left"   # changing direction to left

    def move_right(self):
        self.direction = "right"    # changing direction to right
# ______________________________________________________________________________

    def walk(self):      # to check and make block change diredtion
        if self.direction == "up":      # changing direction with if and elif statements
            self.y -= 10    # increasing and decreasing 10 pixels according to direction
        elif self.direction == "down":
            self.y += 10
        elif self.direction == "left":
            self.x -= 10
        elif self.direction == "right":
            self.x += 10
        self.draw()      # to call the functions


# here we put the game inside class to make it object oriented programming (oops)
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))  # size of window put inside "surface" variable
        self.snake = Snake(self.surface)   # the snake class as an object and joining it to the Game class & passing "surface" to parentscreen
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():  # from pygame.local
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # if ESCAPE key is pressed, the loop should stop
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()   # calling the move up function we created

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False
            self.snake.walk()     # using walk function from snake class
            time.sleep(0.05)        # to stop the loop every 0.2 sec and make the block move by its own
                                   # u can increase block speed from here too


if __name__ == "__main__":
    game = Game()      # putting the Game class we made above in a variable
    game.run()         # calling the run function






















