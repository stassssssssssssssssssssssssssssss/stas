import pygame
import sys
import random
from s import WIDTH, HEIGHT, WHITE, BUTTON_COLOR

# Инициализация Pygame
pygame.init()

# Создание окна
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камінь, Ножиці, Папір")

# Загрузка изображений
rock_img = pygame.image.load('images/rock.jpg')
scissors_img = pygame.image.load('images/scissors.jpg')
paper_img = pygame.image.load('images/paper.jpg')

# Опции для выбора
options = ['rock', 'scissors', 'paper']

# Функция выбора компьютера
def get_computer_choice():
    return random.choice(options)

# Определение победителя
def determine_winner(player, computer):
    if player == computer:
        return "Нічия"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "Ви виграли!"
    return "Комп'ютер виграв!"

# Основные переменные
player_choice = None
computer_choice = None
result = "Зробіть свій вибір!"  # Стартовое сообщение

# Основной цикл игры
while True:
    # Заливка экрана
    win.fill(WHITE)

    # Отображение изображений
    win.blit(rock_img, (50, 300))       # Координаты x=50, y=300
    win.blit(scissors_img, (225, 300)) # Координаты x=225, y=300
    win.blit(paper_img, (400, 300))    # Координаты x=400, y=300


    # Отображение текста результата
    font = pygame.font.SysFont('Arial', 30)
    label = font.render(f"Результат: {result}", True, (0, 0, 0))
    win.blit(label, (50, 100))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Проверка кликов на изображения
            if 50 <= mouse_x <= 150 and 300 <= mouse_y <= 400:
                player_choice = 'rock'
            elif 225 <= mouse_x <= 325 and 300 <= mouse_y <= 400:
                player_choice = 'scissors'
            elif 400 <= mouse_x <= 500 and 300 <= mouse_y <= 400:
                player_choice = 'paper'
            
            # Генерация выбора компьютера и определение результата
            if player_choice:
                computer_choice = get_computer_choice()
                result = f"Ви: {player_choice}, Комп'ютер: {computer_choice}. {determine_winner(player_choice, computer_choice)}"

    # Обновление экрана
    pygame.display.flip()
