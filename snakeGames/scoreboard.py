from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_high_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score();

        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open('data.txt') as file:
            return file.read();

    def set_high_score(self):
        with open('data.txt', mode='w') as file:
            return file.write(str(self.high_score))
