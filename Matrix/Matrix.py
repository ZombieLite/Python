import pygame
from random import choice, randrange, randint

ALL = WIDTH, HEIGHT = 900,400
FONT_SIZE = 20
FPS = 30
NUM = 15

pygame.init()

box = pygame.display.set_mode(ALL)
pygame.display.set_caption("Matrix")
fps = pygame.time.Clock()


class PreChars:
    def __init__(self):
        self.char = [chr(int('0x30a0', 16) + i) for i in range(1, 91)]
        self.font = pygame.font.Font('Font/MS Mincho.ttf', FONT_SIZE, bold=True)

    def Random(self, brg):
        b = int(brg)
        b = 255 if b > 250 else b

        return [self.font.render(char, True, pygame.Color(randint(0, (b // 100 * 25)), randrange(140, 255), randint(0, (b // 100 * 25)))) for char in self.char]

    def FirstSimbol(self):
        return [self.font.render(char, True, pygame.Color(144, 255, 144)) for char in self.char]

class Symbol:
    def __init__(self, x, y, speed, char, mode):
        self.x, self.y, self.speed, self.char, self.mode = x, y, speed, char, mode
        self.value = choice(self.char)
        self.interval = randrange(5, 10)


    def draw(self):
        if not pygame.time.get_ticks() % self.interval:
            self.value = choice(self.char)

        self.y = self.y + self.speed  if self.y < HEIGHT else -FONT_SIZE

        if self.mode != 1:
            #surf_alpha = pygame.Surface((FONT_SIZE, FONT_SIZE))
            #surf_alpha.fill(pygame.Color('red'))
            #pygame.draw.rect(surf_alpha, (255, 0, 0), (2, 2, 2, 100))
            #surf_alpha.set_alpha(28)

            #self.value.blit(surf_alpha, (self.x, self.y))
            #box.blit(self.value, (self.x, self.y))
            box.blit(self.value, (self.x, self.y))
        else:
            box.blit(self.value, (self.x, self.y))

class Column:
    def __init__(self, x, y):
        p = PreChars()
        self.x, self.y = x, y
        self.column_num = NUM
        self.column_speed = randrange(3, 10)
        self.column = [Symbol(self.x, i, self.column_speed, p.FirstSimbol(), 1) if((self.y + FONT_SIZE) * self.column_num - FONT_SIZE <= i <= (self.y + FONT_SIZE) * self.column_num) else Symbol(self.x, i, self.column_speed, p.Random(i), 0) for i in range(self.y, (self.y + FONT_SIZE) * self.column_num, FONT_SIZE)]

    def draw(self):
        [s.draw() for s in self.column]


SL = [Column(x, 4) for x in range(0, WIDTH-FONT_SIZE, FONT_SIZE)]

while (1):
    box.fill(pygame.Color('black'))
    fps.tick(FPS)

    [spawn.draw() for spawn in SL]

    pygame.display.flip()
    [exit() for event in pygame.event.get() if event.type == pygame.QUIT]