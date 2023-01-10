# Ludo
We created a game called Ludo in python programing language that uses local server communication to allow for up to 4 players in one session.

[![](https://github.com/dandub03/Ludo/blob/a4a56d667136ae40415da22200953d467405b1ce/image/map1.png)]
# How to run
1.Download necessary library: py install pygame

2.Change IP in server.py and games.py to your local IP adress

3.Run server.py

4.Run 4 clients by running games.py four times
# How it works?
The game logic happens in client application, after making move client sends current position to the server, and receives positions of other players from server. The turn ends after the player throws the dice.
