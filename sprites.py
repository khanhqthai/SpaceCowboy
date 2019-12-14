import pygame

class SunSprite(pygame.sprite.Sprite):
	def __init__(self):
		super(SunSprite, self).__init__()
		#adding image to sprite array(python list)
		self.images = []
		self.images.append(pygame.image.load('img/sprite/Sun_00000.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00001.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00002.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00003.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00004.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00005.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00006.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00007.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00008.png'))
		self.images.append(pygame.image.load('img/sprite/Sun_00009.png'))
		self.direction = -600

		# array index starts at 0(first sprite frame)
		self.index = 0

		# set the image from array to be displayed to self.image(no to be confused with self.images which is a list)
		self.image = self.images[self.index]

		#creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
		self.rect = pygame.Rect(-200,-600,30,30)

	def update(self):
		# when update is called, it incrementals the index by 1.
		# it moves to the next frame in the sprite
		self.index+= 1

		# if the index is larger than length of the array(list) of images.
		if self.index >= len(self.images):
		# we set the index at 0, therefore restart the sprite to the first frame
		# starting our animation over again
			self.index = 0
		# last we update the image that will be displayed
		self.image = self.images[self.index]
		self.direction += 1
		self.rect = pygame.Rect(-200,self.direction, 0, 0)


class JetFighterSprite(pygame.sprite.Sprite):
	def __init__(self):
		super(JetFighterSprite, self).__init__()
		#adding image to sprite array(python list)
		self.images = []
		self.images.append(pygame.image.load('red_jetfighter.png'))

		# array index starts at 0(first sprite frame)
		self.index = 0

		# set the image from array to be displayed to self.image(no to be confused with self.images which is a list)
		self.image = self.images[self.index]

		#creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
		self.rect = pygame.Rect(0,0,35,38)

	def update(self):
		# when update is called, it incrementals the index by 1.
		# it moves to the next frame in the sprite
		self.index+= 1

		# if the index is larger than length of the array(list) of images.
		if self.index >= len(self.images):
		# we set the index at 0, therefore restart the sprite to the first frame
		# starting our animation over again
			self.index = 0
		# last we update the image that will be displayed
		self.image = self.images[self.index]


class JetBoosterSprite(pygame.sprite.Sprite):
	def __init__(self):
		super(JetBoosterSprite, self).__init__()
		#adding image to sprite array(python list)
		self.images = []
		self.images.append(pygame.image.load('booster_1.png'))
		self.images.append(pygame.image.load('booster_2.png'))

		# array index starts at 0(first sprite frame)
		self.index = 0

		# set the image from array to be displayed to self.image(no to be confused with self.images which is a list)
		self.image = self.images[self.index]

		#creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
		self.rect = pygame.Rect(0,0,6,7)

	def update(self):
		# when update is called, it incrementals the index by 1.
		# it moves to the next frame in the sprite
		self.index+= 1

		# if the index is larger than length of the array(list) of images.
		if self.index >= len(self.images):
		# we set the index at 0, therefore restart the sprite to the first frame
		# starting our animation over again
			self.index = 0
		# last we update the image that will be displayed
		self.image = self.images[self.index]

class JetFighter:

	def __init__(self,x,y):
		self.jet_fighter = JetFighterSprite()
		self.jet_booster_right_sprite = JetBoosterSprite()
		self.jet_booster_left_sprite = JetBoosterSprite()
		self.sprite_group = pygame.sprite.Group([self.jet_fighter,self.jet_booster_right_sprite, self.jet_booster_left_sprite])
		self.jet_fighter.rect.move_ip(x,y)
		self.jet_booster_right_sprite.rect.move_ip(x+20,y+35)
		self.jet_booster_left_sprite.rect.move_ip(x+10,y+35)

	
	def update(self):
		self.sprite_group.update()
	
	def draw(self,screen):
		self.sprite_group.draw(screen)

	def move(self,x,y):
		self.jet_fighter.rect.move_ip(x,y)
		self.jet_booster_right_sprite.rect.move_ip(x+20,y+35)
		self.jet_booster_left_sprite.rect.move_ip(x+10,y+35)