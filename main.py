import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000  
        
        screen.fill((0, 0, 0))  # Fill the screen with black before drawing the player
        
        #player.draw(screen)
        for dsprite in drawable:
            dsprite.draw(screen)

        #player.update(dt)
        for usprite in updatable:
            usprite.update(dt)

        for asprite in asteroids:
            for shot in shots:
                if asprite.check_collision(shot):
                    asprite.split() #asprite.kill()
                    shot.kill()

        for asprite in asteroids:
            if asprite.check_collision(player):
                print("Game over!")
                exit()
            
        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()