from turtle import Turtle


class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        with open("data.txt") as data:
            self.heigh_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.Score} High Score: {int(self.heigh_score)}", align="center", font=('Arial', 22, 'normal'))

    def inc(self):
        self.Score += 1
        self.update_scoreboard()

    def reset(self):
        if self.Score > self.heigh_score:
            self.heigh_score = self.Score
        self.Score = 0
        self.writ()
        self.update_scoreboard()

    def writ(self):
        with open("data.txt", mode='w') as wr:
            wr.write(f"{self.heigh_score}")
