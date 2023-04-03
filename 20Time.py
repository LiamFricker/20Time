import pygame, sys, random
from pygame.locals import *

pygame.init()
screen_width = 419
screen_height = 386

screen = pygame.display.set_mode([screen_width, screen_height])
font = pygame.font.Font('freesansbold.ttf', 20)
font5 = pygame.font.Font('freesansbold.ttf', 25)
fontObj = pygame.font.Font('freesansbold.ttf', 40)
font4 = pygame.font.Font('freesansbold.ttf', 96)
font0 = pygame.font.Font('freesansbold.ttf', 128)
font3 = pygame.font.Font('freesansbold.ttf', 200)
font1 = pygame.font.Font('freesansbold.ttf', 300)
font2 = pygame.font.Font('freesansbold.ttf', 450)

class Player(pygame.sprite.Sprite):
        def __init__(self, img):
        # Call the parent class (Sprite) constructor
            super().__init__()
            if img == "HoraceMann":
                self.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
            elif img == "Betty":
                self.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
            else:
                self.image = pygame.image.load("Pictures/%s.png" % img).convert_alpha()

            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
FPS = 60
scenev = 0
tposx2 = -600
clock = pygame.time.Clock()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE =  (  0,   0, 255)
SBLUE = (  0, 191, 255)
YELLOW = ( 255, 255, 0)
LIME  = (173, 255,  47)
GREEN = (  0, 255,   0)
ORANGE = (255, 165,  0)
PURPLE = (160, 32, 240)
MAGENTA = (255, 0, 255)
textt = -90
fil = 0
one = 1
potl = 3.5
potr = 3.5
potn = 1
posg = -250
pots = 1
potrot = 0
potrotc = 0
pos = [0,0]
pos0 = [418,0]
pos1 = [0, 380]
pos2 = [0, 0]
pos69 = [9999,9999]
post = 200
cposx = 0
cposy = 0
post0 = -100
posh0 = -150
pot = 200
poty = 320
posh = 25
posw = 20
cposh = 386
cposw = 419
rott = 0
bruys = 0
#scene = 0
scene = 0
scenet = 0
sceneu = 0
wpos = 1
wposy = 220
wscene = 0
pow = 144
pow0 = 2
tposx = -1134
tposy = 220
tposx0 = 200
tposy0 = -1000
tposx1 = 200
tposy1 = -1400
randpos = [random.randrange(400),random.randrange(300)]

Thomas = Player("ThomasWalk0") #122, 143
Horace = Player("HoraceMann")
Betty = Player("Betty")
question = Player("Question")
Cave = Player("CaveCollision")
blue = Player("blue")
yellow = Player("yellow")
all_sprites_list = pygame.sprite.Group()
backsprite = pygame.sprite.Group()
all_sprites_list.add(Thomas)
all_sprites_list.add(Horace)
all_sprites_list.add(Betty)
all_sprites_list.add(question)
all_sprites_list.add(blue)
all_sprites_list.add(yellow)
backsprite.add(Cave)

def testtext(text1, text2):
    textSurfaceObj = fontObj.render(str(text1), True, BLACK)
    textSurfaceObj2 = fontObj.render(str(text2), True, RED)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (350, 250)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (350, 275)
    screen.blit(textSurfaceObj, textRectObj)
    screen.blit(textSurfaceObj2, textRectObj2)
def text(text1, ttposx, ttposy, font, trans, color):
    textSurfaceObj = font.render(str(text1), True, color)
    textSurfaceObj = pygame.transform.rotate(textSurfaceObj, int(trans))
    textRectObj = textSurfaceObj.get_rect()

    textRectObj.center = (ttposx, ttposy)
    screen.blit(textSurfaceObj, textRectObj)


def sprpos(name, x, y):
    name.rect.x = x
    name.rect.y = y

sprpos(Horace, -900, 0)
sprpos(Betty, -900, 0)
sprpos(question , 9884, 8439)
sprpos(blue, pos69[0], pos69[1])
sprpos(yellow, pos69[0], pos69[1])

