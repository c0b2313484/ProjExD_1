import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #1
    bg_img_2 = pg.transform.flip(bg_img, True, False) #7_1:反転した画像
    kt_img = pg.image.load("fig/3.png") #2_読み込み
    kt_img = pg.transform.flip(kt_img, True, False) #2_左右反転
    kt_rct = kt_img.get_rect() #4_こうかとん画像rectを取得する
    kt_rct.center = 300, 200 #8-2
    tmr = 0
    count = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 #6
        screen.blit(bg_img, [-x, 0]) #3
        screen.blit(bg_img_2, [-x+1600, 0]) #7-1
        screen.blit(bg_img, [-x+3200, 0]) #7-2
        screen.blit(bg_img_2, [-x+4800, 0]) #7-2

        key_lst = pg.key.get_pressed() #全キーの押下状態のリストを取得
        # kt_rct.move_ip((mv))
        mv = [-1, 0]
        if key_lst[pg.K_UP]: #上矢印が押されていたら
            # kt_rct.move_ip((-1, -1))
            mv[0] -= 1
            mv[1] -= 1
        if key_lst[pg.K_DOWN]:
            # kt_rct.move_ip((2, 1))
            mv[0] += 2
            mv[1] += 1
        if key_lst[pg.K_RIGHT]:
            # kt_rct.move_ip((2, 0))
            mv[0] += 2
        if key_lst[pg.K_LEFT]:
            # kt_rct.move_ip((-1, 0))
            mv[0] -= 1
        kt_rct.move_ip((mv))
        screen.blit(kt_img, kt_rct) #kt_img画像をkt_rctに貼る
        pg.display.update()
        tmr += 1        
        clock.tick(200) #5_FPSの変更    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()