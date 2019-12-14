# import pygame package
import pygame
import time
import random
from GIFImage import GIFImage
from Stars import Stars
from settings import *
import PAdLib.particles as particles
from sprites import SunSprite
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
# initialize pygame
pygame.init()

#explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
pygame.mixer.music.load("music/alina_baraz_to_me.mp3")

pause = False

# create and set window/screen display
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('Space Cowboy')

# start clock, we will use this to count frames(fps)
clock = pygame.time.Clock()

# load our car image(player)
jetImg = pygame.image.load('img/red_jetfighter.png')
# car image width. we will use it to calculate collisions with other objects
car_width = 35;
thicQueenImg = pygame.image.load('img/thic_queen.jpg').convert()
thicQueenImg.set_alpha(0)
galaxyImg = pygame.image.load('img/galaxy.png')
pygame.display.set_icon(jetImg)

gifImgToMe = GIFImage("img/to_me.gif")
#gifImgFoundLove = GIFImage("img/found_lil_love.gif")


# gif_grid = []
# for num in range(9):
# 	gif_grid.append(gifImgToMe.copy())
# 	gif_grid[num].scale(-0.334)

# create star falling object 
stars_list = []
stars_list.append(Stars(100, 1, DISPLAY_WIDTH,DISPLAY_HEIGHT, white,1,gameDisplay))
stars_list.append(Stars(30, 2, DISPLAY_WIDTH,DISPLAY_HEIGHT, white,2,gameDisplay))
stars_list.append(Stars(10, 3, DISPLAY_WIDTH,DISPLAY_HEIGHT, white,2,gameDisplay))

sun_sprite = SunSprite()
sprite_group = pygame.sprite.Group(sun_sprite)

def display_score(count):
	font = pygame.font.Font('freesansbold.ttf', 25)
	text = font.render(f"Score: {count}", True, white)
	gameDisplay.blit(text,(0,DISPLAY_HEIGHT-25))

def display_time(seconds):
	font = pygame.font.Font('freesansbold.ttf', 14)
	text = font.render(f"time: {seconds}", True, dark_yellow )
	gameDisplay.blit(text,(0,DISPLAY_HEIGHT-50))

def scrolling_text(text,x,y):
	font = pygame.font.Font('freesansbold.ttf', 20)
	text = font.render(f"{text}", True, dark_yellow )
	gameDisplay.blit(text,(0,DISPLAY_HEIGHT-50))


class Things:
	'''
		Creates Thing objects.
		These will be the obstacles player will evade/dodge
	'''
	def __init__(self, gameDisplay, thingx, thingy, thingw, thingh, color):
		self.thingx = thingx
		self.thingy = thingy
		self.thingw = thingw
		self.thingh = thingh
		self.color = color
		self.gameDisplay = gameDisplay
		#pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

	def draw(self, thing_starty):
		self.thingy = thing_starty
		pygame.draw.rect(self.gameDisplay, self.color, [self.thingx, self.thingy, self.thingw, self.thingh])

	def set_random_x(self):
		self.thingx = random.randrange(0,DISPLAY_WIDTH)

class ThingPolygon:
	def __init__(self, gameDisplay, color, point_list):
		self.gameDisplay = gameDisplay
		self.color = color
		pygame.draw.polygon(gameDisplay, color, point_list)

	def draw(self, point_list):
		pygame.draw.polygon(self.gameDisplay, self.color, point_list)

#our jet function loads jet fighter image at x,y cordinates
def jet(x,y):
	gameDisplay.blit(jetImg, (x,y) )

def display_img(image, x,y):
	gameDisplay.blit(image,(x,y))

def text_objects(text, font):
	TextSurface = font.render(text,True, black)
	return TextSurface, TextSurface.get_rect()


# function to display text to the screen
def message_display(text):

	# set font and size to use
	largeText = pygame.font.Font('freesansbold.ttf', 115)

	TextSurface, TextRect = text_objects(text, largeText)

	# center our text
	TextRect.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)
	
	gameDisplay.blit(TextSurface,TextRect)
	
	# display all changes to screen
	pygame.display.update()

	time.sleep(2)

	game_loop()


#Our crash function, handles what is the next step when a player crashes the car.
#1. We want ask if the player wants to quit
#2. We want to ask if the player wants to continue and try again
def crash():
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(explosion_sound)

	message_display('You Crashed')

