import turtle
import time


# Stworzenie okna

okno = turtle.Screen()
okno.title("T-Rex")
okno.bgcolor("white")
okno.setup(width=800, height=500)
okno.tracer(0)

POZIOM_PODŁOGI = -60
GRAWITACJA = -0.002
punkty=0
# Stworzenie podłogi

podloga = turtle.Turtle()
podloga.speed(0)
podloga.shape("square")
podloga.color("grey")
podloga.shapesize(stretch_wid=15, stretch_len=50)
podloga.penup()
podloga.goto(0, -230)

# punkty
punkty = turtle.Turtle()
punkty.speed(0)
punkty.color("black")
punkty.penup()
punkty.hideturtle()
punkty.goto(200,200)
punkty.write("Wynik: 0", align = "center", font=("Courier",10,"normal"))



# Kaktus 1
kaktus_1 = turtle.Turtle()
kaktus_1.speed(0)
kaktus_1.shape("square")
kaktus_1.color("grey")
kaktus_1.shapesize(stretch_wid=2, stretch_len=1)
kaktus_1.penup()
pozycja = kaktus_1.goto(350, -60)
kaktus_1.dx = -0.2

# # Kaktus 2
# kaktus_2 = turtle.Turtle()
# kaktus_2.speed(0)
# kaktus_2.shape("square")
# kaktus_2.color("grey")
# kaktus_2.shapesize(stretch_wid=2, stretch_len=1)
# kaktus_2.penup()
# kaktus_2.goto(400, -60)
# kaktus_2.dx = -0.2

# Dino
dino = turtle.Turtle()
dino.speed(0)
dino.shape("square")
dino.color("grey")
dino.shapesize(stretch_wid=2, stretch_len=1.5)
dino.penup()
dino.dy = 0
dino.stan = "biegnie"
dino.goto(-250, -60)

def skakanie():
    if dino.stan == "biegnie":
        dino.dy = 0.7
        dino.stan = "skacze"

okno.listen()
okno.onkeypress(skakanie, "space")




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

    #kolizja z jednym kaktusem
    if dino.xcor()>kaktus_1.xcor()-10 and dino.xcor()<kaktus_1.xcor()+10 and dino.ycor()<=kaktus_1.ycor():
        dino.setx(pozycja)
        dino.sety(pozycja)
        break


    okno.update()
