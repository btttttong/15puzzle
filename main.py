import time
from turtle import Screen
from board import Board

screen = Screen()
screen.setup(800, 600)
screen.listen()
screen.tracer(0)
is_game_on = True

board = Board()

while is_game_on:
    screen.update()
    board.draw_tiles()

screen.mainloop()


