import pygame

class Block(Sprite):
	# A class to manage the barriers.

	def __init__(self, ai_settings, screen, ship):
		# Create block for barrier.
		super(Block, self).__init__()
		self.screen = screen

		# Create block rect at (0, 0) then set its position.
		self.rect = pygame.Rect(0, 0, ai_settings.block_height, ai_settings.block_width)

		self.screen_rect = screen.get_rect()
		self.rect.x = self.rect.width 
		self.rect.y = self.screen_rect.bottom - 2 * 