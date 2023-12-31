import pygame
import      Character
import Enemy
import  Golden
from Stinks import Stinks
pygame.init()


pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)


pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()


fon = pygame.image.load('background.jpg')
fon = pygame.transform.scale(fon, (800, 500))

pacman = Character.Character(400, 400, 30, 20, 5, "hero.png" )
pacman2 = Enemy.Enemy(250, 350, 30, 20, 5, "cyborg.png", 100, 200, 300, 300)
gold = Golden.Golden(220, 365, 50, 50,  "treasure.png")


game = True

Stin = []

Stin.append(Stinks(0, 268, 50, 10, (255, 255, 0)))
Stin.append(Stinks(0, 317, 50, 10, (255, 255, 0)))
Stin.append(Stinks(50, 268, 50, 10, (255, 255, 0)))
Stin.append(Stinks(50, 317, 50, 10, (255, 255, 0)))
Stin.append(Stinks(100, 268, 60, 10, (255, 255, 0)))
Stin.append(Stinks(90, 325, 10, 100, (255, 255, 0)))
Stin.append(Stinks(100, 415, 150, 10, (255, 255, 0)))
Stin.append(Stinks(90, 325, 10, 100, (255, 255, 0)))
Stin.append(Stinks(90, 325, 10, 100, (255, 255, 0)))
Stin.append(Stinks(90, 325, 10, 100, (255, 255, 0)))
Stin.append(Stinks(156, 178, 10, 100, (255, 255, 0)))
Stin.append(Stinks(250, 415, 40, 10, (255, 255, 0)))
Stin.append(Stinks(290, 365, 10, 60, (255, 255, 0)))
Stin.append(Stinks(150, 318, 10, 59, (255, 255, 0)))
Stin.append(Stinks(157, 367, 135, 10, (255, 255, 0)))




game = True

money_sould = pygame.mixer.Sound("money.ogg")
money_sould.play()
while game:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    pacman.move()
    pacman2.move()

    for Stinks in Stin:
        if pacman.hit_box.colliderect(Stinks.rect):
            game = False


    if gold.hit_box.colliderect(pacman.hit_box):
        money_sould.play()
        gold.hit_box.x = 1000000

    window.fill((255,205,0))
    window.blit(fon, (0, 0))


    pacman2.render(window)
    pacman.render(window)

    gold.render(window)
    for Stinks in Stin:
        Stinks.render(window)
    pygame.display.flip()
    fps.tick(60)