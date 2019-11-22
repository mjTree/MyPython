# -*- coding: utf-8 -*-
import pygame
import random
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.active = False     #默认不激活

    def move(self):
        #激活状态下，向上移动
        if self.active:
            self.y -= 3
        #当飞出屏幕，就设为不激活
        if self.y < 0:
            self.active = False

    def restart(self):
        #重置子弹位置
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        #激活子弹
        self.active = True

class Enemy:
    def restart(self):
        #重置敌机位置和速度
        self.x = random.randint(50, 400)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.1
        
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('enemy.png').convert_alpha()

    def move(self):
        if self.y < 650:
            self.y += self.speed
        else:
            self.restart()

class Plane:
    def restart(self):
        self.x = 200
        self.y = 600
        
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('plane.png').convert_alpha()

    def move(self):
        x, y = pygame.mouse.get_pos()
        x-= self.image.get_width() / 2
        y-= self.image.get_height() / 2
        self.x = x
        self.y = y

#检测是否碰撞
def checkHit(enemy, bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (
        bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()
    ):
        enemy.restart()
        bullet.active = False
        #增加返回值
        return True
    return False

def checkCrash(enemy, plane):
    if (plane.x + 0.7*plane.image.get_width() > enemy.x) and (
        plane.x + 0.3*plane.image.get_width() < enemy.x + enemy.image.get_width()) and (
        plane.y + 0.7*plane.image.get_height() > enemy.y) and (
        plane.y + 0.3*plane.image.get_width() < enemy.y + enemy.image.get_height()
    ):
        return True
    return False

pygame.init()
screen = pygame.display.set_mode((450, 650), 0, 32)
pygame.display.set_caption("又可以打飞机啦")
background = pygame.image.load('back.jpg').convert()

plane = Plane()
bullets = []    #创建子弹list
for i in range(5):
    bullets.append(Bullet())
count_b = len(bullets)      #子弹总数
index_b = 0                 #即将激活的子弹序号
interval_b = 0              #发射子弹的间隔

enemies = []
for i in range(5):
    enemies.append(Enemy())
gameover = False

score = 0   #分数

#用以显示文字的font变量
font = pygame.font.Font(None, 32)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #判断在gameover状态下点击了鼠标
        if gameover and event.type == pygame.MOUSEBUTTONUP:
            #重置游戏
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active = False
            score = 0
            gameover = False
    screen.blit(background, (0,0))
    if not gameover:
        interval_b -= 1
        if interval_b < 0:
            bullets[index_b].restart()
            interval_b = 200
            index_b = (index_b + 1) % count_b
        for b in bullets:
            if b.active:
                for e in enemies:
                    #击中敌机后，分数加100
                    if checkHit(e, b):
                        score += 100
                b.move()
                screen.blit(b.image, (b.x, b.y))
        for e in enemies:
            if checkCrash(e, plane):
                gameover = True
            e.move()
            screen.blit(e.image, (e.x, e.y))
        plane.move()
        screen.blit(plane.image, (plane.x, plane.y))
        #在屏幕左上角显示分数
        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (0, 0))
    else:
        #在屏幕中央显示分数
        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (190, 400))
        pass
    pygame.display.update()

