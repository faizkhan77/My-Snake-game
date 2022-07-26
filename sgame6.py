
# making the game more functional by adding enter key,pause,losing when snake hit itself and game resetting when u lose

import pygame
from pygame.locals import *
import time
import random      # to move apple at random spot


size = 40          # size of block is 40 so we put 40 too as pixels in a variable called "size"
BACKGROUND_COLOR = (50, 153, 168)

class Apple:
    def __init__(self, parent_screen):           # creating an Apple class to make the apple
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()  # getting apple image in putting it inside "image" variable
        self.x = size*3           # placing it in x and y axis
        self.y = size*3           # multiplying it with size which is 40, so 40*3 is 120, means x and y axis at 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))          # to draw apple above parent screen
        pygame.display.flip()             # flip is important function


    def move(self):  # a function to move the apple at a random place
        self.x = random.randint(1, 24)*size  # to put apple at random spot between 1 to 25, cus our window x, width is 1000 and our apple...
        self.y = random.randint(1, 19)*size  # size is 40 so 1000 devide 40 is 25, means we have 25 square blocks spaces to move our apple
                                             # we do the same with y but minus it with the height we given
                                             # random.randint(-,-) function is used to give random nums between two given nums


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()    # block image
        self.length = length
        self.x = [size]*length  # x axis, multiplying it by length(2) means making 2 extra block
        self.y = [size]*length  # y axis, multiplying it by length(2) means making 2 extra block
        self.direction = "down"

    def increase_length(self):
        self.length += 1        # making function for increasing snake length by 1 block
        self.x.append(-1)       # when length is increased it means new block appear so u have to make x and y axis too
        self.y.append(-1)


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

    def draw(self):
        self.parent_screen.fill((BACKGROUND_COLOR))             # making the surface we fill with colour a parent screen
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))  # drawing all the behind blocks "i"

        pygame.display.flip()                               # important function to call out the drawings



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))  # size of window put inside "surface" variable
        self.snake = Snake(self.surface, 1)   # the snake class as an object and joining it to the Game class & passing "surface" to surface
                                         # passing 2 value to "length"
        self.snake.draw()                # calling the draw function inside the "Snake" class
        self.apple = Apple(self.surface)       # putting apple class here and passing "surface" as parent screen
        self.apple.draw()                      # calling the draw function inside the "Apple" class


    def is_collision(self, x1, y1, x2, y2):         # making function to collide snake head to apple
        if x1 >= x2 and x1 < x2 + size:             # idk wtf is this but its checking if both object..-
            if y1 >= y2 and y1 < y2 + size:         # is colliding (snake n apple)
                return True                         # if it collides than return True
        return False                                 # otherwise return False


    def reset(self):    # to reset game after u lose it
        self.snake = Snake(self.surface, 1)         # snake size and apple will reset to
        self.apple = Apple(self.surface)

    def play(self):   # putting both these inside a function so we can easily call both later
        self.snake.walk()  # using walk function from snake class to move the blocks
        self.apple.draw()  # using draw function from apple class to call the drawing
        self.display_score()     # calling display score function
        pygame.display.flip()    # u need to call .flip() func whenever u paint something in this case the score


        # idk tf is this but its for snake colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):  # collide with only head of snake
                # print("collision!!!!.....")               # printing collision everytime each block collide with the apple
                self.snake.increase_length()           # increase length (blocks) everytime it collides with the apple
                self.apple.move()

        # snake colliding with itself
        for i in range(2,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"           # snake head             # snake body


    def display_score(self):  # to display score
        font = pygame.font.SysFont('arial', 30)  # creating the font which is 'arial' and size is '30'
        score = font.render(f"score: {self.snake.length}", True, (255, 255, 255))
                                # score is snake length        #this is font rgb color
        self.surface.blit(score, (850, 10))  # whenevr u wanna paint smth over surface use ,blit
        # this is x and y axis position to draw the score in

    def show_game_over(self):
        font = pygame.font.SysFont('arial', 30)
        self.surface.fill(BACKGROUND_COLOR)      # coloring background again once game over
        line1 = font.render(f"Game is over! Your score is: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))    # printing game over text on 200 and 300 x and y axis
        line2 = font.render(f"To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))   # .blit is used to draw something over the surface in this case the texts

        pygame.display.flip()           # imp func to see the updated things we did

    def run(self):
        running = True
        pause = True

        while running:
            for event in pygame.event.get():  # from pygame.local
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # if ESCAPE key is pressed, the loop should stop
                        running = False
                    if event.key == K_RETURN:
                        pause = False                # if we lick enter the game should start n not pause
                    if not pause:                    # if its not pause then all these key should work
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

            try:
                if not pause:              # means if pause is not true then we want to play the game
                    self.play()            # calling play function we created to play the game
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.2)        # to stop the loop every 0.2 sec and make the block move by its own
                                   # u can increase block speed from here too


if __name__ == "__main__":
    game = Game()      # putting the Game class we made above in a variable
    game.run()         # calling the run function






















