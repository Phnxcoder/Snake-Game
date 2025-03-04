from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.write(f'Score {self.score}',align='center',font=('Arial',24,'normal'))

    def game_over(self):
        self.clear()
        self.write(f'GameOver',align='center',font=('Arial',24,'normal'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f'Score {self.score}',align='center',font=('Arial',24,'normal'))
