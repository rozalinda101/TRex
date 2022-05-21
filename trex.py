import pygame
import time
pygame.init()

rozmiar=szer,wys=700,400
wyswietlacz=pygame.display.set_mode(rozmiar)

szary1=150,150,150
szary2=110,110,110
bialy=255,255,255

wys_dino=40
szer_dino=20

class dino:
    def __init__(self):
        self.wys_na_wysw=200
        self.poz_na_szer=200
        self.wys=wys_dino
        self.szer=szer_dino

    def narysuj(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,szary2,[self.poz_na_szer,self.wys_na_wysw,self.szer,self.wys])

    def zniknij(self,wyswietlacz):
        pygame.draw.rect(wyswietlacz,bialy,[self.poz_na_szer,self.wys_na_wysw,self.szer,self.wys])

    def skakanie(self,wyswietlacz):
        self.zniknij(wyswietlacz)
        self.wys_na_wysw-=60
        self.narysuj(wyswietlacz)
        pygame.display.update()
        time.sleep(0.5)
        self.zniknij(wyswietlacz)
        self.wys_na_wysw+=60
        self.narysuj(wyswietlacz)
        pygame.display.update()



dinozaur=dino()

while True:
    wyswietlacz.fill(bialy)
    pygame.draw.rect(wyswietlacz,szary1,[0,240,700,160])
    dinozaur.narysuj(wyswietlacz)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                dinozaur.skakanie(wyswietlacz)
                time.sleep(0.5)


    pygame.display.update()



pygame.quit()
