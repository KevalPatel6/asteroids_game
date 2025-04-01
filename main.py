import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
#Initialization
	pygame.init()
	#Starting Message
	print("Starting Asteroids!")
	print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
	
	dt = 0
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	pygame.display.set_caption("Asteroids")
	
	#Player Groups
	updateables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updateables, drawables)

	#Asteroid Groups
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updateables, drawables)

	#Asteroid Field Group
	AsteroidField.containers = (updateables)
	asteroid_field = AsteroidField()

	#Shot Group
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updateables, drawables)


	#Creating a Player object after Player containers are set so it is included.
	player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
	
#Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(pygame.Color(0,0,0))
		#iterate over updateables and update
		for img in updateables:
			img.update(dt)
		#iterate over drawables and draw
		for img in drawables:
			img.draw(screen)
		#iterate over all asteroids and update
		for asteroid in asteroids:
			if asteroid.check_collision(player):
				print("Game Over!")
				sys.exit()
			for shot in shots:
				if asteroid.check_collision(shot):
					shot.kill()
					asteroid.split()

		dt = clock.tick(60)/1000
		pygame.display.flip()

if __name__ == "__main__":
	main()

