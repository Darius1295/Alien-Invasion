class Settings():
	# A Class to store all settings for Alien Invasion.

	def __init__(self):
		# Initialise the game's settings.
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# Ship settings
		self.ship_speed_factor = 3
		self.ship_limit = 1

		# Bullet settings
		self.bullet_speed_factor = 6
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3

		# Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Bomb settings
		self.bomb_speed_factor = 4
		self.bomb_width = 3
		self.bomb_height = 15
		self.bomb_color = (60,60,60)
		self.bomb_intensity = 0.0005

		# Barrier block settings
		self.block_width = 4
		self.block_height = 4

		# How quickly the game speeds up
		self.speedup_scale = 1.2

		self.bomb_scale = 2

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		# Initialise settings that change throughout the game.
		self.alien_speed_factor = 1
		self.bomb_intensity = 0.0002

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		# Increase speed settings.
		self.alien_speed_factor *= self.speedup_scale
		self.bomb_intensity *= self.bomb_scale