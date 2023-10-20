from turtle import Turtle
class Score:
    def __init__(self):
        self.score = 0
        self.ts = Turtle()
        self.ts.penup()
        self.ts.hideturtle()


    def draw_score(self):
        ts = self.ts
        ts.goto(500, 0)
        ts.clear()
        ts.write(f'score: {self.score}', align='center', font=('Tahoma', 20, 'normal'))


    def add_score(self):
        self.score
