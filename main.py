import pygame
import sys
import random

pygame.init()

# Загрузка изображений и настроек
lvlbg = 1
lvlskin = 1
lvlbg1=1
lvlskin1=1
win = 1
x = 1
y = 1
costx = 10
costy = 10
bg = 'bg' + str(lvlbg) + '.png'
bg1='bg1'+str(lvlbg1)+'.png'
skin = 'c' + str(lvlskin) + '.png'
skin1 = 'c1' + str(lvlskin1) + '.png'
spike = 'spike.png'
spike1 = 'spike1.png'
spiker = 'spiker.png'
spikel = 'spikel.png'
upgradeskin='upgradeskin.png'
upgradehome='upgradehome.png'
game = 'g1.png'
mouse_img = 'mouse.png'
gold = 'goldcoin.png'
silver = 'silvercoin.png'
upgradeskin1=pygame.image.load((upgradeskin))
upgradehome1=pygame.image.load((upgradehome))
spiker1 = pygame.image.load(spiker)
spikel1 = pygame.image.load(spikel)
background = pygame.image.load(bg)
background1 = pygame.image.load(bg1)
spikes = pygame.image.load(spike)
spikes1 = pygame.image.load(spike1)
goldcoin = pygame.image.load(gold)
silvercoin = pygame.image.load(silver)
game1 = pygame.image.load(game)
skins=pygame.image.load(skin1)
coin = pygame.image.load(skin)
mouse = pygame.image.load(mouse_img)
font0 = pygame.font.SysFont('times', 30)
font = pygame.font.SysFont('times', 60)
font1 = pygame.font.SysFont('times', 95)
font2 = pygame.font.SysFont('times', 65)
font_bold = pygame.font.SysFont('times', 35, bold=True)

