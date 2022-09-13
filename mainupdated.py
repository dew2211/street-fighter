import pygame
from pygame import mixer
from fighter import Fighter


mixer. init()
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("1v1 me pussio")

clock = pygame.time.Clock()
fps = 60

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

start_count = 3
end_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
roundover_cooldown = 2000
main_menu = True
start = False
f1 = False
f2 = False
f3 = False



warriorsize = 162
warriorscale = 4
warrioroffset = [72, 56]
warriordata = [warriorsize, warriorscale, warrioroffset]
wizardscale = 3
wizardsize = 250
wizardoffset= [112, 107]
wizarddata = [wizardsize, wizardscale, wizardoffset]


odenscale = 3
odensize = 200
odenoffset= [117, 62]
odendata = [odensize, odenscale, odenoffset]

pygame.mixer.music.load("hello/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

cheff_fx = pygame.mixer.Sound("hello/audio/zoro.mp3")
cheff_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("hello/audio/magic.wav")
magic_fx.set_volume(0.5)


bg_image = pygame.image.load("hello/image/bg/skl.png").convert_alpha()
bg_image2 = pygame.image.load("hello/image/bg/mainmenu1.jpg").convert_alpha()
bg_image3 = pygame.image.load("hello/image/bg/bg1.jpg").convert_alpha()

warriorshit = pygame.image.load("hello/image/warrior/Sprites/warrior.png").convert_alpha()
wizardshit = pygame.image.load("hello/image/wizard/Sprites/wizard.png").convert_alpha()
odenshit = pygame.image.load("hello/image/wizard/Sprites/oden.png").convert_alpha()

startimg = pygame.image.load("hello/image/buttons/start.png").convert_alpha()
exitimg = pygame.image.load("hello/image/buttons/exit.png").convert_alpha()

# resizing the button
exit_set_image_size = (180,180)
set_image_size = (200,100)
startimg_okuz = pygame.transform.scale(startimg, set_image_size)
exitimg_okuz = pygame.transform.scale(exitimg, exit_set_image_size)


vitory = pygame. image.load("hello/font/victory2.png").convert_alpha()

f1img = pygame.image.load("hello/image/icon/luffy.png").convert_alpha()
f2img = pygame.image.load("hello/image/icon/zoro.jpg").convert_alpha()
f3img = pygame.image.load("hello/image/icon/ussop.png").convert_alpha()


warriorsteps = [10, 8, 1, 7, 7, 3, 7]
wizardsteps = [8, 8, 1, 8, 8, 3, 7]
odensteps = [8, 8, 2, 6, 6, 4, 6]



countdown_font = pygame.font.Font("hello/font/Megadeth.ttf", 80)
score_font = pygame.font.Font("hello/font/Megadeth.ttf", 30)


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button
        screen.blit(self.image, self.rect)

        return action


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def draw_bg():
  scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0 , 0))

def draw_mainmenu_bg():
  scaled_bg = pygame.transform.scale(bg_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0 , 0))

def draw_start_bg():
      scaled_bg = pygame.transform.scale(bg_image3, (SCREEN_WIDTH, SCREEN_HEIGHT))
      screen.blit(scaled_bg, (0, 0))


def draw_health_bar(health, x, y):
  division = health / 100
  pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 410, 40))
  pygame.draw.rect(screen, RED, (x, y, 400, 30))
  pygame.draw.rect(screen ,YELLOW, (x, y, 400 * division, 30))



def fighter_healthbar():
    if f1 == True:
        draw_health_bar(fighter_1.health, 20, 20)
    if f2 == True:
        draw_health_bar(fighter_2.health, 580, 20)
    if f3 == True:
        draw_health_bar(fighter_3.health, 20, 20)


def fighter_update():
    if f1 == True:
        fighter_1.update()
    if f2 == True:
        fighter_2.update()
    if f3 == True:

        fighter_3.update()


def fighter_draw():
    if f1 == True:

        fighter_1.draw(screen)
    if f2 == True:

        fighter_2.draw(screen)
    if f3 == True:
        fighter_3.draw(screen)







