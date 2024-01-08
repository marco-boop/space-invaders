# creating the class player with move_left() and move_right() functions
import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("player.gif")
        self.color("blue")
        self.speed(0)
        self.shape("player.gif")
        self.pu()
        self.goto(0,-250)

        #player movement
        self.playerspeed = 4

    def move_left(self):
        x = self.xcor()
        x -= self.playerspeed()
        if x < -450:
            x = -450
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.playerspeed()
        if x > 450:
            x = 450
        self.setx(x)