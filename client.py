import pygame
from network import Network
import random

pygame.font.init()
a1 = 0
b1 = 0
c1 = 0
e1 = 0
d = 0
stop = 0
width = 700
height = 700
pole = [(279, 650), (279, 600), (279, 555), (279, 505), (279, 460), (279, 415), (279, 367), (234, 367), (185, 367),
        (139, 367), (93, 367), (45, 367), (0, 367), (0, 320), (0, 274), (45, 274), (93, 274), (139, 274), (185, 274),
        (234, 274), (279, 274), (279, 228), (279, 180), (279, 134), (279, 88), (279, 40), (279, -5), (326, -5),
        (372, -5), (372, 40), (372, 88), (372, 134), (372, 180), (372, 228), (372, 274), (419, 274), (465, 274),
        (512, 274), (559, 274), (606, 274), (653, 274), (653, 320), (653, 367), (606, 367), (559, 367), (512, 367),
        (465, 367), (419, 367), (372, 367), (372, 415), (372, 460), (372, 505), (372, 555), (372, 600), (372, 650),
        (325, 650), (325, 600), (325, 555), (325, 505), (325, 460), (325, 415)]
rx1 = 70
ry1 = 475  # pozycja 1 pionka
rx2 = 163
ry2 = 475  # pozycja 2 pionka
rx3 = 70
ry3 = 570  # pozycja 3 pionka
rx4 = 163
ry4 = 570  # pozycja 4 pionka red
gx1 = 70
gy1 = 55  # pozycja 1 pionka
gx2 = 70
gy2 = 148 # pozycja 2 pionka
gx3 = 163
gy3 = 55  # pozycja 3 pionka
gx4 = 163
gy4 = 148  # pozycja 4 pionka green
yx1 = 488
yy1 = 55  # pozycja 1 pionka
yx2 = 583
yy2 = 148  # pozycja 2 pionka
yx3 = 583
yy3 = 55  # pozycja 3 pionka
yx4 = 488
yy4 = 148 # pozycja 4 pionka yellow
bx1 = 488
by1 = 475  # pozycja 1 pionka
bx2 = 583
by2 = 475  # pozycja 2 pionka
bx3 = 583
by3 = 570  # pozycja 3 pionka
bx4 = 488
by4 = 570  # pozycja 4 pionka blue
r = 0
k1 = 0
k2 = 0
k3 = 0
k4 = 0  # stan wyboru pionka
f1 = 0
f2 = 0
f3 = 0
f4 = 0  # pionki na mapie
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Ludo")


def redrawWindow(win, game,player):
    win.fill((128, 128, 128))
    global rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4, r, a1, k1, k2, b1, k3, k4, c1, e1, stop, f1, f2, f3, f4
    # global d


    ip1 = pygame.image.load("image\\redp.png").convert_alpha()
    ip1 = pygame.transform.scale(ip1, (50, 50))
    ip2 = pygame.image.load("image\\greenp.png").convert_alpha()
    ip2 = pygame.transform.scale(ip2, (50, 50))
    ip3 = pygame.image.load("image\\bluep.png").convert_alpha()
    ip3 = pygame.transform.scale(ip3, (50, 50))
    ip4 = pygame.image.load("image\\yellowp.png").convert_alpha()
    ip4 = pygame.transform.scale(ip4, (50, 50))
    map = pygame.image.load("image\\map1.png").convert_alpha()
    map = pygame.transform.scale(map, (700, 700))
    d0 = pygame.image.load("image\\dice0.png").convert_alpha()
    d1 = pygame.image.load("image\\dice1.png").convert_alpha()
    d2 = pygame.image.load("image\\dice2.png").convert_alpha()
    d3 = pygame.image.load("image\\dice4.png").convert_alpha()
    d4 = pygame.image.load("image\\dice4.png").convert_alpha()
    d5 = pygame.image.load("image\\dice5.png").convert_alpha()
    d6 = pygame.image.load("image\\dice6.png").convert_alpha()
    dice = [d0, d1, d2, d3, d4, d5, d6]
    dice[d] = pygame.transform.scale(dice[d], (50, 50))
    if not (game.connected()):
        font = pygame.font.SysFont("arial", 70)
        text = font.render("Waiting for Players", 1, (255, 0, 0))
        win.blit(text, (50, 200))

    else:
        win.blit(map, (0, 0))
        win.blit(dice[d], (325, 325))
        if d == 6 and r == 0:
            (rx1, ry1) = pole[a1]
            r = r + 1
            stop=0
        print(stop)
        if d >= 1 and r == 1:
            if d == 6:
                if k1 == 1:
                    f1 = 1
                    stop = 0
                    k1 = 0
                if k2 == 1 and not (rx1, ry1) == pole[0] and not (rx3, ry3) == pole[0] and not (rx4, ry4) == pole[0]:
                    (rx2, ry2) = pole[b1]
                    f2 = 1
                    stop = 0
                    k2 = 0
                if k3 == 1 and not (rx1, ry1) == pole[0] and not (rx2, ry2) == pole[0] and not (rx4, ry4) == pole[0]:
                    (rx3, ry3) = pole[c1]
                    f3 = 1
                    stop = 0
                    k3 = 0
                if k4 == 1 and not (rx1, ry1) == pole[0] and not (rx2, ry2) == pole[0] and not (rx3, ry3) == pole[0]:
                    (rx4, ry4) = pole[e1]
                    f4 = 1
                    stop = 0
                    k4 = 0
            else:

                (rx1, ry1) = pole[a1]

        win.blit(ip1, (rx1, ry1))
        win.blit(ip1, (rx2, ry2))
        win.blit(ip1, (rx3, ry3))
        win.blit(ip1, (rx4, ry4))
        win.blit(ip2, (gx1, gy1))
        win.blit(ip2, (gx2, gy2))
        win.blit(ip2, (gx3, gy3))
        win.blit(ip2, (gx4, gy4))
        win.blit(ip3, (bx1, by1))
        win.blit(ip3, (bx2, by2))
        win.blit(ip3, (bx3, by3))
        win.blit(ip3, (bx4, by4))
        win.blit(ip4, (yx1, yy1))
        win.blit(ip4, (yx2, yy2))
        win.blit(ip4, (yx3, yy3))
        win.blit(ip4, (yx4, yy4))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    global player
    player = int(n.getP())
    print("You are player", player)
    global x0
    global d, a1, r, k1, k2, k3, k4, b1, c1, e1, stop
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game,player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    run = False
                if event.key == pygame.K_r and stop == 0:
                    d = random.randint(1, 6)
                    if d == 6:
                        stop = 1
                    if r == 1:
                        a1 = a1 + d
                    if a1 >= 61:
                        a1 = a1 - d
                    if b1 >= 61:
                        b1 = b1 - d
                    if c1 >= 61:
                        c1 = c1 - d
                    if e1 >= 61:
                        e1 = e1 - d
                        print("number is", d)
                if event.key == pygame.K_1:
                    k1 = 1
                if event.key == pygame.K_2:
                    k2 = 1
                if event.key == pygame.K_3:
                    k3 = 1
                if event.key == pygame.K_4:
                    k4 = 1

        redrawWindow(win, game,player )


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("Arial", 60)
        text = font.render("Ludo", 1, (255, 0, 0))
        text1 = font.render("Press to start a game", 1, (255, 0, 0))
        win.blit(text, (270, 200))
        win.blit(text1, (80, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()
