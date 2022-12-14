from turtle import Turtle
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_l, align= 'center', font= FONT)
        self.goto(100, 200)
        self.write(self.score_r, align= 'center', font= FONT)
        

    def game_over(self):
        self.goto(0 , 0)
        self.write("Game Over!", align= 'center', font= FONT)    

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()  

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()  