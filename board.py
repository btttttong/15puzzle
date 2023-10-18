import random
from turtle import Turtle, Screen


class Board:
    def __init__(self):
        self.tiles = [[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [15, 14, 13, None]]
        self.finish = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,None]]
        self.init_pos = (0,0)
        self.void_pos = [3, 3]
        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()

    def draw_tiles(self):
        self.t.clear()
        # t = Turtle()
        t=self.t
        self.t.goto(self.init_pos)
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

    def go_up(self):
        down_to_void_pos = self.void_pos[0]+1, self.void_pos[1]
        self.swap_with_void(down_to_void_pos)

    def go_down(self):
        # self.head.setheading(270)
        up_to_void_pos = self.void_pos[0]-1, self.void_pos[1]
        self.swap_with_void(up_to_void_pos)

    def go_left(self):
        right_to_void_pos = self.void_pos[0], self.void_pos[1]+1
        self.swap_with_void(right_to_void_pos)


    def go_right(self):
        left_to_void_pos = self.void_pos[0], self.void_pos[1]-1
        self.swap_with_void(left_to_void_pos)


    def swap_with_void(self, up_to_void_pos):
        row_void, col_void = self.void_pos
        row_next, col_next = up_to_void_pos
        if self.check_boundary(row_next, col_next):
            self.tiles[row_void][col_void], self.tiles[row_next][col_next] = self.tiles[row_next][col_next], self.tiles[row_void][col_void]
            self.void_pos[0] = row_next
            self.void_pos[1] = col_next

        self.draw_tiles()

    def check_boundary(self, row_num, col_num):
        if 0 <= row_num < 4:
            if 0 <= col_num < 4:
                return True
        return False
