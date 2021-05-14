# Simple Pong Project in Python 3
# By @itsbigrod
# Part 1: Getting started

import turtle
import winsound

wn = turtle.Screen() #window
wn.title("Pong Game by @itsbigrod")
wn.bgcolor("white") #background color
wn.setup(width=800,height=600) #screen setup
wn.tracer(0) #makes game faster

# Score
score_a = 0
score_b = 0 

# Paddle A
paddle_a = turtle.Turtle() #turtle object 
paddle_a.speed(0) #speed of animation A
paddle_a.shape("square") #shape of paddle A
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("red") #color of paddle A
paddle_a.penup() #picks pen up from drawing line
paddle_a.goto(-350,0)



# Paddle B
paddle_b = turtle.Turtle() #turtle object 
paddle_b.speed(0) #speed of animation B
paddle_b.shape("square") #shape of paddle B
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("red") #color of paddle B
paddle_b.penup() #picks pen up from drawing line
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle() #turtle object 
ball.speed(0) #speed of animation ball
ball.shape("circle") #shape of ball
ball.color("blue") #color of ball
ball.penup() #picks pen up from drawing line
ball.goto(0,0)

# ball moves by 2 pixels
ball.dx = .2 
ball.dy = .2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  - Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #calls paddle_a_up on key W
wn.onkeypress(paddle_a_down, "s") #calls paddle_a_down on key S

wn.onkeypress(paddle_b_up, "Up") #calls paddle_a_up on key up
wn.onkeypress(paddle_b_down, "Down") #calls paddle_a_down on key down

# Main Game Loop
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("ballsound.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290) 
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  - Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  - Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1