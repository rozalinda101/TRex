import turtle
import time
import random

# Stworzenie okna
okno = turtle.Screen()
okno.title("T-Rex")
okno.bgcolor("white")
okno.setup(width=800, height=500)
okno.tracer(0)

POZIOM_PODŁOGI = -60
GRAWITACJA = -0.004
punkty=0

# Stworzenie podłogi
podloga = turtle.Turtle()
podloga.speed(0)
podloga.shape("square")
podloga.color("grey")
podloga.shapesize(stretch_wid=15, stretch_len=50)
podloga.penup()
podloga.goto(0, -230)

punkty_aktualne=0

czas_pocz=time.time()

# Kaktus 1
kaktus_1 = turtle.Turtle()
kaktus_1.speed(0)
kaktus_1.shape("square")
kaktus_1.color("green")
kaktus_1.shapesize(stretch_wid=2, stretch_len=1)
kaktus_1.penup()
pozycja = kaktus_1.goto(random.randint(300,400), -60)
kaktus_1.dx = -0.6

# Kaktus 2
kaktus_2 = turtle.Turtle()
kaktus_2.speed(0)
kaktus_2.shape("square")
kaktus_2.color("green")
kaktus_2.shapesize(stretch_wid=2, stretch_len=1)
kaktus_2.penup()
pozycja = kaktus_2.goto(random.randint(600,700), -60)
kaktus_2.dx = -0.6

# Kaktus 3
kaktus_3 = turtle.Turtle()
kaktus_3.speed(0)
kaktus_3.shape("square")
kaktus_3.color("green")
kaktus_3.shapesize(stretch_wid=2, stretch_len=1)
kaktus_3.penup()
pozycja = kaktus_3.goto(random.randint(800,900), -60)
kaktus_3.dx = -0.6

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
        dino.dy = 0.7
        dino.stan = "skacze"

okno.listen()
okno.onkeypress(skakanie, "space")

def restart():
    okno_restart=turtle.Turtle()
    okno_restart.speed(0)
    okno_restart.color("red")
    okno_restart.write(f"KONIEC GRY! Zdobyłeś {punkty_aktualne} punktów", align = "center", font=("Courier",15,"normal"))

# Główna pętla gry
while True:

    # punkty
    punkty = turtle.Turtle()
    punkty.speed(0)
    punkty.color("black")
    punkty.penup()
    punkty.hideturtle()
    punkty.goto(200,200)
    punkty.write(f"Wynik: {punkty_aktualne}", align = "center", font=("Courier",15,"normal"))
    punkty.clear()

    czas=time.time()

    punkty_aktualne=round((czas-czas_pocz)/3)

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
    x = kaktus_1.xcor()
    x += kaktus_1.dx
    kaktus_1.setx(x)

    if kaktus_1.xcor() < -400:
        x = random.randint(400, 600)
        kaktus_1.setx(x)
        kaktus_1.dx *= 1.05
        print(kaktus_1.dx)

    x = kaktus_2.xcor()
    x += kaktus_2.dx
    kaktus_2.setx(x)

    if kaktus_2.xcor() < -400:
        x = random.randint(400, 600)
        kaktus_2.setx(x)
        kaktus_2.dx *= 1.05
        print(kaktus_2.dx)

    x = kaktus_3.xcor()
    x += kaktus_3.dx
    kaktus_3.setx(x)

    if kaktus_3.xcor() < -400:
        x = random.randint(400, 600)
        kaktus_3.setx(x)
        kaktus_3.dx *= 1.05
        print(kaktus_2.dx)

    #kolizja z jednym kaktusem
    if dino.xcor()>kaktus_1.xcor()-25 and dino.xcor()<kaktus_1.xcor()+40 and dino.ycor()<=kaktus_1.ycor():
        dino.setx(pozycja)
        dino.sety(pozycja)
        restart()
        turtle.done()

    #kolizja z drugim kaktusem
    if dino.xcor()>kaktus_2.xcor()-25 and dino.xcor()<kaktus_2.xcor()+40 and dino.ycor()<=kaktus_2.ycor():
        dino.setx(pozycja)
        dino.sety(pozycja)
        restart()
        turtle.done()

    #kolizja z trzecim kaktusem
    if dino.xcor()>kaktus_3.xcor()-25 and dino.xcor()<kaktus_3.xcor()+40 and dino.ycor()<=kaktus_3.ycor():
        dino.setx(pozycja)
        dino.sety(pozycja)
        restart()
        turtle.done()

    okno.update()
