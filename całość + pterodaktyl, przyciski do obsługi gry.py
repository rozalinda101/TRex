import turtle
import time
import random

# Stworzenie okna
def run_game():
    okno = turtle.Screen()
    okno.title("T-Rex")
    okno.bgcolor("white")
    okno.setup(width=800, height=500)
    okno.tracer(0)
    okno.addshape('dino_stoi.gif')
    okno.addshape('dino_ruch1.gif')
    okno.addshape('dino_ruch2.gif')
    okno.addshape('kaktus1.gif')
    okno.addshape('pterodaktyl.gif')

    POZIOM_PODŁOGI = -50
    GRAWITACJA = -0.006
    stan_punktow = 0
    czas_pocz = time.time()

# punkty
    punkty = turtle.Turtle()
    punkty.speed(0)
    punkty.color("black")
    punkty.penup()
    punkty.hideturtle()
    punkty.goto(200,200)
    punkty.write("Wynik: 0", align = "center", font=("Courier",15,"normal"))




# Stworzenie podłogi
    podloga = turtle.Turtle()
    podloga.speed(0)
    podloga.shape("square")
    podloga.color("green")
    podloga.shapesize(stretch_wid=15, stretch_len=50)
    podloga.penup()
    podloga.goto(0, -230)


# Kaktus 1
    kaktus_1 = turtle.Turtle()
    kaktus_1.penup()
    kaktus_1.speed(0)
    kaktus_1.shape("kaktus1.gif")
    pozycja = kaktus_1.goto(random.randint(300,500), -60)
    kaktus_1.dx = -0.6



# Kaktus 2
    kaktus_2 = turtle.Turtle()
    kaktus_2.penup()
    kaktus_2.speed(0)
    kaktus_2.shape("kaktus1.gif")
    pozycja = kaktus_2.goto(random.randint(600,800), -60)
    kaktus_2.dx = -0.6



#Pterodaktyl
    pterodaktyl=turtle.Turtle()
    pterodaktyl.penup()
    pterodaktyl.speed(0)
    pterodaktyl.shape("pterodaktyl.gif")
    pozycja=pterodaktyl.goto(random.randint(1700,1750), 70)
    pterodaktyl.dx = -1

# Dino
    dino = turtle.Turtle()
    dino.penup()

    def dino_animacja():
        if dino.shape() == "dino_ruch1.gif":
            dino.shape("dino_ruch2.gif")
        elif dino.shape() == "dino_ruch2.gif":
            dino.shape("dino_ruch1.gif")
        okno.ontimer(dino_animacja, 150)

    dino.speed(0)
    dino.dy = 0
    dino.stan = "biegnie"
    dino.shape("dino_ruch1.gif")
    dino_animacja()
    dino.goto(-250, -50)

    def skakanie():
        if dino.stan == "biegnie":
            dino.dy = 1
            dino.stan = "skacze"

    okno.listen()
    okno.onkeypress(skakanie, "space")

    def koniec():
        okno_restart=turtle.Turtle()
        okno_restart.speed(0)
        okno_restart.color("red")
        okno_restart.write(f"KONIEC GRY! Zdobyłeś {stan_punktow}",align = "center", font=("Courier",15,"normal"))
        time.sleep(3)
        okno_restart.clear()
        restart=okno_restart.write(f"Jeśli chcesz zagrać jeszcze raz wciśnij spację\n Jeśli nie, wciśnij q",align="center", font=("Courier",12,"normal"))
        okno.listen()
        okno.onkeypress(zakoncz,"q")
        okno.onkeypress(restartgry,"space")


    def zakoncz():
        okno.bye()

    def restartgry():
        okno.clear()
        run_game()


# Główna pętla gry

    

    while True:

        # naliczanie punktów

        czas=time.time()

        stan_punktow=round((czas-czas_pocz)*10)
        punkty.clear()
        punkty.write("Wynik: {}".format(stan_punktow), align = "center", font=("Courier",15,"normal"))

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

        #poruszanie pterodaktylem
        x = pterodaktyl.xcor()
        x+= pterodaktyl.dx
        pterodaktyl.setx(x)

        if pterodaktyl.xcor()<-400:
            x=random.randint(400,600)
            pterodaktyl.setx(x)
            pterodaktyl.dx*=1.05
            print(pterodaktyl.dx)

        #kolizja z pierwszym kaktusem
        if -290 < kaktus_1.xcor() < -210:
            if kaktus_1.xcor() -34 < dino.xcor() and dino.ycor() < -10:
                koniec()
                turtle.done()


        #kolizja z drugim kaktusem
        if -290 < kaktus_2.xcor() < -210:
            if kaktus_2.xcor() -34 < dino.xcor() and dino.ycor() < -10:
                koniec()
                turtle.done()

                      
        #kolizja z pterodaktylem              
        if -290<pterodaktyl.xcor()<-210:
            if pterodaktyl.xcor()-34 <dino.xcor()and dino.ycor()<50 and dino.ycor()>10:
                koniec()
                turtle.done() 

    

        okno.update()

run_game()
