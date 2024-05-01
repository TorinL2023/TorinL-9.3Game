import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

game = turtle.Screen()
game.title("Snake Game")
game.bgcolor("blue")
game.setup(width=600, height=600)
game.tracer(0)

game.register_shape("snake_headUp.gif")
game.register_shape("snake_headDown.gif")
game.register_shape("snake_headLeft.gif")
game.register_shape("snake_headRight.gif")

head = turtle.Turtle()
head.shape("snake_headUp.gif")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

game.register_shape("apple.gif")
food = turtle.Turtle()
food.shape("apple.gif")
food.speed(0)
food.color("red")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
          font=("candara", 24, "bold"))

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
color_index = 0

def group():
    if head.direction != "down":
        head.direction = "up"
        head.shape("snake_headUp.gif")

def godown():
    if head.direction != "up":
        head.direction = "down"
        head.shape("snake_headDown.gif")

def goleft():
    if head.direction != "right":
        head.direction = "left"
        head.shape("snake_headLeft.gif")

def goright():
    if head.direction != "left":
        head.direction = "right"
        head.shape("snake_headRight.gif")

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

game.listen()
game.onkeypress(group, "w")
game.onkeypress(godown, "s")
game.onkeypress(goleft, "a")
game.onkeypress(goright, "d")

segments = []

while True:
    game.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color(colors[color_index])
        color_index = (color_index + 1) % len(colors)
        new_segment.penup()
        new_segment.goto(0, 0)
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        segments[index].color("black", colors[(index + color_index) % len(colors)])
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        segments[0].color("black", colors[color_index])

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

game.mainloop()
