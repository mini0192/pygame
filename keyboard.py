import pygame

pygame.init()

background: pygame.surface.Surface = pygame.display.set_mode((400, 360))

pygame.display.set_caption("SONOL")

play: bool = True

fps: pygame.time.Clock = pygame.time.Clock()

x_pos: int = background.get_size()[0]//2
y_pos: int = background.get_size()[1]//2

to_x: int = 0
to_y: int = 0

BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)

while(play):
    deltaTime: int = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -1

            elif event.key == pygame.K_DOWN:
                to_y = 1

            elif event.key == pygame.K_RIGHT:
                to_x = 1

            elif event.key == pygame.K_LEFT:
                to_x = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = 0

            elif event.key == pygame.K_DOWN:
                to_y = 0

            elif event.key == pygame.K_RIGHT:
                to_x = 0

            elif event.key == pygame.K_LEFT:
                to_x = 0

    x_pos += to_x
    y_pos += to_y

    background.fill(BLACK)
    pygame.draw.circle(background, WHITE, (x_pos, y_pos), 5)
    pygame.display.update()

pygame.quit()