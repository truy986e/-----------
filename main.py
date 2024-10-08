import pygame
import sys
import random

pygame.init()

# Загрузка изображений и настроек
lvlbg = 1
lvlskin = 1
x = 1
y = 1
costx = 10
costy = 10
bg = 'bg'+ str(lvlbg) +'.png'
skin = 'c'+str(lvlskin)+'.png'
spike = 'spike.png'
spike1 = 'spike1.png'
game = 'g1.png'
mouse_img = 'mouse.png'
gold = 'goldcoin.png'
silver = 'silvercoin.png'
background = pygame.image.load(bg)
spikes = pygame.image.load(spike)
spikes1 = pygame.image.load(spike1)
goldcoin = pygame.image.load(gold)
silvercoin = pygame.image.load(silver)
game1 = pygame.image.load(game)
coin = pygame.image.load(skin)
mouse = pygame.image.load(mouse_img)
font = pygame.font.SysFont('times', 60)
font1 = pygame.font.SysFont('times', 95)
font2 = pygame.font.SysFont('times', 65)

# Основной экран
screen = pygame.display.set_mode((500, 800))
score0 = 0
score00 = 0
multitap = 1

# Функция для отрисовки основного меню
def main_menu():
    global score0
    while True:
        screen.blit(background, (0, 0))
        screen.blit(coin, (80, 250))
        # Отображение счета
        score = font.render(f'{score0}', True, 'Silver', None)
        screen.blit(silvercoin, (180, 25))
        score1 = score.get_rect()
        score1.center = (140, 50)
        screen.blit(score, score1)

        scoreg = font.render(f'{score00}', True, 'Gold', None)
        screen.blit(goldcoin, (390, 25))
        scoreg1 = scoreg.get_rect()
        scoreg1.center = (350, 50)
        screen.blit(scoreg, scoreg1)

        # Отображение кнопок
        shopb = font1.render('SHOP', True, 'White', 'Black')
        shopb1 = shopb.get_rect()
        shopb1.center = (120, 750)
        gameb = font1.render('PLAY', True, 'White', 'Black')
        gameb1 = gameb.get_rect()
        gameb1.center = (380, 750)

        screen.blit(shopb, shopb1)
        screen.blit(gameb, gameb1)

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse, mouse_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shopb1.collidepoint(event.pos):
                    shop()
                elif gameb1.collidepoint(event.pos):
                    play()
                elif screen.blit(coin, (70, 250)).collidepoint(event.pos):
                    score0 += multitap
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Функция для окна магазина
def shop():
    global bg, background, score0, lvlbg, skin, lvlskin, coin, x, y, costx, costy
    while True:
        screen.fill((0, 128, 0))  # Заливка фона магазина (например, черным цветом)

        backb = font1.render('BACK', True, 'White', 'Black')
        backb1 = backb.get_rect()
        backb1.center = (250, 750)

        upb = font2.render('UPGRADE HOME', True, 'White', 'Black')
        upb1 = upb.get_rect()
        upb1.center = (250, 50)

        upsb = font2.render('UPGRADE SKIN', True, 'White', 'Black')
        upsb1 = upsb.get_rect()
        upsb1.center = (250, 400)

        screen.blit(backb, backb1)
        screen.blit(upb, upb1)
        screen.blit(upsb, upsb1)

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse, mouse_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backb1.collidepoint(event.pos):
                    return  # Возврат в главное меню
                if upb1.collidepoint(event.pos) and score0 >= costx:
                    lvlbg += x
                    bg = 'bg' + str(lvlbg) + '.png'
                    background = pygame.image.load(bg)
                    score0 -= costx
                    if lvlbg == 10:
                        print("You win")
                        x = 0
                        costx = 0
                        return
                if upsb1.collidepoint(event.pos) and score0 >= costy:
                    lvlskin += y
                    skin = 'c' + str(lvlskin) + '.png'
                    coin = pygame.image.load(skin)
                    score0 -= costy
                    if lvlskin == 7:
                        y = 0
                        costy = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Функция проверки столкновения
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Функция для окна игры
def play():
    global spikes, game, game1, goldcoin, score00
    width = 0
    height = 300
    size = 0
    gold_rect = goldcoin.get_rect(center=(random.randint(50, 450), random.randint(100, 500)))
    while True:
        if width <= 0:
            speedw = 20
            size = 0
            gold_rect = goldcoin.get_rect(center=(random.randint(50, 450), random.randint(100, 500)))
        if width >= 400:
            speedw = -20
            size = 1
            gold_rect = goldcoin.get_rect(center=(random.randint(50, 450), random.randint(100, 500)))
        width += speedw
        height += 30
        screen.fill((0, 128, 0))  # Заливка фона игры (например, зеленым цветом)
        for i in range(10):
            screen.blit(spikes, (50 * i, 600))
            screen.blit(spikes1, (50 * i, 0))
        screen.blit(game1, (width, height))
        screen.blit(goldcoin, gold_rect)
        backb = font1.render('BACK', True, 'White', 'Black')
        backb1 = backb.get_rect()
        backb1.center = (250, 750)

        screen.blit(backb, backb1)
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse, mouse_pos)
        pygame.display.flip()
        pygame.time.delay(200)
        if size == 0:
            game = 'g1.png'
            game1 = pygame.image.load(game)
        elif size == 1:
            game = 'g11.png'
            game1 = pygame.image.load(game)

        game_rect = game1.get_rect(topleft=(width, height))

        if check_collision(game_rect, gold_rect):
            score00 += 1
            gold_rect.center = (random.randint(50, 450), random.randint(100, 500))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backb1.collidepoint(event.pos):
                    return  # Возврат в главное меню
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE] and speedw == 20:
                    height -= 100
                    game = 'g2.png'
                    game1 = pygame.image.load(game)
                if pygame.key.get_pressed()[pygame.K_SPACE] and speedw == -20:
                    height -= 100
                    game = 'g21.png'
                    game1 = pygame.image.load(game)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Запуск основного меню
main_menu()
