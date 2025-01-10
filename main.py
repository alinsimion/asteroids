
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

import pygame

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    p = Player(x, y)
    asf = AsteroidField()

    while 1:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            did = obj.did_collide(p)
            # print(did)
            if did:
                print("Game over!")
                exit(1)
        
        for obj in asteroids:
            print(shots)
            for obj2 in shots:    
                did = obj.did_collide(obj2)
                print(did)
                if did:
                    obj.split()
                    obj2.kill()
    
        pygame.display.flip()
        
        r_time = clock.tick(60)
        
        dt = r_time/1000

        
        

if __name__ == "__main__":
    main()