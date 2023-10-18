import random
from turtle import Turtle, Screen


class Board:
    def __init__(self):
        self.tiles = [[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [15, 14, 13]]
        # self.nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def draw_tiles(self):
        t = Turtle()
        t.hideturtle()
        t.penup()
        for row in range(len(self.tiles)):
            print(row)
            for col in range(len(self.tiles[row])):
                print(' ', self.tiles[row][col])
                t.goto(t.xcor()+50, t.ycor())
                t.write(self.tiles[row][col], align='center', font=('Tahoma', 20, 'normal'))
            t.goto(t.xcor()-200, t.ycor()-50)

        # for row in range(len(self.tiles)):
        #     print(row)
        #     for col in range(3):
        #         ran = random.choice(self.nums)
        #         print(ran)
        #         self.tiles[row].append(ran)
        #         self.nums.pop(ran)