def imag(spr, img):
    if img == "HoraceMann":
                spr.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
    elif img == "Betty":
                spr.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
    else:
                spr.image = pygame.image.load("Pictures/%s.png" % img).convert_alpha()
def trans(spr, rot):
    spr.image = pygame.transform.rotate(spr.image, int(rot))
def dilat(spr, wid, hei):
    spr.image = pygame.transform.scale(spr.image, (int(wid), int(hei)))
def trilat(spr, rot, scl):
    spr.image = pygame.transform.rotozoom(spr.image, rot, scl)
while True:

    if scene == 0:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/WalkCave.png").convert_alpha()
        if wpos <= 172:
            wpos += 2
        if wscene >= 1300 and wscene < 1426:

            tposx += 18
        if wscene >= 1370:
            wpos += 22
        if wscene >= 1380:
            wposy += 24
        if wscene >= 1426:
            tposx += 24


        if wpos >= 173:
            pos[0]-= 2
            pos0[0]-= 2
        if pos[0] <= -418:
            pos[0] = 418
        if pos0[0] <= -418:
            pos0[0] = 418
        wscene += 2
#Make everything faster
        sprpos(Thomas, wpos, wposy)
        if wscene % pow == 0:
            imag(Thomas, "ThomasWalk0")
        if wscene % pow == pow/6:
            imag(Thomas, "ThomasWalk1")
        if wscene % pow == pow/3:
            imag(Thomas, "ThomasWalk3")
        if wscene % pow == pow/2:
            imag(Thomas, "ThomasWalk4")
        if wscene % pow == pow/1.5:
            imag(Thomas, "ThomasWalk5")
        if wscene % pow == pow/1.2:
            imag(Thomas, "ThomasWalk6")

        screen.blit(background, pos)

        if wscene >= 1426:
            background = pygame.image.load("Pictures/WalkCaveEnd0.png").convert_alpha()
            screen.blit(background, pos)
            pow = 36
            pow0 = 24

        if wscene >= 1050:
            background = pygame.image.load("Pictures/WalkCaveEnd.png").convert_alpha()
            pow = 72
            pow0 = 4
            #make it so Thomas walks faster and gets pushed off


        screen.blit(background, pos0)
        if wscene >= 1300:
            text("U.S. Education Sucks!", tposx, tposy, font0, 0, RED)
        testtext(wpos, wscene)
        if wscene == 1520:
            scene = 1
        #1520 is wscene where Thomas falls off.  Need new background for pos after that.


    if scene == 1:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/20Fall0.png").convert_alpha()
        imag(Thomas, "Thomas")
        rott += 2
        scenet += 2
        pos2[1] -= 10
        pos1[1] -= 10
        post += 2
        if scenet <= 950:
            if post >= 386:
                post = -122
        if pos2[1] <= -380:
            pos2[1] = 380
        if pos1[1] <= -380:
            pos1[1] = 380
        #if posh >= 386:
            #posh = -122
        imag(Thomas, "Thomas")
        trans(Thomas, rott)
        screen.blit(background, pos2)
        screen.blit(background, pos1)
        sprpos(Thomas, 137.5, post)
        testtext(scenet, scenet)
        if scenet >= 775:
            imag(Horace, "HoraceMann")
            trans(Horace, rott)
            sprpos(Horace, 25, posg)
            imag(Betty, "Betty")
            trans(Betty, -rott)
            sprpos(Betty, 250, posg)
            posg += 2
            #check scenet
        if scenet >= 1500:
            text("U.S. Education Sucks!", tposx0, tposy0, font1, -90, RED)
            tposy0 += 50
        if scenet >= 1650:
            scene = 2
            pos = (0,0)

    if scene >= 2 and scene < 3:
        background = pygame.image.load("Pictures/WalkCave.png").convert_alpha()
        Bruy = pygame.image.load("Pictures/Bury.png").convert_alpha()
        imag(Thomas, "ThomasFall")
        imag(Horace, "HoraceMann")
        sprpos(Horace, 25, posh0)
        imag(Betty, "Betty")
        sprpos(Betty, 250, posh0)
        sprpos(Thomas, 137.5, post0)
        if sceneu >= 280:
            imag(Thomas, "ThomasFall0")
        else:
            post0 += 3
        if sceneu >= 292 and scene == 2:
            imag(Thomas, "ThomasFall1")
        if scene == 2.1:
            imag(Thomas, "ThomasLook")
            scenev += 1


        if scenev >= 90:
            scene = 4
            pos = [0,0]
            pos0 = [-500,0]
            tposx = 2000
        if sceneu >= 300 and scene == 2:
            scene = 3
        if scene >= 2 and scene < 3:
            bruys = 1

        if posh0 <= 180:
            posh0 += 4
        sceneu += 3


