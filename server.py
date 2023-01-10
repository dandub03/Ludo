import socket
from _thread import *
import pickle
from game import Game

server = "192.168.0.24"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0
#             [[Player1], [Player2], [Player3], [Player4]]
synchropos = [['start','start','start','start'],['start','start','start','start'],['start','start','start','start'],['start','start','start','start']]
synchrodice = [0,0,0,0]
turn = 0

# Przyjmij dane, zdekoduj ze stringa do tupla bądź listy i wstaw do odpowiednich pozycji w listach ze względu na gracza
# Wyczyść przyjęte dane żeby umieścić je w listach
def prepdata(d):
    l = d.split(',')
    l.remove('S')
    return l
# Wsadź dane do listy
def insert(d, player):
    temp = prepdata(d)
    for i in range(5):
        if i == 4:
            synchrodice[player] = temp[4]
        else:
            synchropos[player][i] = temp[i]
# Dane z list przygotuje do przesłania do gracza
def makesyncstring():
    temp = str(synchropos) + ',' + str(synchrodice)
    temp = temp.replace("[","")
    temp = temp.replace("]","")
    temp = temp.replace("'","")
    temp = temp.replace(" ","")
    return temp

def giveturn():
    return str(turn)

def threaded_client(conn, p, gameId):
    global idCount, turn
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()


            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                 # Check if data received is for synchronisation
                elif data[0] == 'S':
                    insert(data,p)
                    # Skoro dane są już wsadzone do list, teraz wyślij do gracza zaktualizowane dane
                    conn.sendall(str.encode(makesyncstring()))
                elif data == 'T':
                    conn.sendall(str.encode(giveturn()))
                elif data == 'T+':
                    if turn == idCount - 1:
                        turn = 0
                    else:
                        turn = turn + 1
                    conn.sendall(str.encode(giveturn()))
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 4
    if idCount % 4 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")





    elif idCount % 4 == 2:
        games[gameId] = Game(gameId)
        print("players 2/4")
        p = 1




    elif idCount % 4 == 3:
        games[gameId] = Game(gameId)
        print("players 3/4")
        p = 2

    else:
        p = 3
        games[gameId].ready = True




    start_new_thread(threaded_client, (conn, p, gameId))
