import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
	# A class to manage bombs dropped by aliens.

	def __init__(self, ai_settings, screen, alien):
		# Create bomb object at an alien's current position.
		super(Bomb, self).__init__()
		self.screen = screen

		# Create bomb rect at (0, 0) then set to correct postion.
		self.rect = pygame.Rect(0, 0, ai_settings.bomb_width, ai_settings.bomb_height)
		self.rect.centerx = alien.rect.centerx
		self.rect.bottom = alien.rect.bottom

		# Store the bomb's position as an integer value.
		self.y = float(self.rect.y)

		self.color = ai_settings.bomb_color
		self.speed_factor = ai_settings.bomb_speed_factor

	def update(self):
		# Move the bomb down the screen.
		# Update the decimal position of the bomb.
		self.y += self.speed_factor
		# Update the rect position.
		self.rect.y = self.y

	def draw_bomb(self):
		# Draw bomb to the screen.
		pygame.draw.rect(self.screen, self.color, self.rect)