#Make thomas a little bit bigger and more down during 2.1

        testtext(sceneu, posh0)
        screen.blit(background, pos)


    if scene == 3:
        screen.fill(WHITE)
        bruys = 0
        sprpos(Horace, 25000, posh0)

        sprpos(Betty, 25000, posh0)
        sprpos(Thomas, 13700.5, post0)
        background = pygame.image.load("Pictures/20Fall.png").convert_alpha()

        tposy1 += 2.5
        if pos2[1] <= -350:
            pos2[1] = 350
        if pos1[1] <= -350:
            pos1[1] = 350
        pos2[1] -= 50
        pos1[1] -= 50
        screen.blit(background, pos2)
        screen.blit(background, pos1)
        text("U.S. Education Sucks!", tposx1, tposy1, font1, -90, RED)
        testtext(tposy1, pos1)
        if tposy1 >= -1000:
            scene = 2.1
        #if scenet =
    if scene == 4:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/WalkCave2.png").convert_alpha()
        bruys = 0
        sprpos(Horace, 25000, posh0)

        sprpos(Betty, 25000, posh0)
        sprpos(Thomas, 13700.5, post0)
        pos[0]+= 50
        pos0[0]+= 50
        if pos[0] >= 500:
            pos[0] = -500
        if pos0[0] >= 500:
            pos0[0] = -500
#Stretch Walk Cave
        tposx -= 50
        screen.blit(background, pos)
        screen.blit(background, pos0)
        text("20TIME!", tposx, tposy, font2, 0, GREEN)
        if tposx <= 0:
            scene = 5
            pos = [0,0]
            pos0 = [-500,0]
            tposx = 1419
            tposy1 = -1000
            wscene =0
            pow = 72
    if scene == 5:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/CaveCollision.png").convert_alpha()
        sprpos(Thomas, pot, poty)
        if tposx > -700:
            imag(Thomas, "ThomasLook")
            trans(Thomas, potrot)


        imag(Cave, "CaveCollision")
        trans(Cave, potrotc)
        dilat(Cave, cposw, cposh)
        dilat(Thomas, posw, posh)


        sprpos(Cave, cposx, cposy)
        #Check thomas
        bruys = 0
