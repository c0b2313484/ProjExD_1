import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #1
    kt_img = pg.image.load("fig/3.png") #2_読み込み
    kt_img = pg.transform.flip(kt_img, True, False) #2_左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) #3
        kt_rct = kt_img.get_rect() #4_こうかとん画像rectを取得する
        kt_rct.center = 300, 200
        screen.blit(kt_img, kt_rct) #kt_img画像をkt_rctに貼る
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()