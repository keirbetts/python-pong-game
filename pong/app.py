import turtle

window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)


score1 = 0
score2 = 0

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('blue')
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)


paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('red')
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('player 1: 0  player 2: 0', align='center',
          font=('Courier', 24, 'normal'))


def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


window.listen()
window.onkeypress(paddle1_up, 'w')
window.onkeypress(paddle2_up, 'Up')
window.onkeypress(paddle1_down, 's')
window.onkeypress(paddle2_down, 'Down')

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write('player 1: {}  player 2: {}'.format(score1, score2), align='center',
                  font=('Courier', 24, 'normal'))

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write('player 1: {}  player 2: {}'.format(score1, score2), align='center',
                  font=('Courier', 24, 'normal'))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
