import pygame
from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(pygame.Color(0,0,0))
		pygame.display.flip()
	print("Starting Asteroids!")
	print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
if __name__ == "__main__":
	main()

