import pygame
from pygame import mixer
from fighter import Fighter
# putting the whole game into a function
def main():

    mixer. init()
    pygame.init()
    #create game window
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fatal combat")

    #set framerate
    clock = pygame.time.Clock()
    fps = 60

    #define colours
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    # when game is launched it goes to main menu
    main_menu = True
    #displays the character selection
    start = False
    #which fighter is chosen
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    f5 = False
    f6 = False

    #define game variables
    start_count = 3
    end_count_update = pygame.time.get_ticks()
    score = [0, 0]
    round_over = False
    roundover_cooldown = 2000
    total = 0
    p1 = 0
    p2 = 0

    #define fighter variable
    warriorsize = 162
    warriorscale = 4
    warrioroffset = [72, 56]
    warriordata = [warriorsize, warriorscale, warrioroffset]

    wizardsize = 250
    wizardscale = 3
    wizardoffset= [112, 107]
    wizarddata = [wizardsize, wizardscale, wizardoffset]

    odenscale = 3
    odensize = 200
    odenoffset = [90, 62]
    odendata = [odensize, odenscale, odenoffset]

    blackscale = 4
    blacksize = 150
    blackoffset = [67, 53]
    blackdata = [blacksize, blackscale, blackoffset]

    tribalscale = 3
    tribalsize = 126
    tribaloffset = [50, 22]
    tribaldata = [tribalsize, tribalscale, tribaloffset]

    firescale = 4
    firesize = 150
    fireoffset = [67, 53]
    firedata = [firesize, firescale, fireoffset]

    #load music and sounds
    pygame.mixer.music.load("hello/audio/music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)

    sword_fx = pygame.mixer.Sound("hello/audio/zoro.mp3")
    sword_fx.set_volume(0.5)
    magic_fx = pygame.mixer.Sound("hello/audio/magic.wav")
    magic_fx.set_volume(0.5)

    #load vicory image
    victory = pygame. image.load("hello/font/victory2.png").convert_alpha()


    #load background image
    bg_image = pygame.image.load("hello/image/bg/timur-tagirov-dojo-2-scene-3.jpg").convert_alpha()
    bg_image2 = pygame.image.load("hello/image/bg/mainmenu1.jpg").convert_alpha()
    bg_image3 = pygame.image.load("hello/image/bg/fire-and-ice-12.jpg").convert_alpha()
    bg_image4 = pygame.image.load("hello/image/bg/end.jpg").convert_alpha()

    #load spritesheets
    warriorsprite = pygame.image.load("hello/image/warrior/Sprites/warrior.png").convert_alpha()
    wizardsprite = pygame.image.load("hello/image/wizard/Sprites/wizard.png").convert_alpha()
    odensprite = pygame.image.load("hello/image/wizard/Sprites/oden.png").convert_alpha()
    blacksprite = pygame.image.load("hello/image/bossmans/black.png").convert_alpha()
    tribalsprite = pygame.image.load("hello/image/bossmans/tribal.png").convert_alpha()
    firesprite = pygame.image.load("hello/image/fireman/fireman.png").convert_alpha()

    # number of steps in each animation
    warriorsteps = [10, 8, 1, 7, 7, 3, 7]
    wizardsteps = [8, 8, 1, 8, 8, 3, 7]
    odensteps = [8, 8, 2, 6, 6, 4, 6]
    blacksteps = [8, 8, 2, 5, 5, 3, 8]
    tribalsteps = [10, 8, 3, 6, 9, 3, 11]
    firesteps = [8, 8, 8, 8, 8, 4, 5]


    #load button image
    startimg = pygame.image.load("hello/image/buttons/start.png").convert_alpha()
    exitimg = pygame.image.load("hello/image/buttons/exit.png").convert_alpha()
    fightimg = pygame.image.load("hello/image/buttons/fight.png").convert_alpha()
    restartimg = pygame.image.load("hello/image/buttons/playAgainButton2x.png").convert_alpha()
    exitimg2 = pygame.image.load("hello/image/buttons/exit2-removebg-preview.png").convert_alpha()

    # resizing the button
    exit_set_image_size = (180,180)
    set_image_size = (200,100)
    fight_image_size = (200, 100)
    restart_image_size = (200, 100)
    exit_set_image_size2 = (190, 80)
    fight_transform = pygame.transform.scale(fightimg, fight_image_size)
    startimg_transform = pygame.transform.scale(startimg, set_image_size)
    exitimg_transform = pygame.transform.scale(exitimg, exit_set_image_size)
    restart_transform = pygame.transform.scale(restartimg, restart_image_size)
    exitimg2_transform = pygame.transform.scale(exitimg2, exit_set_image_size2)

    #define font
    countdown_font = pygame.font.Font("hello/font/Megadeth.ttf", 80)
    score_font = pygame.font.Font("hello/font/Megadeth.ttf", 30)

    #character selection title
    fighterselection = pygame.image.load("hello/font/92a2eb3d5c71a50d469250b47aa7e000.png")
    fimg_set = (500, 100)
    selection_transform = pygame.transform.scale(fighterselection, fimg_set)

    #game logo
    gametitle = pygame.image.load("hello/font/294f99c6a0db4f68efc92366d6afb7e6.png")
    gimg_set = (500, 100)
    name_transform = pygame.transform.scale(gametitle, gimg_set)

    #arrow that point at the fighters
    arrow = pygame.image.load("hello/image/icon/arrowhead.png").convert_alpha()
    vimg_set = (100, 100)
    arrow_transform = pygame.transform.scale(arrow, vimg_set)

    #game over logo
    game_over_title = pygame.image.load("hello/font/game_over-removebg-preview.png")
    goimg_set = (500, 300)
    gameover_transform = pygame.transform.scale(game_over_title, goimg_set)

    #winner image
    winner1 = pygame. image.load("hello/font/winner-1.png").convert_alpha()
    wimg1_set = (250, 200)
    winner1_transform = pygame.transform.scale(winner1, wimg1_set)
    winner2 = pygame. image.load("hello/font/winner-2.png").convert_alpha()
    wimg2_set = (250, 200)
    winner2_transform = pygame.transform.scale(winner2, wimg2_set)

    #loading all the buttons for the fighters
    f1img = pygame.image.load("hello/image/icon/warrior-removebg-preview.png").convert_alpha()
    f1img_set_image_size = (100,150)
    f1img_transform = pygame.transform.scale(f1img, f1img_set_image_size)


    f2img = pygame.image.load("hello/image/icon/wizard.png").convert_alpha()
    f2img_set_image_size = (200,250)
    f2img_flip = pygame.transform.flip(f2img, True, False)
    f2img_transform = pygame.transform.scale(f2img_flip, f2img_set_image_size)


    f3img = pygame.image.load("hello/image/icon/oden.png").convert_alpha()
    f3img_set_image_size = (100,150)
    f3img_transform = pygame.transform.scale(f3img, f3img_set_image_size)



    f4img = pygame.image.load("hello/image/icon/black.png").convert_alpha()
    f4img_set_image_size = (100,150)
    f4img_flip = pygame.transform.flip(f4img, True, False)
    f4img_transform = pygame.transform.scale(f4img_flip, f4img_set_image_size)

    f5img = pygame.image.load("hello/image/icon/image_2022-09-14_203511247-removebg-preview.png").convert_alpha()
    f5img_set_image_size = (100,150)
    f5img_transform = pygame.transform.scale(f5img, f5img_set_image_size)


    f6img = pygame.image.load("hello/image/icon/image_2022-09-14_203557387-removebg-preview.png").convert_alpha()
    f6img_set_image_size = (150,200)
    f6img_flip = pygame.transform.flip(f6img, True, False)
    f6img_transform = pygame.transform.scale(f6img_flip, f6img_set_image_size)


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

    #function for drawing text
    def draw_text(text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      screen.blit(img, (x, y))

    #function for drawing background
    def draw_bg():
      scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
      screen.blit(scaled_bg, (0 , 0))

    def draw_mainmenu_bg():
      scaled_bg = pygame.transform.scale(bg_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))
      screen.blit(scaled_bg, (0 , 0))

    def draw_start_bg():
        scaled_bg = pygame.transform.scale(bg_image3, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))

    def draw_end_bg():
          scaled_bg = pygame.transform.scale(bg_image4, (SCREEN_WIDTH, SCREEN_HEIGHT))
          screen.blit(scaled_bg, (0, 0))

    #function for drawing fighter health bars
    def draw_health_bar(health, x, y):
        division = health / 100
        pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 410, 40))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * division, 30))

    #function that draw the health bar for each fighter
    def fighter_healthbar():
        if f1 == True:
            draw_health_bar(fighter_1.health, 20, 20)
        if f2 == True:
            draw_health_bar(fighter_2.health, 580, 20)
        if f3 == True:
            draw_health_bar(fighter_3.health, 20, 20)
        if f4 == True:
            draw_health_bar(fighter_4.health, 580, 20)
        if f5 == True:
            draw_health_bar(fighter_5.health, 20, 20)
        if f6 == True:
            draw_health_bar(fighter_6.health, 580, 20)
    #function that updates fighters
    def fighter_update():
        if f1 == True:
            fighter_1.update()
        if f2 == True:
            fighter_2.update()
        if f3 == True:

            fighter_3.update()
        if f4 == True:

            fighter_4.update()
        if f5 == True:

            fighter_5.update()
        if f6 == True:

            fighter_6.update()
    #function that draws fighters
    def fighter_draw():
        if f1 == True:
            fighter_1.draw(screen)
        if f2 == True:
            fighter_2.draw(screen)
        if f3 == True:
            fighter_3.draw(screen)
        if f4 == True:
            fighter_4.draw(screen)
        if f5 == True:
            fighter_5.draw(screen)
        if f6 == True:
            fighter_6.draw(screen)
    #function that moves the fighters
    def fighter_move():
        if f1 == True:
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, fighter_4, fighter_6,  round_over)
        if f2 ==  True:
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, fighter_3, fighter_5, round_over)
        if f3 == True:
            fighter_3.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, fighter_6, fighter_4, round_over)
        if f4 ==  True:
            fighter_4.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, fighter_3, fighter_5, round_over)
        if f5 ==  True:
            fighter_5.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, fighter_4, fighter_6, round_over)
        if f6 ==  True:
            fighter_6.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, fighter_3, fighter_5,  round_over)


    #position of the button
    start_button = Button(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2, startimg_transform)
    exit_button = Button(SCREEN_WIDTH // 2 - 65, SCREEN_HEIGHT // 2 + 150, exitimg_transform)
    exit_button1 = Button(SCREEN_WIDTH // 2 - 500, SCREEN_HEIGHT // 2 - 350, exitimg_transform)
    fight_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, fight_transform)
    warrior_button = Button(SCREEN_WIDTH // 2 - 235, SCREEN_HEIGHT // 2 + 25, f1img_transform)
    wizard_button = Button(SCREEN_WIDTH // 2 + 350, SCREEN_HEIGHT // 2 - 75, f2img_transform)
    oden_button = Button(SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 + 25, f3img_transform)
    black_button = Button(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 25, f4img_transform)
    armour_button = Button(SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2 + 25, f5img_transform)
    fire_button = Button(SCREEN_WIDTH // 2 + 230, SCREEN_HEIGHT // 2, f6img_transform)
    restart_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, restart_transform)
    exit_button2 = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, exitimg2_transform)

    #create instances of fighters
    fighter_1 = Fighter(1, 200, 310,False, warriordata, warriorsprite, warriorsteps, sword_fx)
    fighter_2 = Fighter(2, 700, 310, True, wizarddata,  wizardsprite, wizardsteps, magic_fx)
    fighter_3 = Fighter(1, 200, 310, False, odendata, odensprite, odensteps, sword_fx)
    fighter_4 = Fighter(2, 700, 310, True, blackdata, blacksprite, blacksteps, sword_fx)
    fighter_5 = Fighter(1, 200, 310, False, tribaldata, tribalsprite, tribalsteps, sword_fx)
    fighter_6 = Fighter(2, 700, 310, True, firedata, firesprite, firesteps, sword_fx)


    Run = True
    while Run:
        clock.tick(fps)

        draw_bg()

        if main_menu == True:
            draw_mainmenu_bg()
            screen.blit(name_transform, (10, 0))
            if exit_button.draw():
                Run = False
            if start_button.draw():
                main_menu = False
                start = True




        elif start == True:
            draw_start_bg()
            screen.blit(selection_transform, (250, 0))
            # display all the buttons for the fighter
            if warrior_button.draw():
                f1 = True
                f3 = False
                f5 = False
            if wizard_button.draw():
                f2 = True
                f4 = False
                f6 = False
            if oden_button.draw():
                f3 = True
                f1 = False
                f5 = False
            if black_button.draw():
                f4 = True
                f2 = False
                f6 = False
            if armour_button.draw():
                f5 = True
                f1 = False
                f3 = False
            if fire_button.draw():
                f6 = True
                f2 = False
                f4 = False
            # puts an arrow when the fighter  is selected
            if f1 == True:
                screen.blit(arrow_transform, (250, 450))
            if f2 == True:
                screen.blit(arrow_transform, (900, 450))
            if f3 == True:
                screen.blit(arrow_transform, (50, 450))
            if f4 == True:
                screen.blit(arrow_transform, (650, 450))
            if f5 == True:
                screen.blit(arrow_transform, (150, 450))
            if f6 == True:
                screen.blit(arrow_transform, (750, 450))

            if fight_button.draw():
                start = False
            # return back to the main menu
            if exit_button1.draw():
                main_menu = True
                if main_menu == True:
                    draw_mainmenu_bg()
                    if exit_button1.draw():
                        Run = False
                        if start_button.draw():
                            main_menu = False

        else:
            # show player health
            fighter_healthbar()
            # show player score
            draw_text("P1:  " + str(score[0]), score_font, RED, 20, 60)
            draw_text("P2:  " + str(score[1]), score_font, RED, 580, 60)
            # update countdown
            if start_count <= 0:
                # move fighters
                fighter_move()
            else:
                # display count timer
                draw_text(str(start_count), countdown_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
                # update count timer
                if (pygame.time.get_ticks() - end_count_update) >= 1000:
                    start_count -= 1
                    end_count_update = pygame.time.get_ticks()
            # update fighters
            fighter_update()
            # draw fighters
            fighter_draw()

            # check for player defeat
        if round_over == False:
            if fighter_1.alive == False:
                score[1] += 1
                p1 += 1
                total += 1
                round_over = True
                roundover_time = pygame.time.get_ticks()
            elif fighter_2.alive == False:
                score[0] += 1
                total += 1
                p2 += 1
                round_over = True
                roundover_time = pygame.time.get_ticks()
            elif fighter_3.alive == False:
                score[1] += 1
                p1 += 1
                total += 1
                round_over = True
                roundover_time = pygame.time.get_ticks()
            elif fighter_4.alive == False:
                score[0] += 1
                total += 1
                p2 += 1
                round_over = True
                roundover_time = pygame.time.get_ticks()
            elif fighter_5.alive == False:
                score[1] += 1
                p1 += 1
                total += 1
                round_over = True
                roundover_time = pygame.time.get_ticks()
            elif fighter_6.alive == False:
                score[0] += 1
                p2 += 1
                total += 1
                round_over = True
                roundover_time = pygame.time.get_ticks()

        elif round_over == True:
            # This if statement limit the game to 5 rounds
            if total <= 4:
                screen.blit(victory, (300, 150))

                if pygame.time.get_ticks() - roundover_time > roundover_cooldown:
                    round_over = False
                    start_count = 3

                    fighter_1 = Fighter(1, 200, 310, False, warriordata, warriorsprite, warriorsteps, sword_fx)
                    fighter_2 = Fighter(2, 700, 310, True, wizarddata, wizardsprite, wizardsteps, magic_fx)
                    fighter_3 = Fighter(1, 200, 310, False, odendata, odensprite, odensteps, sword_fx)
                    fighter_4 = Fighter(2, 700, 310, True, blackdata, blacksprite, blacksteps, sword_fx)
                    fighter_5 = Fighter(1, 200, 310, False, tribaldata, tribalsprite, tribalsteps, sword_fx)
                    fighter_6 = Fighter(2, 700, 310, True, firedata, firesprite, firesteps, sword_fx)

        else:
            pass
        if total == 5:
            draw_end_bg()
            screen.blit(gameover_transform, (250, -75))
            if p1 > p2 :
                screen.blit(winner2_transform, (375, 110))
            else:
                screen.blit(winner1_transform, (375, 110))
            if restart_button.draw():
                main()
            if exit_button2.draw():
                Run = False

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
        # update display
        pygame.display.update()
    #exit pygame
    pygame.quit()

#calling the game
main()
