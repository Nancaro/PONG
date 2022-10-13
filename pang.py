import turtle

#windows
wn = turtle.Screen ()
wn.title("Pang by Bruno Aguirre Nancaro") 
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
Score1 = 0
Score2 = 0

#Player1
Player1 = turtle.Turtle()
Player1.speed(0)
Player1.shape("square")
Player1.color("white")
Player1.penup()
Player1.goto(-350,0)
Player1.shapesize(stretch_wid=5, stretch_len=1)

#Player2
Player2 = turtle.Turtle()
Player2.speed(0)
Player2.shape("square")
Player2.color("white")
Player2.penup()
Player2.goto(350,0)
Player2.shapesize(stretch_wid=5, stretch_len=1)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)

#Modification (This variables for change speed of the ball)
Ball.dx =0.7
Ball.dy =0.7

#Midline
Midline = turtle.Turtle()
Midline.color("white")
Midline.goto(0,400)
Midline.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador 1: 0		Jugador 2:0", align="center", font=("Courier",24,"normal"))

#Function
def P1_up():
    y= Player1.ycor()
    y+=20
    Player1.sety(y)

def P1_down():
    y= Player1.ycor()
    y-=20
    Player1.sety(y)

def P2_up():
    y= Player2.ycor()
    y+=20
    Player2.sety(y)

def P2_down():
    y= Player2.ycor()
    y-=20
    Player2.sety(y)

def P1_up():
    y=Player1.ycor()
    y += 20
    Player1.sety(y)
    if y>250:
        y +=-20
        Player1.sety(y)
 
def P1_down():
    y=Player1.ycor()
    y -= 20
    Player1.sety(y)
    if y<-250:
        y += 20
        Player1.sety(y)
 

def P2_up():
    y=Player2.ycor()
    y += 20
    Player2.sety(y)
    if y>250:
        y +=-20
        Player2.sety(y)
 

def P2_down():
    y=Player2.ycor()
    y -= 20
    Player2.sety(y)
    if y<-250:
        y +=20
        Player2.sety(y)

#Keyboard 

wn.listen()
wn.onkeypress(P1_up, "w")
wn.onkeypress(P1_down, "s")
wn.onkeypress(P2_up, "Up")
wn.onkeypress(P2_down, "Down")

while True:
	wn.update()

	Ball.setx(Ball.xcor() + Ball.dx)
	Ball.sety(Ball.ycor() + Ball.dy)

	#Revisa colisiones con los bordes de la ventana
	if Ball.ycor() > 290:
		Ball.dy *= -1
	if Ball.ycor() < -290:
		Ball.dy *= -1

  # Si la pelota sale por la izq o derecha, esta regresa al centro.
	if Ball.xcor() > 390:
		Ball.goto(0,0)
		Ball.dx *= -1
		Score1 += 1
		pen.clear()
		pen.write("Player 1: {}		Player 2: {}".format(Score1,Score2), align = "center", font=("Courier", 24, "normal"))

	if Ball.xcor() < -390:
		Ball.goto(0,0)
		Ball.dx *= -1
		Score2 += 1
		pen.clear()
		pen.write("Player 1: {}		Player 2: {}".format(Score1,Score2), align = "center", font=("Courier", 24, "normal"))

	if ((Ball.xcor() > 340 and Ball.xcor() < 350)
			and (Ball.ycor() < Player2.ycor() + 50
			and Ball.ycor() > Player2.ycor() - 50)):
		Ball.dx *= -1
		Ball.dy *= -1

	if ((Ball.xcor() < -340 and Ball.xcor() > -350)
			and (Ball.ycor() < Player1.ycor() + 50
			and Ball.ycor() > Player1.ycor() - 50)):
		Ball.dx *= -1
		Ball.dy *= -1

turtle.mainloop()