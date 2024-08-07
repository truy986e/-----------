import pygame
import sys

pygame.init()

# Загрузка изображений и настроек
bg = 'bg1.png'
skin = 'c1.png'
mouse_img = 'mouse.png'
background = pygame.image.load(bg)
coin = pygame.image.load(skin)
mouse = pygame.image.load(mouse_img)
font = pygame.font.SysFont('times', 50)
font1 = pygame.font.SysFont('times', 95)

# Основной экран
screen = pygame.display.set_mode((500, 800))
score0 = 0
multitap = 1


# Функция для отрисовки основного меню
def main_menu():
    global score0
    while True:
        screen.blit(background, (0, 0))

        # Отображение счета
        score = font.render(f'{score0}', True, 'White', None)
        score1 = score.get_rect()
        score1.center = (250, 50)
        screen.blit(score, score1)

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
    while True:
        screen.fill((0, 0, 0))  # Заливка фона магазина (например, черным цветом)

        backb = font1.render('BACK', True, 'White', 'Black')
        backb1 = backb.get_rect()
        backb1.center = (250, 750)

        screen.blit(backb, backb1)

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse, mouse_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backb1.collidepoint(event.pos):
                    return  # Возврат в главное меню
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# Функция для окна игры
def play():
    while True:
        screen.fill((0, 128, 0))  # Заливка фона игры (например, зеленым цветом)

        backb = font1.render('BACK', True, 'White', 'Black')
        backb1 = backb.get_rect()
        backb1.center = (250, 750)

        screen.blit(backb, backb1)

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse, mouse_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backb1.collidepoint(event.pos):
                    return  # Возврат в главное меню
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# Запуск основного меню
main_menu()
