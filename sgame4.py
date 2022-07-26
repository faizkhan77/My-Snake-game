import pygame
from pygame.locals import *
import time
# making the actual block into snakes and making the apple

size = 40          # size of block is 40 so we put 40 too as pixels in a variable called "size"

class Apple:
    def __init__(self, parent_screen):           # creating an Apple class to make the apple
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()  # getting apple image in putting it inside "image" variable
        self.x = size*3           # placing it in x and y axis
        self.y = size*3           # multiplying it with size which is 40, so 40*3 is 120, means x and y axis at 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))          # to draw apple above parent screen
        pygame.display.flip()             # flip is important function

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()

        self.length = length
        self.x = [size]*length  # x axis, multiplying it by length(2) means making 2 extra block
        self.y = [size]*length  # y axis, multiplying it by length(2) means making 2 extra block
        self.direction = "down"

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

    def draw(self):
        self.parent_screen.fill((50, 153, 168))             # making the surface we fill with colour a parent screen
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))  # drawing all the behind blocks "i"

        pygame.display.flip()                               # important function to call out the drawings

    def walk(self):      # to check and make block change diredtion
        for i in range(self.length-1,0,-1):     # using self.length from snake class to make rest of block behind move
            self.x[i] = self.x[i-1]         # replacing previous blocks with next one
            self.y[i] = self.y[i-1]

        if self.direction == "up":      # changing direction with if and elif statements
            self.y[0] -= size    # increasing and decreasing 10 pixels according to direction
        elif self.direction == "down":
            self.y[0] += size            # self.y[0]  means we are telling the first block to move cuz 0 is the first index in array
        elif self.direction == "left":
            self.x[0] -= size             # 40 cuz the block image size is 40, so we move it per 40 pixels
        elif self.direction == "right":
            self.x[0] += size
        self.draw()      # to call the functions



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 700))  # size of window put inside "surface" variable
        self.snake = Snake(self.surface, 6)   # the snake class as an object and joining it to the Game class & passing "surface" to surface
                                         # passing 2 value to "length"
        self.snake.draw()                # calling the draw function inside the "Snake" class
        self.apple = Apple(self.surface)       # putting apple class here and passing "surface" as parent screen
        self.apple.draw()                      # calling the draw function inside the "Apple" class

    def play(self):   # putting both these inside a function so we can easily call both later
        self.snake.walk()  # using walk function from snake class to move the blocks
        self.apple.draw()  # using draw function from apple class to call the drawing


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():  # from pygame.local
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # if ESCAPE key is pressed, the loop should stop
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()   # calling the move up function we created to change direction

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False


            self.play()            # calling play function we created above in game class
            time.sleep(0.2)        # to stop the loop every 0.2 sec and make the block move by its own
                                   # u can increase block speed from here too


if __name__ == "__main__":
    game = Game()      # putting the Game class we made above in a variable
    game.run()         # calling the run function






















