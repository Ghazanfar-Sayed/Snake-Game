from turtle import Turtle
ALIGNMENT = 'center'
FONT =  ("Verdana", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.speed("fastest")
        self.goto((0, 270))
        self.hideturtle()
        self.update_scoreboard()
       
        
    def update_scoreboard(self):
         self.clear()
         self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
    
    def increase_score(self):
        self.score += 1
        
        self.update_scoreboard()

    def game_over(self):
         self.goto(0,0)
         self.write("GAME OVER", font=FONT, align=ALIGNMENT)