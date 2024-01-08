import turtle

class Bullet(turtle.Turtle):
    def __ini__(self):
        super().__init__()
        turtle.register_shape("missile.gif")
        self.shape("missile.gif")
        self.pu()
        self.goto(0,-240)
        self.speedamt = 20
        self.state = "Ready"