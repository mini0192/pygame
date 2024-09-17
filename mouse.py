import pygame
import random

pygame.init()

background_size: tuple = (400, 300)
background: pygame.surface.Surface = pygame.display.set_mode(background_size)

game_font: pygame.font.Font = pygame.font.SysFont(None, 30)
fps: pygame.time.Clock = pygame.time.Clock()

color: dict = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0)
}

score: dict = {
    "score": 0,
    "socre_pos": (10, 10),

    "win_score": 800,
    "level_score": 100,
    "score_up": 10,
    "speed_up": 10
}

count: dict = {
    "count" : 0,
    "count_time": 100
}

class Target:
    def __init__(self, x_pos: int, y_pos: int):
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.target_size: int = 20

    def getPos(self) -> tuple:
        return (self.x_pos, self.y_pos)
    
    def getSize(self) -> int:
        return self.target_size
    
tar: Target = Target(-5, -5)

is_win: bool = False
play: bool = True
pause: bool = False

while play:
    count["count"] += 1

    if count["count"] % count["count_time"] == 0:
        if not pause and not is_win:
            tar = Target(random.randrange(10, 390), random.randrange(10, 290))
    
    fps.tick(60)
    background.fill(color["BLACK"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mos: tuple = pygame.mouse.get_pos()

            if(not(mos[0] >= tar.getPos()[0] - tar.getSize() and mos[0] <= tar.getPos()[0] + tar.getSize())):
                continue

            if(not(mos[1] >= tar.getPos()[1] - tar.getSize() and mos[1] <= tar.getPos()[1] + tar.getSize())):
                continue
            
            if not pause:
                score["score"] += score["score_up"]
                if score["score"] >= score["win_score"]:
                    is_win = True

                if score["score"] % score["level_score"] == 0:
                    count["count_time"] -= score["speed_up"]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = not pause

    if is_win:
        score_text: pygame.surface.Surface = game_font.render("You Win", True, color["WHITE"])
    
    elif pause:
        score_text: pygame.surface.Surface = game_font.render("Pause", True, color["WHITE"])

    else:
        score_text: pygame.surface.Surface = game_font.render("Score: " + str(score["score"]), True, color["WHITE"])

    background.blit(score_text, score["socre_pos"])

    if not pause and not is_win:
        pygame.draw.circle(background, color["WHITE"], tar.getPos(), 10)
    pygame.display.update()

pygame.quit()