# Основной экран
screen = pygame.display.set_mode((500, 800))
score0 = 893
score00 = 400
multitap = 1
cost = 100
costg = 10
widthskins1=50
widthskins2=50
# Функция для отрисовки основного меню
def main_menu():
    global score0, score00
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
        shopb = pygame.image.load('shop_button.png')
        shopb1 = shopb.get_rect()
        shopb1.center = (120, 740)
        gameb = pygame.image.load('play_button.png')
        gameb1 = gameb.get_rect()
        gameb1.center = (380, 740)

        cost1 = font_bold.render(f'Cost {cost}', True, 'Black', None)
        cost0 = cost1.get_rect()
        cost0.center = (360, 675)
        screen.blit(cost1, cost0)
        screen.blit(silvercoin, (cost0.right + 10, cost0.centery - silvercoin.get_height() // 2))


        screen.blit(shopb, shopb1)
        screen.blit(gameb, gameb1)

        mouse_pos = pygame.mouse.get_pos()
        a=screen.blit(mouse, mouse_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shopb1.collidepoint(event.pos):
                    shop()
                elif gameb1.collidepoint(event.pos) and score0 >= 100:
                    score0 -= 100
                    play()
                elif screen.blit(coin, (80, 250)).collidepoint(event.pos):
                    score0 += multitap
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Функция для окна магазина
def shop():
    global bg, background, score0, lvlbg, skin, lvlskin, coin, x, y, costx, costy, score00, win,lvlbg1,background1,bg1,skin1,skins,widthskins1, widthskins2,lvlskin1
    while True:
        screen.fill((0, 128, 0))  # Заливка фона магазина (например, черным цветом)

        backb = font1.render('BACK', True, 'White', 'Black')
        backb1 = backb.get_rect()
        backb1.center = (250, 750)

        upb = font2.render('UPGRADE HOME', True, 'White', 'Black')
        upb1 = upb.get_rect()
        upb1.center = (260, 50)

        costbg = font_bold.render(f'Cost {costx}', True, 'Black')
        costbg1 = costbg.get_rect()
        costbg1.center = (220, 250)

        upsb = font2.render('UPGRADE SKIN', True, 'White', 'Black')
        upsb1 = upsb.get_rect()
        upsb1.center = (240, 400)

        costskin = font_bold.render(f'Cost {costy}', True, 'Black')
        costskin1 = costskin.get_rect()
        costskin1.center = (230, 585)

        screen.blit(backb, backb1)
        b=screen.blit(upgradehome1, upb1)
        c=screen.blit(upgradeskin1, upsb1)
        screen.blit(costbg, costbg1)
        screen.blit(costskin, costskin1)
        screen.blit(goldcoin, (290,225))
        screen.blit(goldcoin, (290, 560))
        screen.blit(background1,(widthskins1,180))
        screen.blit(skins, (widthskins2, 550))

        mouse_pos = pygame.mouse.get_pos()
        a=screen.blit(mouse, mouse_pos)

        pygame.display.flip()
        if lvlbg == 10 and lvlskin == 7 and win == 1:
            print("You win")
            win = 0
            return
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backb1.collidepoint(event.pos):
                    return  # Возврат в главное меню
                if check_collision(a,b) and score00 >= costx:
                    lvlbg += x
                    bg = 'bg' + str(lvlbg) + '.png'
                    background = pygame.image.load(bg)
                    score00 -= costx
                    costx+=5
                    if lvlbg1<9:
                        lvlbg1+=1
                        bg1 = 'bg1' + str(lvlbg1) + '.png'
                        background1 = pygame.image.load(bg1)
                    if lvlbg == 10:
                        x = 0
                        costx = 0
                        widthskins1+=1000
                        # return
                if check_collision(a,c) and score00 >= costy:
                    lvlskin += y
                    skin = 'c' + str(lvlskin) + '.png'
                    coin = pygame.image.load(skin)
                    score00 -= costy
                    costy+=5
                    if lvlskin<7:
                        lvlskin1+=1
                        skin1 = 'c1' + str(lvlskin1) + '.png'
                        skins=pygame.image.load(skin1)
                    if lvlskin == 7:
                        y = 0
                        costy = 0
                        widthskins2+=1000
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Функция проверки столкновения
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


# Функция для окна игры
def play():
    global spikes, game, game1, goldcoin, score00, spiker1, spikel1
    width = 0
    height = 300
    size = 0
    gold_rect = goldcoin.get_rect(center=(random.randint(50, 450), random.randint(100, 500)))
    rightspike = 0
    spike_positions = [random.randint(100, 600) for _ in range(2)]
    spike_left_positions = [random.randint(100, 600) for _ in range(2)]
    delay_counter = 0
    clock = pygame.time.Clock()

    while True:
        clock.tick(10)  # Устанавливаем 30 FPS

        if width <= 0:
            speedw = 20
            size = 0
            gold_rect = goldcoin.get_rect(center=(random.randint(50, 450), random.randint(100, 500)))
            spike_positions = [random.randint(100, 600) for _ in range(2)]
        if width >= 400:
            speedw = -20
            size = 1
            gold_rect = goldcoin.get_rect(center=(random.randint(50, 450), random.randint(100, 500)))
            spike_left_positions = [random.randint(100, 600) for _ in range(2)]
            rightspike = 1
        width += speedw
        height += 30

        screen.fill((100, 200, 0))  # Заливка фона игры (например, зеленым цветом)
        screen.blit(spikes, (0, 745))  # Нижние шипы
        screen.blit(spikes1, (0, -30))  # Верхние шипы

        spikes_rect = spikes.get_rect(topleft=(0, 780))
        spikes1_rect = spikes1.get_rect(topleft=(0, 0))
        screen.blit(game1, (width, height))
        screen.blit(goldcoin, gold_rect)

        spike_rects = []
        for pos in spike_positions:
            spike_rect = spiker1.get_rect(topleft=(450, pos))
            spike_rects.append(spike_rect)
            screen.blit(spiker1, (410, pos))
        if rightspike == 1:
            for pos in spike_left_positions:
                spike_rect = spikel1.get_rect(topleft=(-30, pos))
                spike_rects.append(spike_rect)
                screen.blit(spikel1, (0, pos))

        scoreg = font.render(f'{score00}', True, 'Gold', None)
        scoreg1 = scoreg.get_rect()
        scoreg1.center = (250, 400)
        screen.blit(scoreg, scoreg1)

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse, mouse_pos)
        pygame.display.flip()

        if size == 0:
            game = 'g1.png'
            game1 = pygame.image.load(game)
        elif size == 1:
            game = 'g11.png'
            game1 = pygame.image.load(game)

        game_rect = game1.get_rect(topleft=(width, height))

        if check_collision(game_rect, gold_rect):
            score00 += 1
            gold_rect.center = (1000, 0)

        # Проверка столкновений
        if (check_collision(game_rect, spikes_rect) or
                check_collision(game_rect, spikes1_rect) or
                any(check_collision(game_rect, spike_rect) for spike_rect in spike_rects)):
            return

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return  # Возврат в главное меню
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    height -= 150
                    game = 'g2.png' if speedw == 20 else 'g21.png'
                    game1 = pygame.image.load(game)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if width <= 0 or width >= 400:
            delay_counter += 1
            if delay_counter >= 15:
                delay_counter = 0
                spike_positions = [random.randint(100, 600) for _ in range(2)]
                spike_left_positions = [random.randint(100, 600) for _ in range(2)]


# Запуск основного меню
main_menu()