#tposx 419, tposy1 0
        if tposy1 >= 0:
            textt -= 5
            tposy1 -= 5
            tposx1 -= 5
        else:
            tposy1 += 10
        tposx -= 10


        if tposx <= -700:


            if wscene <= 230:
                posw *= 1.01
                posh *= 1.01
                pot += potn
                poty -= pots/1.5
                potn *= 1.015
                pots *= 1.0001
                wscene += 2
                #potrot += 0.025
                if wscene % pow == 0:
                    imag(Thomas, "ThomasRun")
                    trans(Thomas, potrot)
                if wscene % pow == pow/6:
                    imag(Thomas, "ThomasRun0")
                    trans(Thomas, potrot)
                if wscene % pow == pow/3:
                    imag(Thomas, "ThomasRun1")
                    trans(Thomas, potrot)
                if wscene % pow == pow/2:
                    imag(Thomas, "ThomasRun2")
                    trans(Thomas, potrot)
                if wscene % pow == pow/1.5:
                    imag(Thomas, "ThomasRun3")
                    trans(Thomas, potrot)
                if wscene % pow == pow/1.2:
                    imag(Thomas, "ThomasRun4")
                    trans(Thomas, potrot)
                dilat(Thomas, posw, posh)
                cposw *= 1.01
                cposh *= 1.01
                potl *= 1.011
                potr *= 1.01
                cposx -= potl
                cposy -= potr
                font1 = pygame.font.Font('freesansbold.ttf', 300)
                tposy1 = 0
                tposx2 += 20
                #potrotc += 0.05
            else:
                scene = 6
                pot = 20
                poty = 420
                sprpos(Thomas, pot, poty)
                potrot = 0
                wscene = 0
                tposy = 190
                scenet = 0
                tposx = -700
                tposx1 = 1115
                tposy1 = 75
        screen.blit(background, pos69)
        backsprite.draw(screen)
        text("U.S. Education Sucks!", tposx1, tposy1, fontObj, textt, RED)
        text("20TIME!", tposx, tposy, font0, 0, GREEN)
        if tposx <= -700:
            text("20TIME!", tposx2, tposy1, font3, 0, GREEN)
        testtext(wscene, tposx)
    if scene == 6:
        screen.fill(WHITE)

        imag(Thomas, "ThomasFall")
        sprpos(Thomas, pot, poty)
        if scenet == 0:
            background = pygame.image.load("Pictures/CaveFinal.png").convert_alpha()
            pot += 1.45
            poty -= 2.1
            potrot += 12
            trans(Thomas, potrot)
            wscene += 2
            tposx += 10
            tposx1 -= 10
            if wscene == 180:
                scenet = 1
        if scenet == 1:
            background = pygame.image.load("Pictures/IntroFinal.png").convert_alpha()
            wscene += 2
        if wscene == 250:
            scenef = 0
            scene = 7
            FPS = 15


        screen.blit(background, pos)
        testtext(wscene, potrot)


        text("20", tposx1, tposy1, font0, 0, BLUE)
        text("TIME!", tposx, tposy, font4, 0, BLUE)
    if scene == 7:
        if wscene == 250:
            wscene += 1
            screen.fill(WHITE)
            sprpos(Thomas, pos69[0], pos69[1])
        randpos = [random.randrange(400),random.randrange(300)]
        imag(question, "Question")
        if scenef % 30 == 10 or scenef % 30 == 20:
            #39, 89
            dilat(question, 78, 178)
            randpos = [random.randrange(100 , 261),random.randrange(11 , 111)]
        if scenef % 30 == 28:
            #39, 89
            dilat(question, 107, 267)
            randpos = [random.randrange(113 , 180),random.randrange(9, 40)]
        scenef += 1
        sprpos(question, randpos[0], randpos[1])
        if scenef >= 62:
            scene = 8
            wscene = 0
            FPS = 60
    if scene == 8:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/Board.png").convert_alpha()
        indepen = pygame.image.load("Pictures/indepen.png").convert_alpha()
        imagine = pygame.image.load("Pictures/imagine.png").convert_alpha()
        illimit = pygame.image.load("Pictures/illimit.png").convert_alpha()
        sprpos(question, pos69[0], pos69[1])
        sprpos(Thomas, 150, 180)
        imag(Thomas, "teachthomas")
        wscene += 1

        screen.blit(background, pos)
        testtext(wscene, None)

        if wscene >= 90:
            screen.blit(indepen, (80, 100))
        if wscene >= 120:
            screen.blit(imagine, (180, 100))
        if wscene >= 150:
            screen.blit(illimit, (280, 100))
        if wscene >= 300:
            scene = 9
            cposx = 200
            cposy = 250
            red = 255
            gre = 255
            blu = 0
            BLUE = (red, gre, blu)
            wscene = 0
    if scene == 9:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/indeback.png").convert_alpha()
        sprpos(Thomas, pos69[0], pos69[1])
        #sprpos(blue, cposx, cposy)
        BLUE = (red, gre, blu)

        if wscene < 255:
            red -= 1
            blu += 1
            gre -= 1
            if wscene % 5 == 0:
                cposx += 1
                cposy -= 1


        wscene += 1

        #sprpos(yellow, 160, 90)
        #make a sprite for this, don't use draw.


        screen.blit(background, pos)
        pygame.draw.circle(screen, BLUE, (cposx, cposy), 14, 0)
        testtext(wscene, red)
        if wscene >= 300:
            scene = 10
            screen.fill(WHITE)
            rposx = 36
            rposx0 = 200
            rposx1 = 225
            rposx2 = 250
            rposx3 = 275
            rposx4 = 300
            rposx5 = 325
            rposx6 = 350
            rposx7 = 375
            one = 1.5
            blok = 20
            bup = 0.9775
            rposy = one * 2
            rposxx = 363
            screen.fill(SBLUE)
            wscene = 0
            hei = 419 * 1.1
            leng = 386 * 1.1
            circle = pygame.image.load("Pictures/white.png").convert_alpha()



    if scene == 10:
        background = pygame.image.load("Pictures/imagback.png").convert_alpha()
        border = pygame.image.load("Pictures/border.png").convert_alpha()
        #circle = pygame.transform.scale(circle, (int(hei), int(leng)))

        wscene += 1
        blok += 1/30
        if wscene < 10:
            rposx += 0.10
            rposxx -= 0.10
        if wscene <= 162 and wscene >= 10:
            rposx += 1
            rposxx -= 1

        if wscene <= 17 and wscene >= 10:
            rposy *= 0.9775
            #rposy *= bup
        elif wscene <= 40 and wscene > 10:
            #rposy *= 0.964
            rposy *= 0.98
        elif wscene <= 65:
            rposy *= 0.98
        elif wscene <= 100:
            rposy *= 0.98
            #rposy *= 0.972

        elif wscene <= 130:
            rposy *= 0.9775
        elif wscene <= 155:
            rposy *= 0.975


        elif wscene == 162:
            rposy = 0
            blok = 25
        if wscene >= 200:
            scene = 11
            bhei = 84
            bwid = 11

            bposx = 170
            bposy = 100
            #bposx0 = 198
            bposy0 = 18
            wscene = 0
            bpop = 0
            boop = 0
            urot = 0
            urot0 = 270
            urot1 = 90
            bop = 1
            wuser = 1
            wuser0 = 1
            wuser1 = 1
            shop = 25
            huser = 1
            huser0 = 1
            huser1 = 1
            top = 1.5



        '''
        if wscene == 168:
            rposy = -0.0625
        if wscene == 192:
            rposy= -0.125
        if wscene == 216:
            rposy= -0.25
        if wscene == 240:
            rposy = -0.5
        if wscene == 264:
            rposy = -1
        if wscene == 288:
            rposy = -2
        if wscene == 312:
            rposy = 0
        '''

        rposx0 -= rposy
        rposx1 -= rposy
        rposx2 -= rposy
        rposx3 -= rposy
        rposx4 -= rposy
        rposx5 -= rposy
        rposx6 -= rposy
        rposx7 -= rposy


        pygame.draw.rect(screen, RED, (rposx, rposx0, 20, blok))
        pygame.draw.rect(screen, ORANGE, (rposx, rposx1, 20, blok))
        pygame.draw.rect(screen, YELLOW, (rposx, rposx2, 20, blok))
        pygame.draw.rect(screen, GREEN, (rposx, rposx3, 20, blok))
        pygame.draw.rect(screen, BLUE, (rposx, rposx4, 20, blok))
        pygame.draw.rect(screen, PURPLE, (rposx, rposx5, 20, blok))
        pygame.draw.rect(screen, MAGENTA, (rposx, rposx6, 20, blok))
        pygame.draw.rect(screen, SBLUE, (rposx, rposx7, 20, blok))

        pygame.draw.rect(screen, RED, (rposxx, rposx0, 20, blok))
        pygame.draw.rect(screen, ORANGE, (rposxx, rposx1, 20, blok))
        pygame.draw.rect(screen, YELLOW, (rposxx, rposx2, 20, blok))
        pygame.draw.rect(screen, GREEN, (rposxx, rposx3, 20, blok))
        pygame.draw.rect(screen, BLUE, (rposxx, rposx4, 20, blok))
        pygame.draw.rect(screen, PURPLE, (rposxx, rposx5, 20, blok))
        pygame.draw.rect(screen, MAGENTA, (rposxx, rposx6, 20, blok))
        pygame.draw.rect(screen, SBLUE, (rposxx, rposx7, 20, blok))

        #pygame.draw.ellipse(screen, BLACK, (0, 0, 419, 386), 50)

        screen.blit(border, pos)
        screen.blit(circle, (0,0))
        textSurfaceObj = fontObj.render(str(wscene), True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        pygame.draw.rect(screen, WHITE, (300, 225, 100, 70))

        testtext(wscene, rposx)



        #implement the border

    '''

        backsprite.draw(screen)
        text("U.S. Education Sucks!", tposx1, tposy1, fontObj, textt)
        text("20TIME!", tposx, tposy, font0, 0)
        if tposx <= -700:
            text("20TIME!", tposx2, tposy1, font3, 0)
        testtext(wscene, tposx)
    '''
    if scene == 11:
        #something
        screen.fill(WHITE);
        background = pygame.image.load("Pictures/cranegame.png").convert_alpha()
        background0 = pygame.image.load("Pictures/cranegame0.png").convert_alpha()
        sthomas = pygame.image.load("Pictures/stuffedthomas.png").convert_alpha()
        sjames = pygame.image.load("Pictures/stuffedjames.png").convert_alpha()
        sthomas0 = pygame.transform.rotate(sthomas, 350)
        sthomas1 = pygame.transform.rotate(sthomas, 10)
        sthomas2 = pygame.transform.rotate(sthomas, 20)
        sthomas3 = pygame.transform.rotate(sthomas, 340)
        sthomas4 = pygame.transform.rotate(sthomas, 30)
        sjames0 = pygame.transform.rotate(sjames, 350)
        sjames1 = pygame.transform.rotate(sjames, 10)
        sjames2 = pygame.transform.rotate(sjames, 20)
        sjames3 = pygame.transform.rotate(sjames, 340)
        sjames4 = pygame.transform.rotate(sjames, 330)
        claw = pygame.image.load("Pictures/claw.png").convert_alpha()
        clawarm = pygame.image.load("Pictures/clawarm.png").convert_alpha()
        clawarm = pygame.transform.scale(clawarm, (int(bwid), int(bhei)))
        clawfing = pygame.image.load("Pictures/clawfing.png").convert_alpha()

        suser = pygame.image.load("Pictures/suser.png").convert_alpha()
        ruser = suser.get_rect()
        suser = pygame.transform.scale(suser, (int(wuser), int(huser)))
        suser = pygame.transform.rotate(suser, urot)
        suser0 = pygame.image.load("Pictures/suser0.png").convert_alpha()
        ruser0 = suser0.get_rect()
        suser0 = pygame.transform.scale(suser0, (int(wuser0), int(huser0)))
        suser0 = pygame.transform.rotate(suser0, urot0)
        suser1 = pygame.image.load("Pictures/suser1.png").convert_alpha()
        ruser1 = suser1.get_rect()
        suser1 = pygame.transform.scale(suser1, (int(wuser1), int(huser1)))
        suser1 = pygame.transform.rotate(suser1, urot1)

#50,60,90,110,120,130,160,170,180,190
#Convert it to the user one

        screen.blit(background0, pos)

        screen.blit(clawfing, (bposx + 1, bposy - 1))

        if boop >= 1 and bop < 10:
            screen.blit(suser1, (bposx + shop - 20, bposy + shop + 5))
            screen.blit(suser, (bposx + shop, bposy + shop + 15))
            screen.blit(suser0, (bposx + shop, bposy + shop + 15))

        screen.blit (sjames0, (160, 200))
        screen.blit (sjames1, (120, 200))
        screen.blit (sthomas3, (170, 200))
        screen.blit (sthomas1, (110, 200))
        screen.blit (sthomas0, (90, 200))
        screen.blit (sjames4, (130, 200))
        screen.blit (sthomas, (190, 200))
        screen.blit (sjames2, (50, 200))
        screen.blit (sjames3, (60, 200))
        screen.blit (sthomas2, (180, 200))
        screen.blit (sthomas4, (240, 200))
        screen.blit (sjames, (270, 200))

        screen.blit (sjames0, (200, 200))
        screen.blit (sjames1, (220, 200))
        screen.blit (sthomas3, (210, 200))
        screen.blit (sthomas1, (300, 200))
        screen.blit (sthomas0, (260, 200))
        screen.blit (sjames4, (250, 200))
        screen.blit (sthomas, (240, 200))
        screen.blit (sjames2, (290, 200))
        screen.blit (sjames3, (230, 200))
        screen.blit (sthomas2, (280, 200))
        screen.blit (sthomas4, (240, 200))
        screen.blit (sjames, (270, 200))
        screen.blit(background, pos)

        screen.blit(claw, (bposx, bposy))
        screen.blit(clawarm, (bposx + 28, bposy0))
        if bop >= 10:
            screen.blit(suser1, (bposx + shop - 20, bposy + shop + 5))
            screen.blit(suser, (bposx + shop, bposy + shop + 15))
            screen.blit(suser0, (bposx + shop, bposy + shop + 15))






        if wscene <= 76 and boop == 0:
            if wscene <= 15:
                bposx += 2
            if wscene >= 38:
                bposy += 2
                bhei += 2
        if wscene >= 85:
            boop += 1

            wuser = ruser.width
            wuser0 = ruser0.width
            wuser1 = ruser1.width

            huser = ruser.height
            huser0 = ruser0.height
            huser1 = ruser1.height
        if boop >= 1:
            wscene -= 1

            if wscene <= 24 and wscene >= 9:
                bposx -= 2
            if wscene >= 47:
                bposy -= 2
                bhei -= 2
            if wscene < 9 and boop >= 1:
                wuser *= 1.05
                wuser0 *= 1.05
                wuser1 *= 1.05
                huser *= 1.05
                huser0 *= 1.05
                huser1 *= 1.05
                ruser.width = wuser
                ruser0.width = wuser0
                ruser1.width = wuser1
                ruser.height = huser
                ruser0.height = huser0
                ruser1.height = huser1
                #ruse.width and stuff to morth the things to get big and rotate
                shop -= top
                top *= 1.04

                urot += 4
                urot0 += 4
                urot1 += 4

                bop += 1
        else:
            wscene += 1
        if wscene == -58:
            scene = 12
            wscene = 0

        testtext(wscene, wuser)
    if scene == 12:
        user = pygame.image.load("Pictures/user.jpg").convert_alpha()
        user0 = pygame.image.load("Pictures/user0.jpg").convert_alpha()
        user1 = pygame.image.load("Pictures/user1.png").convert_alpha()
        wscene += 1
        if wscene <= 200:
            background = user
        elif wscene <= 400 and wscene > 200:
            background = user0
        elif wscene <= 600 and wscene > 400:
            background = user1
        elif wscene <= 800 and wscene > 600:
            scene = 13
        screen.blit(background, pos)
    if scene == 13:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/Board.png").convert_alpha()

        screen.blit(background, pos)
        text("Wow! Someone actually watched this,", 215, 150, font, 0, BLACK)
        text("Tysm! Lik and subsrib", 215, 250, font5, 0, BLACK)
        text("Check desc if you're curious", 215, 350, font, 0, BLACK)


    clock.tick(FPS)


    all_sprites_list.draw(screen)
    if scene == 2.1:
        testtext(scenev, None)
    if bruys == 1:
            screen.blit(Bruy, (25, 320))
            screen.blit(Bruy, (250, 320))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


