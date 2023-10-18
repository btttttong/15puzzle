import time
from turtle import Screen
from board import Board

screen = Screen()
screen.setup(800, 600)
screen.listen()
screen.tracer(0)
is_game_on = True

board = Board()

screen.onkeypress(fun=board.go_up, key="Up")
screen.onkeypress(fun=board.go_down, key="Down")
screen.onkeypress(fun=board.go_right, key="Right")
screen.onkeypress(fun=board.go_left, key="Left")



while is_game_on:
    screen.update()
    board.draw_tiles()

screen.mainloop()


