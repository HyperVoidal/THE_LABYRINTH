import pygame
import time as t
import os
cur_dir = os.path.dirname(__file__)
# pygame setup
pygame.init()
world = pygame.display.set_mode((800, 800))
pygame.display.set_caption(f"{cur_dir}/Maze Game")
clock = pygame.time.Clock()
running = True
playerx = 120
playery = 480
iconx = playerx
icony = playery
enemyx = 400
enemyy = 10
bg = pygame.image.load(f"{cur_dir}/maze.png")
background = pygame.transform.scale(bg, (835, 835))
imga = pygame.image.load(f"{cur_dir}/Hero.png")
img = pygame.transform.scale(imga, (25, 25))

def pursuer():
    pursimg = pygame.image.load(f"{cur_dir}/monster.png") #Put path for monster png here
    pursuer = pygame.draw.rect(world, (0, 255, 0), (enemyx, enemyy, 30, 30))

def wallcaller():
    wall1()
    wall2()
    wall3()
    wall4()
    wall5()
    wall6()
    wall7()
    wall8()
    wall9()
    wall10()
    wall11()
    wall12()
    wall13()
    wall14()
    wall15()
    wall16()
    wall17()
    wall18()
    wall19()
    wall20()
    wall21()
    wall22()
    wall23()
    wall24()
    wall25()
    wall26()
    wall27()
    wall28()
    wall29()
    wall30()
    wall31()
    wall32()
    wall33()
    wall34()
    wall35()
    wall36()
    wall37()
    wall38()
    wall39()

def wall1():
    pygame.draw.rect(world, (0, 0, 0), rect2)
def wall2():
    pygame.draw.rect(world, (0, 0, 0), rect3)
def wall3():
    pygame.draw.rect(world, (0, 0, 0), rect4)
def wall4():
    pygame.draw.rect(world, (0, 0, 0), rect5)
def wall5():
    pygame.draw.rect(world, (0, 0, 0), rect6)
def wall6():
    pygame.draw.rect(world, (0, 0, 0), rect7)
def wall7():
    pygame.draw.rect(world, (0, 0, 0), rect8)
def wall8():
    pygame.draw.rect(world, (0, 0, 0), rect9)
def wall9():
    pygame.draw.rect(world, (0, 0, 0), rect10)
def wall10():
    pygame.draw.rect(world, (0, 0, 0), rect11)
def wall11():
    pygame.draw.rect(world, (0, 0, 0), rect12)
def wall12():
    pygame.draw.rect(world, (0, 0, 0), rect13)
def wall13():
    pygame.draw.rect(world, (0, 0, 0), rect14)
def wall14():
    pygame.draw.rect(world, (0, 0, 0), rect15)
def wall15():
    pygame.draw.rect(world, (0, 0, 0), rect16)
def wall16():
    pygame.draw.rect(world, (0, 0, 0), rect17)
def wall17():
    pygame.draw.rect(world, (0, 0, 0), rect18)
def wall18():
    pygame.draw.rect(world, (0, 0, 0), rect19)
def wall19():
    pygame.draw.rect(world, (0, 0, 0), rect20)
def wall20():
    pygame.draw.rect(world, (0, 0, 0), rect21)
def wall21():
    pygame.draw.rect(world, (0, 0, 0), rect22)
def wall22():
    pygame.draw.rect(world, (0, 0, 0), rect23)
def wall23():
    pygame.draw.rect(world, (0, 0, 0), rect24)
def wall24():
    pygame.draw.rect(world, (0, 0, 0), rect25)
def wall25():
    pygame.draw.rect(world, (0, 0, 0), rect26)
def wall26():
    pygame.draw.rect(world, (0, 0, 0), rect27)
def wall27():
    pygame.draw.rect(world, (0, 0, 0), rect28)
def wall28():
    pygame.draw.rect(world, (0, 0, 0), rect29)
def wall29():
    pygame.draw.rect(world, (0, 0, 0), rect30)
def wall30():
    pygame.draw.rect(world, (0, 0, 0), rect31)
def wall31():
    pygame.draw.rect(world, (0, 0, 0), rect32)
def wall32():
    pygame.draw.rect(world, (0, 0, 0), rect33)
def wall33():
    pygame.draw.rect(world, (0, 0, 0), rect34)
def wall34():
    pygame.draw.rect(world, (0, 0, 0), rect35)
def wall35():
    pygame.draw.rect(world, (0, 0, 0), rect36)
def wall36():
    pygame.draw.rect(world, (0, 0, 0), rect37)
def wall37():
    pygame.draw.rect(world, (0, 0, 0), rect38)
def wall38():
    pygame.draw.rect(world, (0, 0, 0), rect39)
def wall39():
    pygame.draw.rect(world, (0, 0, 0), rect40)

