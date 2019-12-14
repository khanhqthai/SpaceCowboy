"""
    Class Stars Object
    Animating stars, that slowly falls

"""
import pygame
import random

class Stars:
    def __init__(self,numbers,size, display_width, display_height,color, speed, gameDisplay):
        self.numbers = numbers
        self.display_width = display_width
        self.display_height = display_height
        self.color = color
        self.gameDisplay = gameDisplay
        self.stars_list = []
        self.speed = speed
        self.size = size

        # Loop "numbers" of times and add a stars  in a random x,y position
        for i in range(self.numbers):
            x = random.randrange(0, display_width)
            y = random.randrange(0, display_height)
            self.stars_list.append([x,y])

    # draws star and move stars doww(default direction)
    def draw(self):
        # loop each star in the list   
        for i in range(len(self.stars_list)):

            if i%2==0:
                color = (255, 255, 224)
            else:
                color = self.color
            # draw the star
            pygame.draw.circle(self.gameDisplay, color, self.stars_list[i], self.size)
            # Move the star down one pixel
            # add different direction later
            self.stars_list[i][1] += self.speed

            # If star has reached the bottom of the screen
            if self.stars_list[i][1] > self.display_height:
                # move it back to  the top
                y = random.randrange(-50, -10)
                self.stars_list[i][1] = y
                # but give it a new x
                #we dont want it to come down the same spot again
                x = random.randrange(0, self.display_width)
                self.stars_list[i][0] = x