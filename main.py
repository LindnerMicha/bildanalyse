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


# https://stackoverflow.com/questions/63523461/spawn-multiple-enemies-pygame

enemy_img = pygame.image.load("graphics/monster_lvl1.png")
enemy = []
enemyX = []
enemy_spawnX = 300
enemyY = []
enemy_spawnY = 300
enemy_num = 0
spawn_stop = False

maus_pos = pygame.mouse.get_pos()
maus_klick = pygame.mouse.get_pressed()

pixel_font = pygame.font.Font("fonts/PixeloidSans.ttf", 30)

case_val1 = 1
case_val2 = 1
case_val3 = 1
case_val4 = 1
case_val5 = 1
len_array = 0
count = 0

background = pygame.image.load("graphics/tower_lvl11.png").convert_alpha()

class tower:
    def __init__(self, tower_x, tower_y, tower_level):
        self.tower_x = tower_x
        self.tower_y = tower_y
        self.tower_level = tower_level



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


runtime = True
while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        runtime = False
    if pressed[pygame.K_w]:
        enemy_num += 1




    for i in range(enemy_num):
        enemy.append(enemy_img)
        enemyX.append(215)
        enemyY.append(0)

    for i in range(enemy_num):
        enemyY[i] += 4


    screen.blit(background, (0,0))
    for i in range(enemy_num):
        screen.blit(enemy[i], (enemyX[i], enemyY[i]))

    userinterface()
    pygame.display.flip()

    clock.tick(fps)