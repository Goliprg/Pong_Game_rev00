
from turtle import Turtle



ALIGN = "center"
FONT = ("Courier",20,"normal")


class UserScore(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-20, 170)
        self.current_score = -1
        self.score_update()



    def score_update(self):
        self.current_score += 1
        self.clear()
        self.write(self.current_score, False, ALIGN, FONT )
        if self.current_score == 10:
           self.game_over()
           return False
        else:
            return True
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER, YOU WIN", False, ALIGN, FONT)




class ComputerScore(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(20, 170)
        self.current_score = -1
        self.score_update()

    def score_update(self):
        self.current_score += 1
        self.clear()
        self.write(self.current_score, False, ALIGN, FONT)
        if self.current_score == 10:
            self.game_over()
            return False
        else:
            return True

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER, COMPUTER WINS", False, ALIGN, FONT)

