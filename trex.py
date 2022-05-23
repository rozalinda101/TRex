import pygame
import time
pygame.init()

#rozmiar wyswietlacza określam
rozmiar=szer,wys=700,400
wyswietlacz=pygame.display.set_mode(rozmiar)
pygame.display.set_caption("T-rex")

#określam oznaczenia kolorow w rgb
szary1=150,150,150
szary2=110,110,110
bialy=255,255,255

#okreslam rozmiar "dinozaura"
wys_dino=40
szer_dino=30


#okreslam klasę obiektu dinozaur
class dino():
    def __init__(self):
        #okreslam pozycje dinozaura na ekranie
        self.wys_na_wysw=200  #######CO OZNACZAJĄ SKRÓTY WYS_NA_WYSW POZ_NA_SZERA DO CZEGO TO SIĘ OD NOSI, NIE MOGĘ TEGO ZROZUMIEĆ, HELP XD
        self.poz_na_szera=200
        #przypisuje rozmiar dinozaura
        self.wys=wys_dino
        self.szer=szer_dino

    #rysuję dino
    def narysuj(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,szary2,[self.poz_na_szera,self.wys_na_wysw,self.szer,self.wys])


    #skakanie - zmieniam pozycję, wymazuję tego co na ziemi, chwila skoku - 0,5 sekundy, zmieniam pozycję znowy na ziemię
    def skakanie(self,wyswietlacz):
        self.wys_na_wysw -= 70
        pygame.display.update()


#okreslam klase kaktus
class kaktus():
    def __init__(self):
        #okreslam pozycje kaktusa na ekranie
        self.wys_na_wysw=190
        self.poz_na_szer=700
        #przypisuje rozmiar kaktusa
        self.wys=50
        self.szer=20


    #rysuję "kaktusa"
    def narysuj(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,szary2,[self.poz_na_szer,self.wys_na_wysw,self.szer,self.wys])


    #poruszanie - zmieniam pozycję, wymazuję, zmieniam pozycję znowu
    def poruszanie(self,wyswietlacz):
        self.poz_na_szer-=0.1
        self.narysuj(wyswietlacz)
        pygame.display.update()



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


    pygame.display.update()



pygame.quit()
