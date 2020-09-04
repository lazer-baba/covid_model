

import sys, pygame
from random import *
import random
import time

start = time.time()
elapsed = 0
c = 0


img_file1 = "gball.png"
img_file2 = "rball.png"
img_file3 = "buball.png"
img_file4 = "bkball.png"
img_file5 = "oball.png"


class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, img_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left - 5 < 0 or self.rect.right + 5 > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top - 5 < 0 or self.rect.bottom + 5 > height:
            self.speed[1] = -self.speed[1]


def animation(groupall):
    screen.fill([255, 255, 255])

    for ball in grouphealty:
        grouphealty.remove(ball)
        if pygame.sprite.spritecollide(ball, grouphealty, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        grouphealty.add(ball)
        groupall.add(ball)
        ball.move()
        screen.blit(ball.image, ball.rect)

    r2 = random.randrange(0, 100, 1)
    if r2 % 10 == 0:
        for ball in grouphealty:
            grouphealty.remove(ball)
            if pygame.sprite.spritecollide(ball, groupinfecteds, False):
                ball.image = pygame.image.load("oball.png")
                ball.speed[0] = -ball.speed[0]
                ball.speed[1] = -ball.speed[1]
                groupinfecteds.add(ball)
                groupall.add(ball)
            else:
                grouphealty.add(ball)
                groupall.add(ball)

            ball.move()
            screen.blit(ball.image, ball.rect)


    else:
        for ball in grouphealty:
            grouphealty.remove(ball)
            if pygame.sprite.spritecollide(ball, groupinfecteds, False):
                ball.image = pygame.image.load("rball.png")
                ball.speed[0] = -ball.speed[0]
                ball.speed[1] = -ball.speed[1]
                groupinfecteds.add(ball)
                groupall.add(ball)
            else:
                grouphealty.add(ball)
                groupall.add(ball)

            ball.move()
            screen.blit(ball.image, ball.rect)


    for ball in groupinfecteds:
        groupinfecteds.remove(ball)
        if pygame.sprite.spritecollide(ball, groupinfecteds, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        groupinfecteds.add(ball)
        groupall.add(ball)
        ball.move()
        screen.blit(ball.image, ball.rect)

    for ball in groupinfecteds:
        groupinfecteds.remove(ball)
        if pygame.sprite.spritecollide(ball, grouphealty, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        groupinfecteds.add(ball)
        groupall.add(ball)
        ball.move()
        screen.blit(ball.image, ball.rect)

    for ball in groupinfecteds:
        groupinfecteds.remove(ball)
        elapsed = time.time() - start
        r1 = random.randrange(0, 9000, 1)
        if elapsed > 10:
            if r1 % 555 == 0:
                ball.image = pygame.image.load("buball.png")
        groupinfecteds.add(ball)
        groupall.add(ball)

        ball.move()
        screen.blit(ball.image, ball.rect)


    for ball in groupinfecteds:

        elapsed = time.time() - start
        r1 = random.randrange(0, 9000, 1)
        c = len(groupdead.sprites())
        if elapsed > 10 and c < 5:
            if r1 % 5555 == 0:
                groupinfecteds.remove(ball)
                ball.image = pygame.image.load("bkball.png")
                ball.speed[0] = 0
                ball.speed[1] = 0
                c=c+1
                groupdead.add(ball)
        groupall.add(ball)

        ball.move()
        screen.blit(ball.image, ball.rect)

    for ball in groupall:
        screen.blit(ball.image, ball.rect)


    pygame.display.flip()
    pygame.time.delay(20)


size = width, height = 1200, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Cronavirus Model of a City')
screen.fill([255, 255, 255])

grouphealty = pygame.sprite.Group()
groupinfecteds = pygame.sprite.Group()
groupinfectedwos = pygame.sprite.Group()
groupallinfected = pygame.sprite.Group()
groupdead = pygame.sprite.Group()
groupall = pygame.sprite.Group()

for r in range(0, 147):
    location = [random.randrange(10, width - 10, 20), random.randrange(10, height - 10, 20)]
    speed = [choice([-1, 1]), choice([-1, 1])]
    ball = MyBallClass(img_file1, location, speed)
    grouphealty.add(ball)
    groupall.add(ball)

for r in range(0, 3):
    location = [random.randrange(10, width - 10, 20), random.randrange(10, height - 10, 20)]
    speed = [choice([-1, 1]), choice([-1, 1])]
    ball = MyBallClass(img_file2, location, speed)
    groupinfecteds.add(ball)
    groupall.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animation(groupall)
    groupall.update()
