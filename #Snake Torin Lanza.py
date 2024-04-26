## TORIN LANZA SNAKE
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

class SnakeGame:
    def __init__(self):
        self.tl = turtle.Screen()
        self.tl.title("Snake Game")
        self.tl.bgcolor("green")
        self.tl.setup(width=600, height=600)
        self.tl.tracer(0)
        self.tl.addshape('apple.gif')

        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Stop"

        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape('apple.gif')
        self.food.penup()
        self.food.goto(0, 100)

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 250)
        self.pen.write("Score : 0 High Score : 0", align="center", font=("candara", 24, "bold"))

        self.segments = []

        self.tl.listen()
        self.tl.onkeypress(self.group, "w")
        self.tl.onkeypress(self.godown, "s")
        self.tl.onkeypress(self.goleft, "a")
        self.tl.onkeypress(self.goright, "d")

    def group(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def godown(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def goleft(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def goright(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def run_game(self):
        global score
        global high_score
        while True:
            self.tl.update()
            if (
                self.head.xcor() > 290
                or self.head.xcor() < -290
                or self.head.ycor() > 290
                or self.head.ycor() < -290
            ):
                self.game_over()
            self.move()
            if self.head.distance(self.food) < 20:
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                self.food.goto(x, y)
                score += 10
                if score > high_score:
                    high_score = score
                self.pen.clear()
                self.pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
                self.add_segment()
            self.update_segment_positions()
            self.check_collision_with_segments()
            time.sleep(delay)

    def game_over(self):
        time.sleep(1)
        self.head.goto(0, 0)
        self.head.direction = "Stop"
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        global score
        score = 0
        global delay
        delay = 0.1
        self.pen.clear()
        self.pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    def add_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        segcolors = random.choice(['red', 'orange', 'yellow', 'blue', 'purple'])
        new_segment.shape("square")
        new_segment.color(segcolors)
        new_segment.penup()
        self.segments.append(new_segment)

    def update_segment_positions(self):
        if len(self.segments) > 0:
            for index in range(len(self.segments) - 1, 0, -1):
                x = self.segments[index - 1].xcor()
                y = self.segments[index - 1].ycor()
                self.segments[index].goto(x, y)
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

    def check_collision_with_segments(self):
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 20:
                self.game_over()

# Key functions outside of class
def group():
    game.group()

def godown():
    game.godown()

def goleft():
    game.goleft()

def goright():
    game.goright()

if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
