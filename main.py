from board import Board
import pyxel

board = Board(256, 256)
# we establish the dimensions of the screen and the Title of our game:
pyxel.init(board.width, board.height, caption="This is super Mario")
# we load all the pyxres of mario and the elements
pyxel.load("assets/resources.pyxres")
# we import the song
pyxel.playm(0, loop=True)
# we invoke the draw and update from the board so we can start the game
pyxel.run(board.draw, board.update)



