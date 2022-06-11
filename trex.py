import turtle
import time

# Stworzenie okna

wn = turtle.Screen()
wn.title("T-Rex")
wn.bgcolor("white")
wn.setup(width=800, height=500)
wn.tracer(0)
wn.addshape('dino_stoi.gif')
wn.addshape('dino_ruch1.gif')
wn.addshape('dino_ruch2.gif')


POZIOM_PODŁOGI = -50
GRAWITACJA = -0.002

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
kaktus_1.color("grey")
kaktus_1.shapesize(stretch_wid=2, stretch_len=1)
kaktus_1.penup()
kaktus_1.goto(450, -60)
kaktus_1.dx = -0.2

# Kaktus 2
kaktus_2 = turtle.Turtle()
kaktus_2.speed(0)
kaktus_2.shape("square")
kaktus_2.color("grey")
kaktus_2.shapesize(stretch_wid=2, stretch_len=1)
kaktus_2.penup()
kaktus_2.goto(400, -60)
kaktus_2.dx = -0.2

# Dino
dino = turtle.Turtle()
dino.penup()

def dino_animacja():
    if dino.shape() == "dino_ruch1.gif":
        dino.shape("dino_ruch2.gif")
    elif dino.shape() == "dino_ruch2.gif":
        dino.shape("dino_ruch1.gif")
    wn.ontimer(dino_animacja, 10)
dino.speed(0)

dino.dy = 0
dino.stan = "biegnie"
dino.shape("dino_ruch1.gif")
dino_animacja()
dino.goto(-250, -50)



def skakanie():
    if dino.stan == "biegnie":
        dino.dy = 0.7
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
