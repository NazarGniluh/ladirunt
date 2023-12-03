import pygame
import  Character
import Enemy

pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()


fon = pygame.image.load('background.jpg')
fon = pygame.transform.scale(fon, (800, 500))

pacman = Character.Character(250, 350, 30, 20, 5, "hero.png" )
pacman2 = Enemy.Enemy(350, 370, 30, 20, 5, "cyborg.png", 200, 300, 300, 300)
game = True
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    pacman.move()
    pacman2.move()

    window.fill((255,205,0))
    window.blit(fon, (0, 0))


    pacman2.render(window)
    pacman.render(window)
    pacman2.render(window)
    pygame.display.flip()
    fps.tick(60)