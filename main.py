import pygame

pygame.init()

screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
fps = 60

tower_x = 0
tower_y = 0
tower_level = 1
enemy_x = 30
enemy_y = 30
enemy_life = 0
enemy_speed = 1

background = pygame.image.load("graphics/test_arena.png").convert_alpha()

class tower:
    def __init__(self, tower_x, tower_y, tower_level):
        self.tower_x = tower_x
        self.tower_y = tower_y
        self.tower_level = tower_level


class enemy:
    def __init__(self, enemy_type, enemy_x, enemy_y, enemy_life, enemy_speed):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.enemy_life = enemy_life
        self.enemy_speed = enemy_speed
        self.enemy_type = enemy_type

    def blit(self):

        enemy_lvl1 = pygame.image.load("graphics/monster_lvl1.png").convert_alpha()

        if self.enemy_type == "enemy_l1":
            screen.blit(enemy_lvl1, (self.enemy_x, self.enemy_y))
            print(str(self.enemy_y) + " <-Y   X-> " + str(self.enemy_x))

        if self.enemy_y < 750:
            self.enemy_y += self.enemy_speed
        elif self.enemy_y >= 750:
            self.enemy_x += self.enemy_speed





enemy1 = enemy("enemy_l1", 0, 0, 0, 1)

runtime = True
while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        runtime = False




    screen.fill((0, 0, 255))
    enemy1.blit()
    pygame.display.flip()

    clock.tick(fps)