import pygame
import sys

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

maus_pos = pygame.mouse.get_pos()
maus_klick = pygame.mouse.get_pressed()

pixel_font = pygame.font.Font("fonts/PixeloidSans.ttf", 30)

case_val = 1
enemy_count = 1


background = pygame.image.load("graphics/tower_lvl11.png").convert_alpha()

class tower:
    def __init__(self, tower_x, tower_y, tower_level):
        self.tower_x = tower_x
        self.tower_y = tower_y
        self.tower_level = tower_level

class enemy:
    def __init__(self, enemy_type, enemy_x, enemy_y, enemy_life, enemy_speed, case_val):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.enemy_life = enemy_life
        self.enemy_speed = enemy_speed
        self.enemy_type = enemy_type
        self.case_val = case_val

    def blit(self):

        enemy_lvl1 = pygame.image.load("graphics/monster_lvl1.png").convert_alpha()

        if self.enemy_type == "enemy_l1":
            screen.blit(enemy_lvl1, (self.enemy_x, self.enemy_y))
            print(str(self.enemy_y) + " <-Y   X-> " + str(self.enemy_x))


        match self.case_val:
            case 1:
                self.enemy_y += self.enemy_speed
                print("Case 1")
                if self.enemy_y >= 386:
                    self.case_val += 1
            case 2:
                self.enemy_x += self.enemy_speed
                print("Case 2")
                if self.enemy_x >= 800:
                    self.case_val += 1
            case 3:
                self.enemy_y += self.enemy_speed
                print("Case 3")


    def collide_wall(self):
        lifes = 10
        if enemy_x > 1920 or enemy_y > 1080:
            lifes -= 1
            print("lifes " + str(lifes) + " von 10 übrig")
            return True


def textObjekt(text, pixel_font):
    textFlaeche = pixel_font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1):
    global maus_aktiv
    global option
    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if but_txt == "Start":
                option = "Start"
            elif but_txt == "Einstellungen":
                option = "Einstellungen"
            elif but_txt == "Credits":
                option = "Credits"
            elif but_txt == "Home":
                option = "Home"
            elif but_txt == "Exit":
                sys.exit()
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, pixel_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)

def userinterface():
    pygame.draw.rect(screen, "Black", (1520, 0, 400, 1080))


enemy1 = enemy("enemy_l1", 215, 0, 0, 1, case_val)

runtime = True
while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        runtime = False
    if pressed[pygame.K_w]:
        while pressed[pygame.k_w]:
            enemy_count += 1
            enemy[enemy_count]




    screen.blit(background, (0,0))
    userinterface()
    enemy1.blit()
    enemy1.collide_wall()
    pygame.display.flip()

    clock.tick(fps)