import pygame
from pygame.locals import *
# here we put the game inside class to make it object oriented programming (oops)
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))  # size of window put inside "surface" variable
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
                        self.snake.move_up()    # calling the move up function we created

                    if event.key == K_DOWN:
                        self.snake.move_down()  # calling the move down function we created

                    if event.key == K_LEFT:
                        self.snake.move_left()   # calling the move left function we created

                    if event.key == K_RIGHT:
                        self.snake.move_right()  # calling the move right function we created

                elif event.type == QUIT:
                    running = False


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load(  "resources/block.jpg").convert()
        self.x = 100  # x axis of block stored in variable
        self.y = 100  # y axis of block stored in variable


    def draw(self):
        self.parent_screen.fill((50, 153, 168))             # making the surface we fill with colour a parent screen
        self.parent_screen.blit(self.block, (self.x, self.y))  # the block we made on surface to parent screen
        pygame.display.flip()                               # important function to call out the drawings

    def move_up(self):        # creating a move up func inside snake class so u can call it directly to move it
        self.y = self.y - 10  # reducing 10 pixels to move up
        self.draw()           # you have to call the .draw function everytime

    def move_down(self):      # creating a move down func inside snake class so u can call it directly to move it
        self.y = self.y + 10  # increasing 10 pixels to move down
        self.draw()           # you have to call the .draw function everytime

    def move_left(self):      # creating a move left func inside snake class so u can call it directly to move it
        self.x = self.x - 10  # reducing 10 pixels to move left
        self.draw()           # you have to call the .draw function everytime

    def move_right(self):     # creating a move right func inside snake class so u can call it directly to move it
        self.x = self.x + 10  # increasing 10 pixels to move right
        self.draw()           # you have to call the .draw function everytime


if __name__ == "__main__":
    game = Game()      # putting the Game class we made above in a variable
    game.run()         # calling the run function






















