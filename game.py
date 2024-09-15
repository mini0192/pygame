import pygame
import sys

pygame.init()
pygame.display.set_caption("걷는 고양이")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 400))
font = pygame.font.Font(None, 50)

img_char : tuple = (
    "./character/1.png",
    "./character/2.png",
    "./character/3.png",
    "./character/4.png",
    "./character/5.png",
    "./character/6.png",
    "./character/7.png",
    "./character/8.png",
    "./character/9.png",
    "./character/10.png",
    "./character/11.png",
    "./character/12.png",
)

img_bg : tuple = (
    "./background/bg.jpg",
)

state : bool = False

character = pygame.image.load(img_char[0])
character_ext = character.get_rect()[2:4]
character_size : float = 0.6

background = pygame.image.load(img_bg[0])
background_ext = character.get_rect()[2:4]
background_size : float = 3.5
background_position : int = -100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move = 0
                state = True
                print("do")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                state = False

    background = pygame.transform.scale(background, (int(background_ext[0] * background_size), int(background_ext[1] * background_size)))

    if state == True:
        move += 1
        index : int = int((move / 10) % 12)

        if move % 5 == 0:
            background_position += 1
            if(background_position > 0):
                background_position = -100

        character = pygame.image.load(img_char[index])
        character = pygame.transform.scale(character, (int(character_ext[0] * character_size), int(character_ext[1] * character_size)))
    else:
        character = pygame.image.load(img_char[0])
        character = pygame.transform.scale(character, (int(character_ext[0] * character_size), int(character_ext[1] * character_size)))

    screen.blit(background, [background_position, 0])
    screen.blit(character, [300, 250])

    pygame.display.update()
    
    clock.tick(100)