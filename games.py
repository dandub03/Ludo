import pygame
import random
import pickle
import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.24"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 4))
        except socket.error as e:
            print(e)

    def sendsync(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

pygame.font.init()

a1 = [0, 0, 0, 0]
b1 = [0, 0, 0, 0]
c1 = [0, 0, 0, 0]
e1 = [0, 0, 0, 0]
d = [0, 0, 0, 0]
drys = [0, 0, 0, 0]
stop = 0
width = 900
height = 700
pole = [[(279, 650), (279, 600), (279, 555), (279, 505), (279, 460), (279, 415), (279, 367), (234, 367), (185, 367),
         (139, 367), (93, 367), (45, 367), (0, 367), (0, 320), (0, 274), (45, 274), (93, 274), (139, 274), (185, 274),
         (234, 274), (279, 274), (279, 228), (279, 180), (279, 134), (279, 88), (279, 40), (279, -5), (326, -5),
         (372, -5), (372, 40), (372, 88), (372, 134), (372, 180), (372, 228), (372, 274), (419, 274), (465, 274),
         (512, 274), (559, 274), (606, 274), (653, 274), (653, 320), (653, 367), (606, 367), (559, 367), (512, 367),
         (465, 367), (419, 367), (372, 367), (372, 415), (372, 460), (372, 505), (372, 555), (372, 600), (372, 650),
         (325, 650), (325, 600), (325, 555), (325, 505), (325, 460), (325, 415)],
        [(0, 274), (45, 274), (93, 274), (139, 274), (185, 274),
         (234, 274), (279, 274), (279, 228), (279, 180), (279, 134), (279, 88), (279, 40), (279, -5), (326, -5),
         (372, -5), (372, 40), (372, 88), (372, 134), (372, 180), (372, 228), (372, 274), (419, 274), (465, 274),
         (512, 274), (559, 274), (606, 274), (653, 274), (653, 320), (653, 367), (606, 367), (559, 367), (512, 367),
         (465, 367), (419, 367), (372, 367), (372, 415), (372, 460), (372, 505), (372, 555), (372, 600), (372, 650),
         (325, 650), (279, 650), (279, 600), (279, 555),
         (279, 505), (279, 460), (279, 415), (279, 367), (234, 367), (185, 367), (139, 367), (93, 367), (45, 367),
         (0, 367), (0, 320), (45, 320), (93, 320), (139, 320), (185, 320), (234, 320)],
        [(372, -5), (372, 40), (372, 88), (372, 134), (372, 180), (372, 228), (372, 274), (419, 274), (465, 274),
         (512, 274), (559, 274), (606, 274), (653, 274), (653, 320), (653, 367), (606, 367), (559, 367), (512, 367),
         (465, 367), (419, 367), (372, 367), (372, 415), (372, 460), (372, 505), (372, 555), (372, 600), (372, 650),
         (325, 650), (279, 650), (279, 600), (279, 555),
         (279, 505), (279, 460), (279, 415), (279, 367), (234, 367), (185, 367), (139, 367), (93, 367), (45, 367),
         (0, 367), (0, 320), (0, 274), (45, 274), (93, 274),
         (139, 274), (185, 274), (234, 274), (279, 274), (279, 228), (279, 180), (279, 134), (279, 88), (279, 40),
         (279, -5), (326, -5), (326, 40), (326, 88), (326, 134), (326, 180), (326, 228)],
        [(653, 367), (606, 367), (559, 367), (512, 367), (465, 367), (419, 367), (372, 367), (372, 415), (372, 460),
         (372, 505), (372, 555), (372, 600), (372, 650), (325, 650), (279, 650), (279, 600), (279, 555), (279, 505),
         (279, 460), (279, 415), (279, 367), (234, 367), (185, 367), (139, 367), (93, 367), (45, 367), (0, 367),
         (0, 320), (0, 274), (45, 274), (93, 274), (139, 274), (185, 274), (234, 274), (279, 274),
         (279, 228), (279, 180), (279, 134), (279, 88), (279, 40), (279, -5), (326, -5), (372, -5), (372, 40),
         (372, 88), (372, 134), (372, 180), (372, 228), (372, 274), (419, 274), (465, 274), (512, 274), (559, 274),
         (606, 274), (653, 274), (653, 320), (606, 320), (559, 320), (512, 320), (465, 320), (419, 320)]]
xy1 = [(70, 475), (70, 55), (488, 55), (488, 475)]
xy2 = [(163, 475), (70, 148), (583, 148), (583, 475)]
xy3 = [(70, 570), (163, 55), (583, 55), (583, 570)]
xy4 = [(163, 570), (163, 148), (488, 148), (488, 570)]
r = [0, 0, 0, 0]
k1 = [0, 0, 0, 0]
k2 = [0, 0, 0, 0]
k3 = [0, 0, 0, 0]
k4 = [0, 0, 0, 0]  # stan wyboru pionka
f1 = [0, 0, 0, 0]
f2 = [0, 0, 0, 0]
f3 = [0, 0, 0, 0]
f4 = [0, 0, 0, 0]  # pionki na mapie
turn = 0
xystart = [[(70, 475), (163, 475), (70, 570), (163, 570)], [(70, 55), (70, 148), (163, 55), (163, 148)],
           [(488, 55), (583, 148), (583, 55), (488, 148)], [(488, 475), (583, 475), (583, 570), (488, 570)]] # Pozycje startowe pionków
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# Zakoduj współrzędne na indexy i dodaj kość i oznaczenie typu danych
def makesync(player):
    pos = []
    if xy1[player] in xystart[player]:
        pos.append('start')
    else:
        pos.append(pole[player].index(xy1[player]))
    if xy2[player] in xystart[player]:
        pos.append('start')
    else:
        pos.append(pole[player].index(xy2[player]))
    if xy3[player] in xystart[player]:
        pos.append('start')
    else:
        pos.append(pole[player].index(xy3[player]))
    if xy4[player] in xystart[player]:
        pos.append('start')
    else:
        pos.append(pole[player].index(xy4[player]))
    pos = pos + [d[player]]
    return 'S'+','+str(pos[0]) + ',' + str(pos[1]) + ',' + str(pos[2]) + ',' + str(pos[3]) + ',' + str(pos[4])
# Rozkoduj współrzędne i wstaw do matryc, musi być warunkowe żęby uwzględnić gracza
# Decode index positions to coordinates
def indexdecode(data, p):
    temp = [0, 0, 0, 0]
    for i in range(4):
        if data[i] == 'start':
            temp[i] = xystart[p][i]
        else:
            temp[i] = pole[p][int(data[i])]
    return temp
# Insert into list
def insrt(data,player):
    xy1[player] = data[0]
    xy2[player] = data[1]
    xy3[player] = data[2]
    xy4[player] = data[3]

def insrtind(data, player):
    if data[0] == 'start':
        a1[player] = 0
    else:
        a1[player] = int(data[0])
    if data[1] == 'start':
        b1[player] = 0
    else:
        b1[player] = int(data[1])
    if data[2] == 'start':
        c1[player] = 0
    else:
        c1[player] = int(data[2])
    if data[3] == 'start':
        e1[player] = 0
    else:
        e1[player] = int(data[3])

# insert received data into the lists
def insertdata(data, player):
    datalist = data.split(',')
    p1 = datalist[:4]
    p2 = datalist[4:8]
    p3 = datalist[8:12]
    p4 = datalist[12:16]
    dice = list(map(int,datalist[16:])) # No decoding needed, just changing type from str to int
    #Decode indexes into coordinates
    p1d = indexdecode(p1,0)
    p2d = indexdecode(p2,1)
    p3d = indexdecode(p3,2)
    p4d = indexdecode(p4,3)
    # Insert dice
    # for i in range(4):
    #     if i != player:
    #         d[i] = dice[i]
    # Insert positions and indexes
    if player == 0:
        insrt(p2d, 1)
        insrt(p3d, 2)
        insrt(p4d, 3)

        insrtind(p2, 1)
        insrtind(p3, 2)
        insrtind(p4, 3)
    elif player == 1:
        insrt(p1d, 0)
        insrt(p3d, 2)
        insrt(p4d, 3)

        insrtind(p1, 0)
        insrtind(p3, 2)
        insrtind(p4, 3)
    elif player == 2:
        insrt(p1d, 0)
        insrt(p2d, 1)
        insrt(p4d, 3)

        insrtind(p1, 0)
        insrtind(p2, 1)
        insrtind(p4, 3)
    elif player == 3:
        insrt(p1d, 0)
        insrt(p2d, 1)
        insrt(p3d, 2)

        insrtind(p1, 0)
        insrtind(p2, 1)
        insrtind(p3, 2)



class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 175
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("arial", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redrawWindow(win, game, p):
    global xy1, xy2, xy3, xy4, r, a1, k1, k2, b1, k3, k4, c1, e1, f1, f2, f3, f4, turn, drys  # ,stop
    global d
    win.fill((128, 128, 128))
    map = pygame.image.load("image\\map1.png").convert_alpha()
    map = pygame.transform.scale(map, (700, 700))
    ip1 = pygame.image.load("image\\redp.png").convert_alpha()
    ip1 = pygame.transform.scale(ip1, (50, 50))
    ip2 = pygame.image.load("image\\greenp.png").convert_alpha()
    ip2 = pygame.transform.scale(ip2, (50, 50))
    ip3 = pygame.image.load("image\\yellowp.png").convert_alpha()
    ip3 = pygame.transform.scale(ip3, (50, 50))
    ip4 = pygame.image.load("image\\bluep.png").convert_alpha()
    ip4 = pygame.transform.scale(ip4, (50, 50))
    d0 = pygame.image.load("image\\dice0.png").convert_alpha()
    d1 = pygame.image.load("image\\dice1.png").convert_alpha()
    d2 = pygame.image.load("image\\dice2.png").convert_alpha()
    d3 = pygame.image.load("image\\dice3.png").convert_alpha()
    d4 = pygame.image.load("image\\dice4.png").convert_alpha()
    d5 = pygame.image.load("image\\dice5.png").convert_alpha()
    d6 = pygame.image.load("image\\dice6.png").convert_alpha()
    ramka = pygame.image.load("image\\ramka.png").convert_alpha()
    turnfont = pygame.font.SysFont("Arial", 30)
    turntext = turnfont.render("Player " + str(turn+1) + " turn", 1, (0, 0, 0))
    dice = [d0, d1, d2, d3, d4, d5, d6]
    dice[drys[p]] = pygame.transform.scale(dice[drys[p]], (50, 50))
    print(d[0], d[1], k1[p], f1[p], r[p], p, a1[p], b1[p], c1[p], e1[p])
    if not (game.connected()):
        font = pygame.font.SysFont("arial", 70)
        text = font.render("Waiting for Players", 1, (255, 0, 0))
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    else:
        win.blit(map, (0, 0))
        win.blit(dice[drys[p]], (325, 325))
        win.blit(ip1, (xy1[0]))
        win.blit(ip1, (xy2[0]))
        win.blit(ip1, (xy3[0]))
        win.blit(ip1, (xy4[0]))
        win.blit(ip2, (xy1[1]))
        win.blit(ip2, (xy2[1]))
        win.blit(ip2, (xy3[1]))
        win.blit(ip2, (xy4[1]))
        win.blit(ip3, (xy1[2]))
        win.blit(ip3, (xy2[2]))
        win.blit(ip3, (xy3[2]))
        win.blit(ip3, (xy4[2]))
        win.blit(ip4, (xy1[3]))
        win.blit(ip4, (xy2[3]))
        win.blit(ip4, (xy3[3]))
        win.blit(ip4, (xy4[3]))
        btn1.draw(win)
        btn2.draw(win)
        btn3.draw(win)
        btn4.draw(win)
        btn5.draw(win)
        if f1[p] == 1:
            win.blit(ramka, (703, 47))
        if f2[p] == 1:
            win.blit(ramka, (703, 172))
        if f3[p] == 1:
            win.blit(ramka, (703, 297))
        if f4[p] == 1:
            win.blit(ramka, (703, 422))
        if p == turn:
            win.blit(turntext, (710, 10))

    pygame.display.update()


btn1 = Button("1st Piece", 710, 50, (0, 0, 0))
btn2 = Button("2nd Piece", 710, 175, (0, 0, 0))
btn3 = Button("3rd Piece", 710, 300, (0, 0, 0))
btn4 = Button("4th Piece", 710, 425, (0, 0, 0))
btn5 = Button("Roll Dice", 710, 550, (0, 0, 0))

def updatepos(p):
    if k1[p] == 1:
        xy1[p] = pole[p][a1[p]]

    if k2[p] == 1:
        xy2[p] = pole[p][b1[p]]

    if k3[p] == 1:
        xy3[p] = pole[p][c1[p]]

    if k4[p] == 1:
        xy4[p] = pole[p][e1[p]]

def makemove(p):
    global xy1, xy2, xy3, xy4, r, a1, k1, k2, b1, k3, k4, c1, e1, f1, f2, f3, f4, turn  # ,stop
    global d
    if k1[p] == 1 and f1[p] == 1:
        r[p] = 1

        # stop = 0
    if k2[p] == 1 and f2[p] == 1:
        r[p] = 2

        # stop = 0
    if k3[p] == 1 and f3[p] == 1:
        r[p] = 3

        # stop = 0
    if k4[p] == 1 and f4[p] == 1:
        r[p] = 4

        # stop = 0
    if d[p] == 6:
        r[p] = 0

    if f1[p] == 1 and not xy2[p] == pole[p][0] and not xy3[p] == pole[p][0] and not xy4[p] == pole[p][0] \
            and d[p] == 6 and k1[p] == 0:
        xy1[p] = pole[p][a1[p]]
        k1[p] = 1
        f1[p] = 0
        # stop = 0
    if f2[p] == 1 and not xy1[p] == pole[p][0] and not xy3[p] == pole[p][0] and not xy4[p] == pole[p][0] \
            and d[p] == 6 and k2[p] == 0:
        xy2[p] = pole[p][b1[p]]
        k2[p] = 1
        f2[p] = 0
        # stop = 0
    if f3[p] == 1 and not xy1[p] == pole[p][0] and not xy2[p] == pole[p][0] and not xy4[p] == pole[p][0] \
            and d[p] == 6 and k3[p] == 0:
        xy3[p] = pole[p][c1[p]]
        k3[p] = 1
        f3[p] = 0
        # stop = 0
    if f4[p] == 1 and not xy1[p] == pole[p][0] and not xy2[p] == pole[p][0] \
            and not xy3[p] == pole[p][0] and d[p] == 6 and k4[p] == 0:
        xy4[p] = pole[p][e1[p]]
        k4[p] = 1
        f4[p] = 0
        # stop = 0
    if k1[p] == 1:
        xy1[p] = pole[p][a1[p]]

    if k2[p] == 1:
        xy2[p] = pole[p][b1[p]]

    if k3[p] == 1:
        xy3[p] = pole[p][c1[p]]

    if k4[p] == 1:
        xy4[p] = pole[p][e1[p]]

def wincheck():
    winner = 69
    if xy1[0] in pole[0][57:] and xy2[0] in pole[0][57:] and xy3[0] in pole[0][57:] and xy4[0] in pole[0][57:]:
        winner = 0
    if xy1[1] in pole[1][57:] and xy2[1] in pole[1][57:] and xy3[1] in pole[1][57:] and xy4[1] in pole[1][57:]:
        winner = 1
    if xy1[2] in pole[2][57:] and xy2[2] in pole[2][57:] and xy3[2] in pole[2][57:] and xy4[2] in pole[2][57:]:
        winner = 2
    if xy1[3] in pole[3][57:] and xy2[3] in pole[3][57:] and xy3[3] in pole[3][57:] and xy4[3] in pole[3][57:]:
        winner = 3
    return winner

def wintime(win, game, p, winner):
    t = 5
    winfont = pygame.font.SysFont("Arial", 60)
    wintext = winfont.render("Player " + str(winner + 1) + ' wins!', 1, (255,0,0))
    closetext = winfont.render('Game will close in 5sec', 1, (255,0,0))
    win.fill((128, 128, 128))
    win.blit(wintext, (100, 290))
    win.blit(closetext, (100,440))
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()


def main():
    global d, f1, f2, f3, f4, k1, k2, k3, k4, a1, b1, c1, e1, r, turn, drys  # ,stop
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    while run:
        clock.tick(60)
        pygame.display.update()
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            n.send(d)
            redrawWindow(win, game, player)
            pygame.time.delay(500)

            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            pygame.display.update()
            pygame.time.delay(2000)

        # Check turn
        turn = int(n.sendsync('T'))
        print(turn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if turn == player:
                    if btn1.click(pos) and game.connected():
                        f1[player] = 1
                        f2[player] = 0
                        f3[player] = 0
                        f4[player] = 0
                    if btn2.click(pos) and game.connected():
                        f1[player] = 0
                        f2[player] = 1
                        f3[player] = 0
                        f4[player] = 0
                    if btn3.click(pos) and game.connected():
                        f1[player] = 0
                        f2[player] = 0
                        f3[player] = 1
                        f4[player] = 0
                    if btn4.click(pos) and game.connected():
                        f1[player] = 0
                        f2[player] = 0
                        f3[player] = 0
                        f4[player] = 1
                    if btn5.click(pos) and game.connected() and stop == 0:
                        rand = random.randint(1, 6)
                        d[player] = rand
                        drys[player] = rand
                        turn = int(n.sendsync('T+'))

                    makemove(player)
                    # if d[player] >= 1 and (k1[player] == 1 or k2[player] == 1 or k3[player] == 1 or k4[player] == 1):
                    # stop = 1
                    if r[player] == 1:
                        a1[player] = a1[player] + d[player]
                        r[player] = 0
                    if r[player] == 2:
                        b1[player] = b1[player] + d[player]
                        r[player] = 0
                    if r[player] == 3:
                        c1[player] = c1[player] + d[player]
                        r[player] = 0
                    if r[player] == 4:
                        e1[player] = e1[player] + d[player]
                        r[player] = 0
                    if a1[player] >= 61:
                        a1[player] = a1[player] - d[player]
                    if b1[player] >= 61:
                        b1[player] = b1[player] - d[player]
                    if c1[player] >= 61:
                        c1[player] = c1[player] - d[player]
                    if e1[player] >= 61:
                        e1[player] = e1[player] - d[player]
                    if k1[player] == 1:
                        if a1[player] == c1[player] or a1[player] == b1[player] or a1[player] == e1[player]:
                            if a1[player] <= 0:
                                a1[player] = a1[player]
                            else:
                                a1[player] = a1[player] - d[player]
                    if k2[player] == 1:
                        if b1[player] == c1[player] or b1[player] == e1[player] or b1[player] == a1[player]:
                            if b1[player] <= 0:
                                b1[player] = b1[player]
                            else:
                                b1[player] = b1[player] - d[player]
                    if k3[player] == 1:
                        if c1[player] == b1[player] or c1[player] == e1[player] or c1[player] == a1[player]:
                            if c1[player] <= 0:
                                c1[player] = c1[player]
                            else:
                                c1[player] = c1[player] - d[player]
                    if k4[player] == 1:
                        if e1[player] == b1[player] or e1[player] == c1[player] or e1[player] == a1[player]:
                            if e1[player] <= 0:
                                e1[player] = e1[player]
                            else:
                                e1[player] = e1[player] - d[player]
                    d[player] = 0
                    updatepos(player)

        # Before redraw, update pos of all pieces on board
        try:
            # Send data to serwer and receieve
            temp = n.sendsync(makesync(player))
            # Insert data into the lists
            print(temp)
            insertdata(temp, player)
        except:
            run = False
            print("Couldn't synchronize the data")
            break
        print("Wartości f1: ")
        print(f1)
        redrawWindow(win, game, player)
        pygame.display.update()
        w = wincheck()
        wl = [0,1,2,3]
        if w in wl:
            wintime(win,game,player, w)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("Arial", 60)
        text = font.render("Ludo", 1, (255, 0, 0))
        text1 = font.render("Press to start a game", 1, (255, 0, 0))
        win.blit(text, (370, 200))
        win.blit(text1, (180, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()