def fighter_move():
    if f1 == True:
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
    if f2 ==  True:
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    if f3 == True:
        fighter_3.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)


fighter_1 = Fighter(1, 200 , 310, False,  warriordata, warriorshit, warriorsteps, cheff_fx )
fighter_2 = Fighter(2, 700 , 310, True, wizarddata, wizardshit, wizardsteps, magic_fx)
fighter_3 = Fighter(1, 200 , 310, False,  odendata, odenshit, odensteps, cheff_fx )
def fighter_shet():
    if f1 == True:
        Fighter(1, 200 , 310, False,  warriordata, warriorshit, warriorsteps, cheff_fx )
    if f2 == True:

        Fighter(2, 700 , 310, True, wizarddata, wizardshit, wizardsteps, magic_fx)
    if f3 == True:

        Fighter(3, 200 , 310, False,  odendata, odenshit, odensteps, cheff_fx )


start_button = Button(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 , startimg_okuz)
start_button1 = Button(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 25, startimg_okuz)
exit_button = Button(SCREEN_WIDTH // 2 - 65, SCREEN_HEIGHT // 2 + 150, exitimg_okuz)
exit_button1 = Button(SCREEN_WIDTH // 2  , SCREEN_HEIGHT // 2 , exitimg_okuz)
start_button2 = Button(SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2 + 25, startimg_okuz)
start_button3 = Button(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 25, startimg_okuz)
start_button4 = Button(SCREEN_WIDTH // 2 + 350, SCREEN_HEIGHT // 2 + 25, startimg_okuz)

Run = True
while Run:
  clock.tick(fps)

  draw_bg()
  if main_menu == True:
        draw_mainmenu_bg()
        if exit_button.draw():
            Run = False
        if start_button.draw():
            main_menu =  False
            start = True




  elif start == True:
    draw_start_bg()

    if start_button1.draw():
        f1 = True
        f3 = False
        screen.blit(f1img, (100, 200))
    if start_button2.draw():
        f2 = True
        screen.blit(f2img, (300, 200))
    if start_button3.draw():
        f3 = True
        f1 = False

        screen.blit(f3img, (600, 200))
    if start_button4.draw():
        start = False






    if exit_button1.draw():
        main_menu = True
        if main_menu == True:
            draw_mainmenu_bg()
            if exit_button1.draw():
                Run = False
                if start_button.draw():
                    main_menu = False







  else:
    fighter_healthbar()
    #draw_health_bar(fighter_1.health, 20, 20)
    #draw_health_bar(fighter_2.health, 580, 20)
    draw_text("P1:  "+ str(score[0]), score_font, RED, 20, 60 )
    draw_text("P2:  "+ str(score[1]), score_font, RED, 580, 60 )

    if start_count <= 0:
      fighter_move()

      #fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2 , round_over)
      #fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
      draw_text(str(start_count), countdown_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
      if(pygame.time.get_ticks() - end_count_update) >= 1000:
        start_count -= 1
        end_count_update = pygame.time.get_ticks()


    fighter_update()
    #fighter_1.update()
    #fighter_2.update()


    fighter_draw()
    #fighter_1.draw(screen)
    #fighter_2.draw(screen)


    if round_over == False:
      if fighter_1.alive == False:
        score[1] += 1
        round_over = True
        roundover_time = pygame.time.get_ticks()
      elif fighter_2.alive == False:
        score[0] += 1
        round_over = True
        roundover_time = pygame.time.get_ticks()

    else:
      screen.blit(vitory, (300, 150))
      if pygame.time.get_ticks() - roundover_time > roundover_cooldown:
        round_over =  False
        start_count = 3


        fighter_1 = Fighter(1, 200, 310, False, warriordata, warriorshit, warriorsteps, cheff_fx)
        fighter_2 = Fighter(2, 700, 310, True, wizarddata, wizardshit, wizardsteps, magic_fx)
        fighter_3 = Fighter(1, 200, 310, False, odendata, odenshit, odensteps, cheff_fx)




  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Run =  False

  pygame.display.update()


pygame.quit()
