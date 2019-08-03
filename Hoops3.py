import pygame
assert pygame.init()==(6,0)
from pygame.locals import *
from random import randint, random
from time import sleep

gravity = 0.0006
ym = 0
xm = 0

b_size = 13
bx = 0
by = 0
b_color = (255,  120, 0)
ball = pygame.Surface((b_size, b_size))
ball.fill(b_color)
score = 0

l1 = pygame.Surface((11, 2))
l2 = pygame.Surface((2, 11))

hoop = pygame.Surface((20, 3))
e1 = pygame.Surface((8, 3))
e2 = pygame.Surface((8, 3))
bb = pygame.Surface((3, 35))
e1.fill((255, 0, 0))
e2.fill((255, 0, 0))
hoop.fill((255, 0, 0))
h_pos = (500, 250)

set_font_button = pygame.image.load("button_set-font.png")
tog_al = pygame.image.load("button_toggle-anti-lag.png")
randt = pygame.image.load("button_rand-theme.png")
x_set = pygame.image.load("button_x.png")
winter = pygame.image.load("button_winter.png")
fall = pygame.image.load("button_fall.png")
summer = pygame.image.load("button_summer.png")
spring = pygame.image.load("button_spring.png")
thanos = pygame.image.load("button_thanos.png")
lock = pygame.image.load("lock.jpg")
lock2 = pygame.image.load("lock2.jpg")
lock3 = pygame.image.load("lock3.jpg")
blcl = pygame.image.load("button_ball-color.png")

net = pygame.image.load("net.png")
bar = pygame.image.load("bar.png")

coin_file = open("coins.txt", "r+")
coins = int(coin_file.read())
thanos_ul_file = open("thanos.txt", "r+")
thanos_ul = thanos_ul_file.read()
if thanos_ul == "0":
    thanos_ul = False
else:
    thanos_ul = True

randulf = open("rand.txt", "r+")
randul = randulf.read()
if randul == "0":
    randul = False
else:
    randul = True

wintulf = open("winter.txt", "r+")
wintul = wintulf.read()
if wintul == "0":
    wintul = False
else:
    wintul = True

ofnt_thing = input("What font would you like your score to be in? ")

if ofnt_thing == "":
    file = open("fontdefault.txt", "r+")
    default = file.read()
    print("Set to default: " + default)
    ofnt_thing = default
    file.close()

elif ofnt_thing == "set_default()":
    newfile = open("fontdefault.txt", "w+")
    newdef = input("New default font: ")
    newfile.write(newdef)
    ofnt_thing = newdef
    newfile.close()
    
ofnt = pygame.font.SysFont(str(ofnt_thing), 50)
stxt = ofnt.render(str(score), False, (255, 20, 255))

fntcol = (255, 20, 255)
ctxt = ofnt.render("$" + str(coins), False, (fntcol))

lag = input("Anti-Lag Mode? [Y/N]\n")
if lag == "N":
    lag = False
    g_a = input("Do you want even higher-quality graphics? (more lag) [Y/N]\n")
    if g_a == "Y":
        s_l = 85
    else:
        s_l = 65
elif lag == "Y":
    lag = True

turns = 5

def blit():
    global h_pos
    global screen, stxt
    global ball, l1, l2
    global coins, ctxt, fntcol
    screen.blit(stxt, (500, 20))
    ctxt = ofnt.render("$" + str(coins), False, (fntcol))
    screen.blit(ctxt, (850, 20))
    screen.blit(bar, (950, 0))
    screen.blit(hoop, h_pos)
    screen.blit(e1, (h_pos[0] - 8, h_pos[1]))
    screen.blit(e2, (h_pos[0] + 20, h_pos[1]))
    screen.blit(net, (h_pos[0] - 8, h_pos[1] + 3))
    screen.blit(bb, (h_pos[0] + 25, h_pos[1] - 35))
    try:
        screen.blit(plustxt, (850, 50))
    except:
        pass
    ball.blit(l1, (0, 6))
    ball.blit(l2, (5, 0))

