class Player:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        print(f"{self.name} атакует {target.name} на {self.attack_power} HP!")
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} теперь имеет {target.hp} HP.\n")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} лечится на {amount} HP!")
        print(f"{self.name} теперь имеет {self.hp} HP.\n")


# создаём игроков
player1 = Player("Poppy", 100, 15)

player2 = Player("Omen", 80, 10)

# боевой цикл
while player1.hp > 0 and player2.hp > 0:
    player1.attack(player2)
    if player2.hp <= 0:
        print(f"{player2.name} побеждён! {player1.name} выигрывает!")
        break
    player2.heal(15)
    player1.heal(1)
    player2.attack(player1)
    if player1.hp <= 0:
        print(f"{player1.name} побеждён! {player2.name} выигрывает!")
        break
# ===============================================================================
# бой со случайним выбором!!!!!!!!!
# ===============================================================================

import random

class Player:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} атакует {target.name} на {self.attack_power} HP!")
        print(f"{target.name} теперь имеет {target.hp} HP.\n")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} лечится на {amount} HP!")
        print(f"{self.name} теперь имеет {self.hp} HP.\n")


# создаём игроков
player1 = Player("Poppy", 100, 15)
player2 = Player("Omen", 80, 10)

# боевой цикл с случайными действиями
while player1.hp > 0 and player2.hp > 0:
    # Ход player1
    if random.choice(["attack", "heal"]) == "attack":
        player1.attack(player2)
    else:
        heal_amount = random.randint(5, 15)
        player1.heal(heal_amount)
    
    if player2.hp <= 0:
        print(f"{player2.name} побеждён! {player1.name} выигрывает!")
        break

    # Ход player2
    if random.choice(["attack", "heal"]) == "attack":
        player2.attack(player1)
    else:
        heal_amount = random.randint(5, 15)
        player2.heal(heal_amount)

    if player1.hp <= 0:
        print(f"{player1.name} побеждён! {player2.name} выигрывает!")
        break
