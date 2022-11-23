import pygame
import sys



pygame.init()


global option
global setting_state
global set_decider


option = "Home"

screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
fps = 60
fps_tick = 0


tower_x = 0
tower_y = 0
tower_level = 1

ticker = 0
ticker_sec = 0
enemy_spawn_sec = 1     # -> Sekunden

user_input = ""
set_decider = ""
case_val = 0
case_val2 = 0

# https://stackoverflow.com/questions/63523461/spawn-multiple-enemies-pygame

enemy_img = pygame.image.load("graphics/monster_lvl1.png")
enemy = []
enemyX = []
enemy_spawnX = 300
enemyY = []
enemy_spawnY = 300
global enemy_num
enemy_num = 0
spawn_stop = False
slider_bool = True

maus_pos = pygame.mouse.get_pos()
maus_klick = pygame.mouse.get_pressed()

pixel_font60 = pygame.font.Font("fonts/PixeloidSans.ttf", 60)
pixel_font30 = pygame.font.Font("fonts/PixeloidSans.ttf", 30)
pixel_font15 = pygame.font.Font("fonts/PixeloidSans.ttf", 15)
sys_font15 = pygame.font.SysFont(None, 15)
sys_font30 = pygame.font.SysFont(None, 30)

background = pygame.image.load("graphics/tower_lvl11.png").convert_alpha()
tower_img = pygame.image.load("graphics/tower.png").convert_alpha()
home_background = pygame.image.load("graphics/pixback.jpg").convert_alpha()

class tower:
    def __init__(self, tower_x, tower_y, tower_level):
        self.tower_x = tower_x
        self.tower_y = tower_y
        self.tower_level = tower_level

def draw_text(text, sys_font15, color, screen, x , y):
    textobj = sys_font15.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option
    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            option = but_txt
            if option == "Exit":
                sys.exit()
            elif but_txt == "Resume":
                option = "Play"
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)

def setting_button(set_state, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global setting_state
    global maus_aktiv
    global set_decider
    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            if set_state == "+":
                set_decider = "+"
            if set_state == "-":
                set_decider = "-"
        if maus_klick[0] == 0:
            maus_aktiv = False
            set_decider = ""
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))

    textGrund, textkasten = textObjekt(set_state, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)

def userinterface():
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, "White", (1520, 0, 400, 1080))
    button("BUY LVL1", 1570, 400, 80, 45, "Green", "Grey", pixel_font15)
    screen.blit(tower_img, (1550,250))
    button("BUY LVL2", 1780, 400, 80, 45, "Green", "Grey", pixel_font15)
    screen.blit(tower_img, (1760, 250))
    button("BUY LVL3", 1570, 650, 80, 45, "Green", "Grey", pixel_font15)
    screen.blit(tower_img, (1550, 500))
    button("BUY LVL4", 1780, 650, 80, 45, "Green", "Grey", pixel_font15)
    screen.blit(tower_img, (1760, 500))

    button("Home", 1570, 980, 80, 45, "Green", "Red", pixel_font15)
    button("Settings", 1680, 980, 80, 45, "Green", "Red", pixel_font15)
    button("Exit", 1790, 980, 80, 45, "Green", "Red", pixel_font15)

def slide_setting(slide_text, min_val, max_val, slide_x, slide_y):


    setting_button("+", slide_x + 750, slide_y, 40, 40, (68, 212, 219), "Grey", sys_font30)
    setting_button("-", slide_x + 240, slide_y, 40, 40, (68, 212, 219), "Grey", sys_font30)
    draw_text(str(slide_text), pixel_font30, (0,0,0), screen, slide_x, slide_y)
    draw_text(str(min_val), pixel_font30, (0, 0, 0), screen, slide_x + 300,slide_y)
    draw_text(str(max_val), pixel_font30, (0, 0, 0), screen, slide_x + 700,slide_y)




def setting_slider(slide_text, min_val, max_val, slide_x, slide_y):
    pass

def homescreen():
    screen.blit(home_background, (0, 0))
    pygame.draw.rect(screen, (48, 79, 84), (0, 0, 350, 1080))

    button("Play", 50, 100, 200, 60, (31, 64, 69), "Green", pixel_font30)
    button("Settings", 50, 300, 200, 60, (31, 64, 69), "Green", pixel_font30)
    button("Exit", 50, 500, 200, 60, (31, 64, 69), "Green", pixel_font30)

