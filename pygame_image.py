import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg2_img =pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img2 = pg.transform.rotozoom(kk_img,10,1.0)
    kk_img3 = pg.transform.rotozoom(kk_img,3,1.0)
    kk_img4 = pg.transform.rotozoom(kk_img,7,1.0)
    kk_img5 = pg.transform.rotozoom(kk_img,1,1.0)
    kk_img6 = pg.transform.rotozoom(kk_img,2,1.0)
    kk_img7 = pg.transform.rotozoom(kk_img,4,1.0)
    kk_img8 = pg.transform.rotozoom(kk_img,5,1.0)
    kk_img9 = pg.transform.rotozoom(kk_img,6,1.0)
    kk_img10 = pg.transform.rotozoom(kk_img,8,1.0)
    kk_img11 = pg.transform.rotozoom(kk_img,9,1.0)
    kk_lmgs = [kk_img,kk_img5,kk_img6,kk_img3,kk_img7,kk_img8,kk_img9,kk_img4,kk_img10,kk_img11,kk_img2]
    
    
    


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #x = - 2  *  tmr
        x = tmr

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img,[1600-x,0])
        screen.blit(kk_lmgs[tmr%11],[300,200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()