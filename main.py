import pygame
import sys
pygame.init()
bg='bg1.png'
skin='c1.png'
screen=pygame.display.set_mode((500,800))
background=pygame.image.load(bg)
coin=pygame.image.load(skin)
mouse=pygame.image.load('mouse.png')
font=pygame.font.SysFont('times',50)
font1=pygame.font.SysFont('times',95)
score0=0
multitap=1
score=font.render(f'{score0}',True,'White',None)
score1=score.get_rect()
score1.center=(250,50)
mouse_pos=pygame.mouse.get_pos()
while True:
    score=font.render(f'{score0}',True,'White',None)
    score1=score.get_rect()
    score1.center=(250,50)
    shopb=font1.render('SHOP',True,'White','Black')
    shopb1=shopb.get_rect()
    shopb1.center=(120,750)
    gameb=font1.render('PLAY',True,'White','Black')
    gameb1=gameb.get_rect()
    gameb1.center=(380,750)
    mouse_pos=pygame.mouse.get_pos()
    #a=pygame.Rect(110,240,300,300)
    #b=pygame.Rect()
    screen.blit(background, (0,0))
    a=screen.blit(coin, (70,250))
    screen.blit(score,score1)
    shop=screen.blit(shopb,shopb1)
    game=screen.blit(gameb,gameb1)
    #screen.blit(coin1, (260,50))
    c=screen.blit(mouse, (mouse_pos))
    # if c in a and event.type==pygame.MOUSEBUTTONDOWN:
    #     score0+=1       
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and c in a:
            score0+=multitap
        if event.type==pygame.MOUSEBUTTONDOWN and c in shop:
            screen_shop=pygame.display.set_mode((500,500))
        if event.type==pygame.MOUSEBUTTONDOWN and c in game:
            screen_game=pygame.display.set_mode((500,500))
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
