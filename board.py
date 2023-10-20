import random
from turtle import Turtle, Screen
import numpy as np


class Board:
    def __init__(self):
        self.nums = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.finish = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12], [None, 15, 14, 13]]
        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.init_pos = (0, 0)
        self.tiles = self.create_puzzle()
        self.void_pos = none_index = np.where(self.tiles == None)
        self.void_pos = [none_index[0][0], none_index[1][0]]
        # self.void_pos = [3, 3]
        # self.start = self.create_puzzle()

    def draw_tiles(self):
        self.t.clear()
        # t = Turtle()
        t = self.t
        self.t.goto(self.init_pos)
        for row in range(len(self.tiles)):
            # print(row)
            for col in range(len(self.tiles[row])):
                # print(' ', self.tiles[row][col])
                t.goto(t.xcor() + 50, t.ycor())
                t.write(self.tiles[row][col], align='center', font=('Tahoma', 20, 'normal'))
            t.goto(t.xcor() - 200, t.ycor() - 50)

    def go_up(self):
        down_to_void_pos = self.void_pos[0] + 1, self.void_pos[1]
        self.swap_with_void(down_to_void_pos)

    def go_down(self):
        # self.head.setheading(270)
        up_to_void_pos = self.void_pos[0] - 1, self.void_pos[1]
        self.swap_with_void(up_to_void_pos)

    def go_left(self):
        right_to_void_pos = self.void_pos[0], self.void_pos[1] + 1
        self.swap_with_void(right_to_void_pos)

    def go_right(self):
        left_to_void_pos = self.void_pos[0], self.void_pos[1] - 1
        self.swap_with_void(left_to_void_pos)

    def swap_with_void(self, up_to_void_pos):
        row_void, col_void = self.void_pos
        row_next, col_next = up_to_void_pos
        if self.check_boundary(row_next, col_next):
            self.tiles[row_void][col_void], self.tiles[row_next][col_next] = self.tiles[row_next][col_next], \
                self.tiles[row_void][col_void]
            self.void_pos[0] = row_next
            self.void_pos[1] = col_next

        self.draw_tiles()

    def check_boundary(self, row_num, col_num):
        if 0 <= row_num < 4:
            if 0 <= col_num < 4:
                return True
        return False

    def create_puzzle(self):
        rv = [[], [], [], []]
        for row in range(len(rv)):
            for col in range(4):
                ran = random.choice(self.nums)
                rv[row].append(ran)
                self.nums.remove(ran)
        print('rv = ', rv)

        rv = self.check_solveable(rv)

        return rv

    def check_solveable(self, listrv):
        # check with inversion if even num then swap
        listrv = [item for sublist in listrv for item in sublist]
        print('check_solveable = ', listrv)
        inversions = 0
        for i in range(len(listrv)):
            for j in range(i + 1, len(listrv)):
                if listrv[i] is not None and listrv[j] is not None and listrv[i] > listrv[j]:
                    inversions += 1
        print('inversions', inversions)

        if inversions % 2 == 0:
            for i in range(len(listrv)):
                if listrv[i] is not None and listrv[i + 1] is not None and listrv[i] > listrv[i + 1]:
                    listrv[i], listrv[i + 1] = listrv[i + 1], listrv[i]
                    break
            print(f'swap listrv = {listrv}')

        # back to [[],[],[],[]]
        solveablerv = np.reshape(listrv, (4, 4))
        # for i in range(len(listrv)):
        #     row = []
        #     for j in range(4):
        #         row.append(listrv[i * 4 + j])
        #         solveablerv.append(row)

        return solveablerv

    def check_correct_ans(self):
        return np.all(self.finish == self.tiles)