def settings():
    screen.blit(home_background, (0, 0))
    pygame.draw.rect(screen, (48, 79, 84), (510, 0, 900, 1080))
    draw_text("Settings", pixel_font60, (0, 0, 0), screen, 860, 0)
    button("Home", 755, 980, 110, 45, (68, 212, 219), "Green", pixel_font30)
    button("Resume", 1055, 980, 140, 45, (68, 212, 219), "Green", pixel_font30)

def show_fps():
    fps_tick = str(int(clock.get_fps()))
    draw_text(str(fps_tick), sys_font30, "Red", screen, 0, 0)

def debug():
    print(str(ticker_sec) + "<-Ticker Sec  - EnNum -> " + str(enemy_num))
    print(maus_pos[0], maus_pos[1])

rec_x = 930
rec_y = 300

runtime = True
while runtime:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False


#region #Deffinitionen updaten
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    pressed = pygame.key.get_pressed()
    #endregion

    if pressed[pygame.K_SPACE]:
        runtime = False
    if pressed[pygame.K_w]:
        pass


#region #enemy Spawn + Movement
    if ticker > 40:
        ticker_sec +=1
        ticker = 0

    if ticker_sec > enemy_spawn_sec:
        enemy_num += 1
        ticker_sec = 0

    for i in range(enemy_num):
        enemy.append(enemy_img)
        enemyX.append(215)
        enemyY.append(0)

    for i in range(enemy_num):
        enemyY[i] += 4
#endregion


    #draw_text("TestTestTest", sys_font15, "Red", screen, 100, 100)
    if option == "Home":
        homescreen()
        enemy.clear()
        enemyX.clear()
        enemyY.clear()
        enemy_spawnY = 300
        enemy_spawnX = 300
        ticker_sec = 0
        ticker = 0

    elif option == "Play":
        userinterface()
        for i in range(enemy_num):
            screen.blit(enemy[i], (enemyX[i], enemyY[i]))


    elif option == "Settings":
        settings()
        pygame.draw.rect(screen, (0, 0, 0), (930, rec_y+10, 320, 15))
        slide_setting("Test", 0, 10, 580, 300)
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if set_decider == "+":
                case_val +=1
                if case_val >= 9:
                    case_val = 9
            elif set_decider == "-":
                case_val -= 1
                if case_val <= 0:
                    case_val = 0
        if maus_klick[0] == 0:
            maus_aktiv = False

        match case_val:
            case 0:
                pygame.draw.rect(screen, "Grey", (900, 300, 35, 35))
            case 1:
                pygame.draw.rect(screen, "Grey", (935, 300, 35, 35))
            case 2:
                pygame.draw.rect(screen, "Grey", (970, 300, 35, 35))
            case 3:
                pygame.draw.rect(screen, "Grey", (1005, 300, 35, 35))
            case 4:
                pygame.draw.rect(screen, "Grey", (1040, 300, 35, 35))
            case 5:
                pygame.draw.rect(screen, "Grey", (1075, 300, 35, 35))
            case 6:
                pygame.draw.rect(screen, "Grey", (1110, 300, 35, 35))
            case 7:
                pygame.draw.rect(screen, "Grey", (1145, 300, 35, 35))
            case 8:
                pygame.draw.rect(screen, "Grey", (1180, 300, 35, 35))
            case 9:
                pygame.draw.rect(screen, "Grey", (1215, 300, 35, 35))

        slide_setting("Musik", "OFF", "ON", 580, 600)
        if maus_klick[0] == 1 and maus_aktiv == False:
            print(maus_aktiv)
            maus_aktiv = True
            if set_decider == "+":
                case_val2 += 1
            elif set_decider == "-":
                case_val2 -= 1
        if maus_klick[0] == 0:
            maus_aktiv = False
        match case_val2:
            case 0:
                pygame.draw.rect(screen, "Grey", (900, 600, 35, 35))
            case 1:
                pygame.draw.rect(screen, "Grey", (935, 600, 35, 35))



    show_fps()
    pygame.display.flip()
    ticker += 1
    clock.tick(fps)