from turtle import Screen, Turtle
from random import randint

def draw_arena():
    drawer = Turtle()
    drawer.speed(0)
    drawer.hideturtle()
    drawer.penup()
    drawer.goto(-250, 250)
    drawer.color("light blue")
    drawer.pendown()
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(500)
        drawer.right(90)
    drawer.end_fill()


class Tank(Turtle):
    max_missiles = 0


    def __init__(self, x_start, y_start, color, left_key, right_key, fire_key):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.goto(x_start, y_start)
        self.left_key = left_key
        self.right_key = right_key
        self.fire_key = fire_key
        self.missiles = []


    def advance(self):
        self.forward(5)
        self.keep_in_bounds()


    def keep_in_bounds(self):
        x, y = self.position()
        if not (-240 < x < 240 and -240 < y < 240):
            self.undo()
            self.left(180)


    def rotate_left(self):
        self.left(10)


    def rotate_right(self):
        self.right(10)


    def fire(self):
        if Tank.max_missiles < 10:
            missile = Missile(self)
            self.missiles.append(missile)
            Tank.max_missiles += 1


class Missile(Turtle):
    def __init__(self, shooter):
        super().__init__()
        self.hideturtle()
        self.shape("triangle")
        self.color("orange")
        self.penup()
        self.goto(shooter.xcor(), shooter.ycor())
        self.setheading(shooter.heading())
        self.showturtle()


    def move(self):
        self.forward(15)


class Treasure(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.speed(0)
        self.reposition()


    def reposition(self):
        self.goto(randint(-240, 240), randint(-240, 240))


class Adversary(Turtle):
    def __init__(self, target):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.penup()
        self.speed(1)
        self.target = target
        self.goto(randint(-240, 240), randint(-240, 240))


    def chase(self):
        self.setheading(self.towards(self.target))
        self.forward(2)


def check_treasure_collision(tank, treasure, adversaries):
    if tank.distance(treasure) < 20:
        treasure.reposition()
        adversaries.append(Adversary(tank))
        adversaries.append(Adversary(tank))


def check_missile_collision(missile, adversaries):
    for adversary in adversaries:
        if missile.distance(adversary) < 20:
            missile.hideturtle()
            adversaries.remove(adversary)
            adversary.hideturtle()
            Tank.max_missiles -= 1
            return True
    return False


def check_adversary_collision(tank, adversaries):
    for adversary in adversaries:
        if adversary.distance(tank) < 20:
            return True
    return False


def announce_winner(color):
    announcer = Turtle()
    announcer.hideturtle()
    announcer.color(color)
    announcer.penup()
    announcer.goto(0, 0)
    announcer.write(f"{color.upper()} Wins!", align="center", font=("Arial", 24, "bold"))


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=500, height=500)


    draw_arena()


    tank1 = Tank(-100, 0, "cyan", "Left", "Right", "Up")
    tank2 = Tank(100, 0, "magenta", "a", "d", "w")


    treasure = Treasure()


    adversaries = []


    screen.listen()
    screen.onkeypress(tank1.rotate_left, tank1.left_key)
    screen.onkeypress(tank1.rotate_right, tank1.right_key)
    screen.onkeypress(tank1.fire, tank1.fire_key)
    screen.onkeypress(tank2.rotate_left, tank2.left_key)
    screen.onkeypress(tank2.rotate_right, tank2.right_key)
    screen.onkeypress(tank2.fire, tank2.fire_key)


    game_active = True
    while game_active:
        tank1.advance()
        tank2.advance()


        for tank in [tank1, tank2]:
            for missile in tank.missiles:
                missile.move()
                if abs(missile.xcor()) > 250 or abs(missile.ycor()) > 250:
                    missile.hideturtle()
                    tank.missiles.remove(missile)
                    Tank.max_missiles -= 1
                if check_missile_collision(missile, adversaries):
                    tank.missiles.remove(missile)


            check_treasure_collision(tank, treasure, adversaries)


        for adversary in adversaries:
            adversary.chase()


        if check_adversary_collision(tank1, adversaries):
            announce_winner(tank2.color()[0])
            game_active = False


        if check_adversary_collision(tank2, adversaries):
            announce_winner(tank1.color()[0])
            game_active = False


        screen.update()


    screen.mainloop()


if __name__ == "__main__":
    main()





