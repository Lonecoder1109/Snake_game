from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.pendown()
        self.pencolor("white")
        self.update_scorecard()

    def update_scorecard(self):
        self.write(arg=f"Score : {self.score}", align='center', font=('Courier', 14, 'normal'))

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(arg=f"GAME OVER\nFinal score : {self.score}", align='center', font=('Courier', 20, 'normal'))


    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scorecard()