def button(startx,starty,width,height,active_color, inactive_color, title, action=None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if startx + width > mouse[0] > startx and starty + height > mouse[1] > starty:
			pygame.draw.rect(gameDisplay, active_color,(startx,starty,width,height))
			if click[0] == 1:
				action()

		else:
			pygame.draw.rect(gameDisplay, inactive_color,(startx,starty,width,height))

		smallText = pygame.font.Font("freesansbold.ttf", 20)
		textSurf, textRect = text_objects(title, smallText)
		textRect.center = ((startx+(width/2)), (starty+(height/2)) )
		gameDisplay.blit(textSurf, textRect)
		clock.tick(15)


def quit_game():
	# this will quit pygame
	pygame.quit()
	# this will  quit python
	quit()


def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',60)
		TextSurf, TextRect = text_objects("Jet Fighter", largeText)
		TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
		gameDisplay.blit(TextSurf, TextRect)

		green_button = button(150, 400, 100, 50, bright_green, green, "START", game_loop)
		red_button = button(390, 400, 100, 50, bright_red, red, "QUIT", quit_game)

		pygame.display.update()
		clock.tick(15)

def game_unpause():
	global pause
	pause = False
	pygame.mixer.music.unpause()

def game_pause():
	pygame.mixer.music.pause()

	gameDisplay.fill(white)
	largeText = pygame.font.Font('freesansbold.ttf',60)
	TextSurf, TextRect = text_objects("Paused", largeText)
	TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
	gameDisplay.blit(TextSurf, TextRect)

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()



		green_button = button(150, 400, 100, 50, bright_green, green, "Continue", game_unpause)
		red_button = button(390, 400, 100, 50, bright_red, red, "QUIT", quit_game)

		pygame.display.update()
		clock.tick(15)



#our main game loop logic
def game_loop():
	i=1
	global pause
	pygame.mixer.music.play(1)
	# start tick, we use this calculate our timer
	start_ticks=pygame.time.get_ticks()
	seconds=0

	# cordinates where we want our car to initially loaded on the screen
	# which is towards the bottom and in the middle
	x = (DISPLAY_WIDTH * 0.45)
	y = (DISPLAY_HEIGHT * 0.90)

	# change in x and y for our car
	x_change = 0
	car_speed = 0
	
	# characteristics of our initial thing drawn objects
	thing_startx = 0
	thing_starty = 0
	thing_speed = 7
	thing_width = 50
	thing_height = 50
	# charateristic of diamond polygon object
	# diamond_point_list=[(20,20),(30,0),(40,20),(30,30)]

	# create our list of thing objets
	things_list = []
	for item in range(0):
		things_list.append(Things(gameDisplay, thing_startx, thing_starty, thing_width, thing_height, block_color))
		# start each object at random x cordinates
		things_list[item].set_random_x()

	# create our diamon thing object
	# diamon_polygon = ThingPolygon(gameDisplay, block_color, diamond_point_list)

	# initial score counter = 0
	dodged = 0
	
	# condition for our game to end
	gameExit = False

	# reset our gif, to it start from the beggining.
	# for gif in gif_grid:
	# 	gif.reset()
	# 	gif.play()


	counter = 255
	while not gameExit:
		seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
		
		# pygame  has event functions that gets all the event in the game, e.i. mouse clicks, buttons click
		for event in pygame.event.get():
			
			# if event is QUIT(), aka, player click "X" on window
			if event.type == pygame.QUIT:
				quit_game()

			
			# if key is pressed, add or minus change in x
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					quit_game()
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_p:
					pause = True
					game_pause()

			# if key is released, set x_change back to 0. we want our race car to stop moving when the key is released
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				
		# update change in x per left or right button events
		x+=x_change	
		
		# set the backgrond color of our display(screen)
		gameDisplay.fill(black)
		seconds2 = seconds - 10
		
		if seconds > 10	 and seconds < 35:
			thicQueenImg.set_alpha(seconds2*6)
		
		if seconds >=35 and seconds <=36:
			thicQueenImg.set_alpha(255)
			seconds2 = 255
		
		if seconds > 30:
			counter = counter -1
			thicQueenImg.set_alpha(counter)
		
		display_img(thicQueenImg, 0,0)
		
		if seconds > 25:
			sprite_group.update()
			sprite_group.draw(gameDisplay)

		#scrolling_text("Alina Baraz",DISPLAY_WIDTH/2,DISPLAY_HEIGHT/2)
		if seconds > 0 and seconds < 10:
			gifImgToMe.render(gameDisplay,(80,105))
		if seconds > 3 and seconds < 10:
			gifImgToMe.pause()


		
		for star in stars_list:
			star.draw()

		for thing in things_list:
			thing.draw(thing_starty)
			# we check if the thing object we moved is off the screen, if it is then we start back at the top again.
			# also want randomize the x cordinate too, because we don't want it to come down from the same spot
			if thing.thingy > DISPLAY_HEIGHT:
				thing_starty = 0 - thing_height
				thing.set_random_x()
				dodged += 1


			# collision check 2: car cannot touch thing object
			# if car touch thing object, consider it a crashed
			if y < thing.thingy + thing.thingh:
				if x > thing.thingx and x < thing.thingx + thing.thingw or x + car_width > thing.thingx and x + car_width < thing.thingx +thing.thingw:
					crash()
					

		# now we move the thing object down, we do this by changing the thing object y cordinate
		thing_starty += 1

		
		# call our jet function, to move jet to x,y cordinates
		jet(x,y)


		# display our score(aka how many obstacle dodged)
		#display_score(dodged)
		#display_time(seconds)

		# collision check 1: car can not touch the sides of our display.
		# if car x cordinate is greater than the display setting or less 0.
		# We will considered a crash and have player restart
		if x > DISPLAY_WIDTH-car_width or x<0:
			crash()

		# update, and display on screen
		pygame.display.update()
		
		# we move the frame forward, setting 30 or 60, will gives use 30 fps or 60fps and so on.
		clock.tick(60)


#game_intro()
# run our game 
game_loop()

# quit game
quit_game()