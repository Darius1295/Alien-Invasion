import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	# A class to represent a single alien in the fleet.

	def __init__(self, ai_settings, screen):
		# Initialise the alien and set its starting postion.
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load('/Users/Darius/Documents/python_work/alien_invasion/images/alien2.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store th alien's exact postion.
		self.x = float(self.rect.x)

	def blitme(self):
		# Draw the alien at its current location.
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		# Return true if alien is at edge of screen.
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True 
		elif self.rect.left <= 0:
			return True

	def update(self):
		# Move the alien to the right.
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x







