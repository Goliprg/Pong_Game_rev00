import time

from turtle import Screen
from paddle import Paddle, Ball
from random import choice
from scoreboard import ComputerScore,UserScore


screen = Screen()
screen.title("Pong Game")
screen.setup(800, 400)
screen.bgcolor("black")
screen.tracer(0)
dashed_line = Paddle()
dashed_line.make_dashed_line()
del dashed_line

user_paddle = Paddle()
user_paddle.goto(-385,0)

computer_paddle = Paddle()
computer_paddle.goto(385,-170)
ball = Ball()
screen.update()
screen.tracer(1)
moving_angle = choice([x for x in range(0, 361) if x not in (range(40, 140) and range(220, 320))])
flag_move_up = 1
computer_score = ComputerScore()
user_score = UserScore()
game_on = True
while game_on:
   screen.listen()
   screen.onkey(fun=user_paddle.move_up, key="Up")
   screen.onkey(fun=user_paddle.move_down, key="Down")
   if flag_move_up == 1:
      if computer_paddle.ycor() >= 160:
         flag_move_up = 0
      computer_paddle.move_up()
   else:
      if computer_paddle.ycor() <= -160:
         flag_move_up = 1
      computer_paddle.move_down()

   ball.move_ball(moving_angle)

   if ball.xcor()< -390:
      game_on = computer_score.score_update()
      ball.home()
      time.sleep(1)
      moving_angle = choice([x for x in range(0, 361) if x not in ( range(40, 140) and range(220,320))])
   elif ball.xcor()> 390:
      game_on = user_score.score_update()
      ball.home()
      time.sleep(1)
      moving_angle = choice([x for x in range(0, 361) if x not in (range(40, 140) and range(220, 320))])

   if ball.ycor()>= 185 or ball.ycor() <= -180:
      last_moving_angle = moving_angle
      moving_angle = ball.bounce(last_moving_angle)

   if (abs(ball.xcor() - user_paddle.xcor()) <= 15 and abs(ball.ycor()-user_paddle.ycor())< 40) or (abs(ball.xcor() - computer_paddle.xcor()) <= 15 and abs(ball.ycor()-computer_paddle.ycor())< 40):
      last_moving_angle = moving_angle
      moving_angle = ball.paddle_bounce(last_moving_angle)



screen.exitonclick()