rect1 = pygame.Rect(758, 250, 25, 25)
rect2 = pygame.Rect(0, 0, 20, 800)
rect3 = pygame.Rect(0, 0, 1000, 12)
rect4 = pygame.Rect(788, 0, 20, 1000)
rect5 = pygame.Rect(0, 788, 1000, 12)
rect6 = pygame.Rect(728, 360, 60, 20)
rect7 = pygame.Rect(728, 255, 20, 110)
rect8 = pygame.Rect(678, 150, 100, 20)
rect9 = pygame.Rect(730, 150, 20, 50)
rect10 = pygame.Rect(620, 200, 120, 20)
rect11 = pygame.Rect(628, 255, 120, 20)
rect12 = pygame.Rect(623, 100, 20, 100)
rect13 = pygame.Rect(573, 100, 60, 20)
rect14 = pygame.Rect(572, 120, 20, 205)
rect15 = pygame.Rect(623, 275, 20, 55)
rect16 = pygame.Rect(676, 315, 20, 50)
rect17 = pygame.Rect(570, 358, 105, 20)
rect18 = pygame.Rect(208, 255, 360, 20)
rect19 = pygame.Rect(462, 277, 20, 40)
rect20 = pygame.Rect(515, 310, 20, 100)
rect21 = pygame.Rect(311, 310, 210, 20)
rect22 = pygame.Rect(518, 412, 48, 20)
rect23 = pygame.Rect(573, 379, 20, 150)
rect24 = pygame.Rect(625, 412, 120, 20)
rect25 = pygame.Rect(728, 412, 20, 180)
rect26 = pygame.Rect(593, 466, 98, 20)
rect27 = pygame.Rect(671, 466, 20, 280)
rect28 = pygame.Rect(572, 727, 100, 20)
rect29 = pygame.Rect(572, 529, 20, 200)
rect30 = pygame.Rect(725, 625, 60, 20)
rect31 = pygame.Rect(725, 625, 20, 120)
rect32 = pygame.Rect(0, 0, 0, 0)
rect33 = pygame.Rect(0, 0, 0, 0)
rect34 = pygame.Rect(0, 0, 0, 0)
rect35 = pygame.Rect(0, 0, 0, 0)
rect36 = pygame.Rect(0, 0, 0, 0)
rect37 = pygame.Rect(0, 0, 0, 0)
rect38 = pygame.Rect(0, 0, 0, 0)
rect39 = pygame.Rect(0, 0, 0, 0)
rect40 = pygame.Rect(0, 0, 0, 0)

previous_x, previous_y = 0, 0
x_change, y_change = 0, 0

speed = 3

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -speed
                y_change = 0
            if event.key == pygame.K_d:
                x_change = speed
                y_change = 0
            if event.key == pygame.K_s:
                y_change = speed
                x_change = 0
            if event.key == pygame.K_w:
                y_change = -speed
                x_change = 0
            if event.key == pygame.K_p:
                print("x = " + str(rect1.x) + " y = " + str(rect1.y))

        if event.type == pygame.KEYUP:
            x_change = 0
            y_change = 0

    world.fill((255, 255, 255))


    #world.blit(bg, ((0), (0))) #this is the maze background
    pursuer()
    previous_x = rect1.x
    previous_y = rect1.y

    rect1.x = rect1.x + x_change
    rect1.y = rect1.y + y_change
    playerx = rect1.x
    playery = rect1.y

    if rect1.colliderect(rect2) or rect1.colliderect(rect3) or rect1.colliderect(rect4) or rect1.colliderect(rect5) or rect1.colliderect(rect6) or rect1.colliderect(rect7) or rect1.colliderect(rect8) or rect1.colliderect(rect9) or rect1.colliderect(rect10):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect11) or rect1.colliderect(rect12) or rect1.colliderect(rect13) or rect1.colliderect(rect14) or rect1.colliderect(rect15) or rect1.colliderect(rect16) or rect1.colliderect(rect17) or rect1.colliderect(rect18) or rect1.colliderect(rect19):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect20) or rect1.colliderect(rect21) or rect1.colliderect(rect22) or rect1.colliderect(rect23) or rect1.colliderect(rect24) or rect1.colliderect(rect25) or rect1.colliderect(rect26) or rect1.colliderect(rect27) or rect1.colliderect(rect28) or rect1.colliderect(rect29) or rect1.colliderect(rect30):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect31) or rect1.colliderect(rect32) or rect1.colliderect(rect33) or rect1.colliderect(rect34) or rect1.colliderect(rect35) or rect1.colliderect(rect36) or rect1.colliderect(rect37) or rect1.colliderect(rect38) or rect1.colliderect(rect39) or rect1.colliderect(rect40):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    wallcaller()
    
    pygame.draw.rect(world, (255, 255, 255), rect1, 1)

    world.blit(img, (playerx, playery))
    world.blit(background, ((-20), (-20)))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()