pygame.display.set_caption("Hoops2 - MM Olde Games")
pygame.font.init()
font = pygame.font.SysFont('HarryP', 10)
ll1 = pygame.Surface((3, 2000))
ll2 = pygame.Surface((2000, 3))
ll1.fill((190, 190, 190))
ll2.fill((190, 190, 190))
pwr = pygame.Surface((50, 3))
pwr.fill((0, 0, 0))
screen = pygame.display.set_mode((1000, 500))
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
bg = pygame.Surface((1000, 500))
bgcol = (255, 255, 0)
bg.fill(bgcol)
screen.blit(bg, (0, 0))
blit()
screen.blit(ball, (bx, by))
pygame.display.flip()
playing = True
magic = False
screen.blit(stxt, (500, 20))
av = 0
to = 0

trail = []
trail2 = pygame.image.load("streak.png")


g1 = 50
g2 = 2.9

stage = 1

streak = 0
edge = False

fntcol = (255 - bgcol[0], 255 - bgcol[1], 255 - bgcol[2])
while playing:
    ym = 0
    xm = 0
    p = 0
    dy = 0
    dx = 0
    r = 0
    mgc = 1
    while not magic:
        ### GLITCH FIXING ###
        if bx >= 987 or bx <= 0:
            bx = 25
        ebf = False
        exbf = False
        for event in pygame.event.get():
            lnx, lny = pygame.mouse.get_pos()
            
            screen.fill(bgcol)
            blit()
            screen.blit(ball, (bx, by))
            if not lag:
                post = font.render(" (" + str(int(pygame.mouse.get_pos()[0])) + ", " + str(int(pygame.mouse.get_pos()[1])) + ")", False, fntcol)
                screen.blit(post, (pygame.mouse.get_pos()[0] + 5, pygame.mouse.get_pos()[1] + 5))
            screen.blit(ll1, (lnx, lny - 1000))
            screen.blit(ll2, (lnx - 1000, lny))
            if not lag:
                stt = font.render("Y: " + str(int(ym * 1000)) + "   X: " + str(int(xm * 1000)), False, fntcol)
                screen.blit(stt, (20, 20))
            if mgc == 0:
                #bg.fill((25, 25, 25))
                #screen.blit(bg, (0, 0))
                screen.blit(set_font_button, (250, 15))
                screen.blit(tog_al, (250, 65))
                screen.blit(randt, (250, 115))
                screen.blit(x_set, (450, 15))
                screen.blit(winter, (250, 165))
                screen.blit(fall, (250, 215))
                screen.blit(summer, (250, 265))
                screen.blit(spring, (250, 315))
                screen.blit(thanos, (250, 365))
                if thanos_ul == False:
                    screen.blit(lock, (230, 365))
                if randul == False:
                    screen.blit(lock2, (230, 115))
                if wintul == False:
                    screen.blit(lock3, (230, 165))
                screen.blit(blcl, (250, 415))
            pygame.display.flip()
            if event.type == MOUSEBUTTONDOWN and mgc != 0:
                mx, my = pygame.mouse.get_pos()
                magic = True
            elif event.type == KEYDOWN and mgc != 0:
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_s:
                    mgc = 0
                    screen.blit(set_font_button, (250, 15))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(tog_al, (250, 65))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(randt, (250, 115))
                    if randul == False:
                        screen.blit(lock2, (230, 115))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(winter, (250, 165))
                    if wintul == False:
                        screen.blit(lock3, (230, 165))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(fall, (250, 215))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(summer, (250, 265))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(spring, (250, 315))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(thanos, (250, 365))
                    pygame.display.flip()
                    if thanos_ul == False:
                        screen.blit(lock, (230, 365))
                    sleep(0.04)
                    screen.blit(blcl, (250, 415))
                    pygame.display.flip()
                    sleep(0.04)
                    screen.blit(x_set, (450, 15))
                    pygame.display.flip()
            blobx, bloby = pygame.mouse.get_pos()
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 15 and blobx<= 363 and bloby <= 51:
                ofnt_thing = input("What font would you like your score to be in? ")
                if ofnt_thing == "":
                    file = open("fontdefault.txt", "r+")
                    default = file.read()
                    print("Set to default: " + default)
                    ofnt_thing = default
                    file.close()
                elif ofnt_thing == "set_default()":
                    newfile = open("fontdefault.txt", "w+")
                    newdef = input("New default font: ")
                    newfile.write(newdef)
                    ofnt_thing = newdef
                    newfile.close()
                ofnt = pygame.font.SysFont(str(ofnt_thing), 50)
                stxt = ofnt.render(str(score), False, fntcol)
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 65 and blobx <= 437 and bloby <= 100:
                if lag:
                    lag = False
                else:
                    lag = True
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 450 and bloby >= 15 and blobx <= 488 and bloby <= 54:
                mgc = 1
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 115 and blobx <= 422 and bloby <= 154 and randul:
                bgcol = (randint(1,255),randint(1,255),randint(1,255))
                bg.fill(bgcol)
                screen.blit(bg, (0, 0))
                screen.fill(bgcol)
                fntcol = (255 - bgcol[0], 255 - bgcol[1], 255 - bgcol[2])
                ball.fill(fntcol)
                stxt = ofnt.render(str(score), False, fntcol)
                pygame.display.flip()
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 165 and blobx <= 357 and bloby <= 205 and wintul:
                bgcol = (153, 255, 255)
                bg.fill(bgcol)
                screen.blit(bg, (0, 0))
                screen.fill(bgcol)
                fntcol = (3, 72, 105)
                ball.fill(fntcol)
                stxt = ofnt.render(str(score), False, fntcol)
                pygame.display.flip()
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 215 and blobx <= 322 and bloby <= 252:
                bgcol = (255, 91, 20)
                bg.fill(bgcol)
                screen.blit(bg, (0, 0))
                screen.fill(bgcol)
                fntcol = (84, 0, 0)
                ball.fill(fntcol)
                stxt = ofnt.render(str(score), False, fntcol)
                pygame.display.flip()
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 265 and blobx <= 375 and bloby <= 305:
                bgcol = (255, 255, 0)
                bg.fill(bgcol)
                screen.blit(bg, (0, 0))
                screen.fill(bgcol)
                fntcol = (39, 78, 19)
                ball.fill(fntcol)
                stxt = ofnt.render(str(score), False, fntcol)
                pygame.display.flip()
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 315 and blobx <= 352 and bloby <= 353:
                bgcol = (25, 255, 1)
                bg.fill(bgcol)
                screen.blit(bg, (0, 0))
                screen.fill(bgcol)
                fntcol = (255, 0, 237)
                ball.fill(fntcol)
                stxt = ofnt.render(str(score), False, fntcol)
                pygame.display.flip()
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 365 and blobx <= 361 and bloby <= 403 and thanos_ul:
                bgcol = (153, 0, 255)
                bg.fill(bgcol)
                screen.blit(bg, (0, 0))
                screen.fill(bgcol)
                fntcol = (255, 0, 255)
                ball.fill(fntcol)
                stxt = ofnt.render(str(score), False, fntcol)
                pygame.display.flip()
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 250 and bloby >= 415 and blobx <= 409 and bloby <= 454:
                r = int(input("R: "))
                g = int(input("G: "))
                b = int(input("B: "))
                print("\n\n")
                try:
                    ball.fill((r, g, b))
                except:
                    print("Invalid color given...")
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 230 and bloby >= 365 and blobx <= 261 and bloby <= 410 and coins >= 5000:
                thanos_ul = True
                coins -= 5000
                coin_file.close()
                coin_file = open("coins.txt", "w+")
                coinstring = str(coins)
                coin_file.write(coinstring)
                coin_file.close()
                coin_file = open("coins.txt", "r+")
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 230 and bloby >= 115 and blobx <= 261 and bloby <= 160 and coins >= 7000:
                randul = True
                coins -= 7000
                coin_file.close()
                coin_file = open("coins.txt", "w+")
                coinstring = str(coins)
                coin_file.write(coinstring)
                coin_file.close()
                coin_file = open("coins.txt", "r+")
                randulf.close()
                randulf = open("rand.txt", "w+")
                randulf.write("1")
                randulf.close()
                randulf = open("rand.txt", "r+")
            if mgc == 0 and event.type == MOUSEBUTTONDOWN and blobx >= 230 and bloby >= 165 and blobx <= 354 and bloby <= 205 and coins >= 100 and wintul == False:
                wintul = True
                coins -= 100
                coin_file.close()
                coin_file = open("coins.txt", "w+")
                coinstring = str(coins)
                coin_file.write(coinstring)
                coin_file.close()
                coin_file = open("coins.txt", "r+")
                wintulf.close()
                wintulf = open("winter.txt", "w+")
                wintulf.write("1")
                wintulf.close()
                wintulf = open("winter.txt", "r+")
    magic = False
    while not magic:
            for event in pygame.event.get():
                post = font.render(" " + str(500 - int(pygame.mouse.get_pos()[1])), False, fntcol)
                screen.fill(bgcol)
                blit()
                screen.blit(post, (952, pygame.mouse.get_pos()[1] - 9))
                screen.blit(ll1, (lnx, lny - 1000))
                screen.blit(ll2, (lnx - 1000, lny))
                screen.blit(ball, (bx, by))
                screen.blit(pwr, (950, pygame.mouse.get_pos()[1]))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN:
                    n, p = pygame.mouse.get_pos()
                    magic = True
                    
            
    magic = False
    dy = my - by
    dx = mx - bx
    r = dx / dy
    p = 985 - p
    if p < 0:
        p = 0
    p /= 1450
    ym = p
    if dy < 0:
        ym *= -1
    xm = p * r
    if dy < 0:
        xm *= -1
    inx = bx
    edge = False
    while by < 487:
        pygame.event.get()
        screen.fill(bgcol)
        b_pos = (bx, by)
        if streak >= 3 and not lag:
            trail = [(b_pos[0] + 2, b_pos[1] + 2)] + trail
            try:
                if not lag:
                    for i in range(s_l):
                        screen.blit(trail2, (trail[i][0], trail[i][1]))
            except:
                pass
        else:
            trail = []
        if not lag:
            stt = font.render("Y: " + str(int(ym * 1000)) + "   X: " + str(int(xm * 1000)), False, fntcol)
        bx += xm
        by += ym
        if not lag:
            screen.blit(stt, (20, 20))
        ym += gravity
        blit()
        screen.blit(ball, (bx, by))
        pygame.display.flip()
        if abs(by - h_pos[1]) < 3 and bx - h_pos[0] < 20 and bx - h_pos[0] > 0:
            prevcoin = coins
            if abs(inx - h_pos[0]) >= 184:
                score += 3
                coins += 2
            else:
                score += 2
                coins += 1
            if turns >= 4:
                coins += 2
            elif turns >= 3:
                coins += 1
            coins += streak
            plustxt = ofnt.render("+$" + str(coins - prevcoin), False, fntcol)
            screen.blit(plustxt, (850, 50))
            pygame.display.flip()
            #sleep(0.2)
            #h_pos = (randint(20, 850), randint(150, 450))
            bx = randint(50, 950)
            by = randint(25, 50)
            mx += randint(1, 3) / 10
            av += 6 - turns
            to += 1
            if turns >= 3:
                streak += 1
            else:
                streak = 0
            turns = 5
            stxt = ofnt.render(str(score), False, fntcol)
        ### BOUNCE OFF WALLS ###
        if bx >= 987 or bx <= 0:
            xm *= -1
        ''''''
        if abs(by - h_pos[1]) < 3 and bx - (h_pos[0] + 20) < 8 and bx - (h_pos[0] + 20) > 0:
            ym *= -1 * random()
            edge = True
            if exbf == False:
                #xm = 0
                #while xm == 0:
                xm = -0.73 * xm #randint(-2, 2) / 11 * random()
                exbf = True
            else:
                pass
        if abs(by - h_pos[1]) < 13 and bx - (h_pos[0] - 8) < 8 and bx - (h_pos[0] - 8) > 0:
            ym *= -1 * random()
            edge = True
            if ebf == False:
                #xm = 0
                #while xm == 0:
                xm = -0.73 * xm #randint(-2, 2) / 11 * random()
                ebf = True
            else:
                pass
        ### BACKBOARD COLLISION DETECTIONS ###
        if abs(by - h_pos[1]) <=  45 and by - h_pos[1] < 0 and (bx + 13) > h_pos[0] + 28 and (bx < (h_pos[0] + 31) or (bx + 13) < (h_pos[0] + 31)):
            xm *= -1
            
    turns -= 1
    if turns <= 0:
        #pygame.quit()
        print("End of trial stage! SCORE: " + str(score))
        print("Average turns to score: " + str(av / to))
        if score >= g1 and ((av / to) - ((score - (g1 - 5)) / 100)) <= g2:
            print("You have been accepted into the NRPCA!")
            hs = open("Hoops2HS.txt", "r")
            high = hs.read()
            coins += 15
            if score == int(high):
                print("You tied the high score, " + high + " points!")
            elif score > int(high):
                print("You beat the high score of " + high + " points! You received " + str(score) + " points!")
                coins += 35
                hs = open("Hoops2HS.txt", "w")
                hs.write(str(score))
            if coins < 0:
                coins = 0
            screen.fill((0, 255, 0))
            pygame.display.flip()
            sleep(0.1)
            pygame.quit()
            hs.close()
            coin_file.close()
            coin_file = open("coins.txt", "w+")
            coinstr = str(coins)
            coin_file.write(coinstr)
            print("You now have " + str(coins) + " coins!")
            coin_file.close()
            if thanos_ul:
                thanos_ul_file.close()
                thanos_ul_file = open("thanos.txt", "w+")
                thanos_ul_file.write("1")
                thanos_ul_file.close()
            raise SystemExit()
        print("Trial Ended!!!\nUnfortunately, your quality of playing was not satisfactory to the NRPCA and your application has been rejected.\n\nYou may try again in one month.")
        hs = open("Hoops2HS.txt", "r")
        coins -= 50
        high = hs.read()
        if score == int(high):
            print("You tied the high score, " + high + " points!")
        elif score > int(high):
            print("You beat the high score of " + high + " points! You received " + str(score) + " points!")
            coins += 20
            hs.close()
            hs = open("Hoops2HS.txt", "w")
            hs.write(str(score))

        if coins < 0:
            coins = 0
        screen.fill((255, 0, 0))
        pygame.display.flip()
        sleep(0.1)
        pygame.quit()
        hs.close()
        coin_file.close()
        coin_file = open("coins.txt", "w+")
        coinstr = str(coins)
        coin_file.write(coinstr)
        coin_file.close()
        print("You now have " + str(coins) + " coins!")
        if thanos_ul:
            thanos_ul_file.close()
            thanos_ul_file = open("thanos.txt", "w+")
            thanos_ul_file.write("1")
            thanos_ul_file.close()
        raise SystemExit()
    by = 486
    pygame.event.clear()
    screen.blit(ball, (bx, by))
    pygame.display.flip()
