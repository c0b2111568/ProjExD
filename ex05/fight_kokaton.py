import pygame as pg
import sys
from random import randint
import pygame
import time
from pygame.locals import *
import sys

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Text:
    def __init__(self, size, txt, color, xy):
        self.font = pg.font.Font(None, size)
        self.txt = self.font.render(txt, True, color)
        self.x, self.y = xy
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.txt, (self.x, self.y))


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        if yoko == -1 or tate ==-1: 
            self.vx *=1.2
            self.vy *=1.2
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Music:
    def __init__(self,BGM):
        pygame.mixer.init(frequency = 44100)    # 初期設定
        pygame.mixer.music.load(BGM)     # 音楽ファイルの読み込み
        pygame.mixer.music.play(1)              # 再生の終了
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                pygame.mixer.music.stop()
                return

    def se(se):
        pygame.mixer.init(frequency = 44100)    # 初期設定
        pygame.mixer.music.load(se)     # 音楽ファイルの読み込み
        pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
        time.sleep(1)
        pygame.mixer.music.stop()               # 再生の終了
        return 0


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    pygame.mouse.set_visible(False) #画面にマウスポインタを表示させなくする

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (900, 400))

    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)

    clock = pg.time.Clock() # 練習1

    Music("MP3/BGM.mp3")

    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        bkd.update(scr)

        s = pg.time.get_ticks()
        time = Text(80, str(s/1000), "Black", (50, 50))
        time.blit(scr)

        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            Music.se("MP3/bomb.mp3")
            return

        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()