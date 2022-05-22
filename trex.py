import pygame
import time
pygame.init()

#rozmiar wyswietlacza określam
rozmiar=szer,wys=700,400
wyswietlacz=pygame.display.set_mode(rozmiar)

#określam oznaczenia kolorow w rgb
szary1=150,150,150
szary2=110,110,110
bialy=255,255,255

#okreslam rozmiar "dinozaura"
wys_dino=40
szer_dino=20

#okreslam klasę obiektu dinozaur
class dino():
    def __init__(self):
        #okreslam pozycje dinozaura na ekranie
        self.wys_na_wysw=200
        self.poz_na_szer=200
        #przypisuje rozmiar dinozaura
        self.wys=wys_dino
        self.szer=szer_dino

    #rysuję "dinozaura"
    def narysuj(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,szary2,[self.poz_na_szer,self.wys_na_wysw,self.szer,self.wys])

    #wymazuję dinozaura przy skakaniu
    def zniknij(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,bialy,[self.poz_na_szer,self.wys_na_wysw,self.szer,self.wys])

    #skakanie - zmieniam pozycję, wymazuję tego co na ziemi, chwila skoku - 0,5 sekundy, zmieniam pozycję znowy na ziemię
    def skakanie(self,wyswietlacz):
        self.zniknij(wyswietlacz)
        self.wys_na_wysw-=70
        self.narysuj(wyswietlacz)
        pygame.display.update()
        time.sleep(0.5)
        self.zniknij(wyswietlacz)
        self.wys_na_wysw+=70
        self.narysuj(wyswietlacz)
        pygame.display.update()


#okreslam klase kaktus
class kaktus():
    def __init__(self):
        #okreslam pozycje kaktusa na ekranie
        self.wys_na_wysw=180
        self.poz_na_szer=700
        #przypisuje rozmiar kaktusa
        self.wys=60
        self.szer=20

    #rysuję "kaktusa"
    def narysuj(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,szary2,[self.poz_na_szer,self.wys_na_wysw,self.szer,self.wys])

    #wymazuję kaktusa przy poruszaniu
    def zniknij(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,bialy,[self.poz_na_szer,self.wys_na_wysw,self.szer,self.wys])

    #poruszanie - zmieniam pozycję, wymazuję, zmieniam pozycję znowu
    def poruszanie(self,wyswietlacz):
        self.zniknij(wyswietlacz)
        self.poz_na_szer-=3
        self.narysuj(wyswietlacz)
        pygame.display.update()
        time.sleep(0.1)


dinozaur=dino()

kaktus1=kaktus()

# kaktus2=kaktus()

while True:
    #wypełniam wyświetlacz białym
    wyswietlacz.fill(bialy)
    #rysuję ziemię
    pygame.draw.rect(wyswietlacz,szary1,[0,240,700,160])
    #rysuję "dinozaura"
    dinozaur.narysuj(wyswietlacz)
    #rysuję kaktusa
    kaktus1.narysuj(wyswietlacz)
    #poruszam kaktusa
    kaktus1.poruszanie(wyswietlacz)
    for event in pygame.event.get():
        #zeby się gra zatrzymala w pewnym momencie
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        #żeby przy naciśnieciu spacji dinozaur skakał
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                dinozaur.skakanie(wyswietlacz)
                #żeby nie dało się cały czas skakać
                time.sleep(0.5)

    pygame.display.update()



pygame.quit()
