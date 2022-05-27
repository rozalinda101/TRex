import turtle
import time

# Stworzenie okna

wn = turtle.Screen()
wn.title("T-Rex")
wn.bgcolor("white")
wn.setup(width=800, height=500)
wn.tracer(0)

POZIOM_PODŁOGI = -60
GRAWITACJA = -0.04

# Stworzenie podłogi

podloga = turtle.Turtle()
podloga.speed(0)
podloga.shape("square")
podloga.color("grey")
podloga.shapesize(stretch_wid=15, stretch_len=50)
podloga.penup()
podloga.goto(0, -230)




# Kaktus 1
kaktus_1 = turtle.Turtle()
kaktus_1.speed(0)
kaktus_1.shape("square")
kaktus_1.color("black")
kaktus_1.shapesize(stretch_wid=2, stretch_len=1)
kaktus_1.penup()
kaktus_1.goto(450, -60)
kaktus_1.dx = -0.8

# Kaktus 2
kaktus_2 = turtle.Turtle()
kaktus_2.speed(0)
kaktus_2.shape("square")
kaktus_2.color("black")
kaktus_2.shapesize(stretch_wid=2, stretch_len=1)
kaktus_2.penup()
kaktus_2.goto(400, -60)
kaktus_2.dx = -0.8

# Dino
dino = turtle.Turtle()
dino.speed(0)
dino.shape("square")
dino.color("black")
dino.shapesize(stretch_wid=2, stretch_len=1.5)
dino.penup()
dino.dy = 0
dino.stan = "biegnie"
dino.goto(-250, -60)

def skakanie():
    if dino.stan == "biegnie":
        dino.dy = 2.5
        dino.stan = "skacze"

wn.listen()
wn.onkeypress(skakanie, "space")




# Główna pętla gry
while True:

    # GRAWITACJA
    dino.dy += GRAWITACJA

    # Skakanie
    y = dino.ycor()
    y += dino.dy
    dino.sety(y)

    # Przestań spadać
    if dino.ycor() < POZIOM_PODŁOGI:
        dino.sety(POZIOM_PODŁOGI)
        dino.dy = 0
        dino.stan = "biegnie"

    #Poruszanie kaktusem
    kaktus_1.setx(kaktus_1.xcor() + kaktus_1.dx)

    wn.update()
