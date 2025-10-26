import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Demo")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (0, 200, 0)
YELLOW = (255, 215, 0)
GRAY = (200, 200, 200)

font = pygame.font.SysFont("arial", 24)

# Класс персонажа
class Character:
    def __init__(self, name, hp, attack_power, x, y, color):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.x = x
        self.y = y
        self.color = color
        self.width = 50
        self.height = 50

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        # HP-полоска
        ratio = self.hp / self.max_hp
        pygame.draw.rect(win, RED, (self.x, self.y - 15, self.width, 10))
        pygame.draw.rect(win, GREEN, (self.x, self.y - 15, int(self.width * ratio), 10))
        # Имя и HP
        hp_text = font.render(f"{self.name}: {self.hp}/{self.max_hp}", True, BLACK)
        win.blit(hp_text, (self.x - 20, self.y - 40))

    def attack(self, target):
        dmg = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.hp -= dmg
        if target.hp < 0:
            target.hp = 0
        return f"{self.name} attacks {target.name} for {dmg} HP!"

    def heal(self):
        heal_amount = random.randint(10, 15)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        return f"{self.name} heals for {heal_amount} HP!"

# Игрок и враг
player = Character("Hero", 100, 20, 150, 200, GREEN)
enemy = Character("Orc", 100, 15, 400, 200, RED)

# Лог действий
log = []

# Кнопки
attack_button = pygame.Rect(50, 300, 100, 50)
heal_button = pygame.Rect(200, 300, 100, 50)

running = True
player_turn = True  # ход игрока

while running:
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            if attack_button.collidepoint(event.pos):
                log.append(player.attack(enemy))
                player_turn = False
            elif heal_button.collidepoint(event.pos):
                log.append(player.heal())
                player_turn = False

    # Враг атакует автоматически, если ход не игрока
    if not player_turn and enemy.hp > 0 and player.hp > 0:
        pygame.time.delay(500)  # пауза перед атакой врага
        log.append(enemy.attack(player))
        player_turn = True

    # Рисуем персонажей
    player.draw()
    enemy.draw()

    # Рисуем кнопки
    pygame.draw.rect(win, GRAY, attack_button)
    pygame.draw.rect(win, GRAY, heal_button)
    win.blit(font.render("Attack", True, BLACK), (attack_button.x + 10, attack_button.y + 10))
    win.blit(font.render("Heal", True, BLACK), (heal_button.x + 10, heal_button.y + 10))

    # Рисуем лог
    y_offset = 20
    for line in log[-6:]:
        win.blit(font.render(line, True, BLACK), (50, y_offset))
        y_offset += 20

    # Проверка конца боя
    if player.hp <= 0:
        win.blit(font.render("💀 Enemy Wins!", True, YELLOW), (WIDTH//2 - 80, HEIGHT//2))
    elif enemy.hp <= 0:
        win.blit(font.render("🏆 Hero Wins!", True, YELLOW), (WIDTH//2 - 80, HEIGHT//2))

    pygame.display.update()
    pygame.time.Clock().tick(60)
