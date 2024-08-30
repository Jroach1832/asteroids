import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000  
        
        screen.fill((0, 0, 0))  # Fill the screen with black before drawing the player
        player.draw(screen)
        player.update(dt)
            
        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()