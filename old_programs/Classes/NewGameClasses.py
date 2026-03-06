import random
import time
# ================== Родительский класс ==================
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


# ================== Наследники ==================
class Warrior(Player):
    def heal(self, amount):
        amount = amount // 3   # воин хилится хуже
        super().heal(amount)


class Wizard(Player):
    def heal(self, amount):
        amount = amount * 3    # маг хилится сильнее
        super().heal(amount)


class Rouge(Player):
    def attack(self, target):
        temp_power = self.attack_power * 2
        target.hp -= temp_power
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} атакует {target.name} на {temp_power} HP!")
        print(f"{target.name} теперь имеет {target.hp} HP.\n")

    def heal(self, amount):
        amount = amount // 2 
        super().heal(amount)
# ================== Создаём игроков ==================
warrior = Warrior("Воин", 120, 15)
wizard = Wizard("Маг", 80, 20)
rouge = Rouge("Rouge", 50, 15)

# ================== Боевой цикл ==================
while warrior.hp > 0 and wizard.hp > 0 and rouge.hp > 0:
    # Ход Воина
    if random.choice(["attack", "heal"]) == "attack":
        targets = random.choice([wizard, rouge])
        warrior.attack(targets)
    else:
        warrior.heal(random.randint(5, 15))

    if wizard.hp <=0 and rouge.hp <= 0:
        print(f"{wizard.name} и {rouge.name} пали! {warrior.name} победил!")
        break
    elif wizard.hp <= 0:
        print(f"{wizard.name} пал! {warrior.name} победил!")
        break
    elif rouge.hp <= 0:
        print(f"{rouge.name} пал! {warrior.name} победил!")
        break
    time.sleep(1)
    # Ход Мага
    if random.choice(["attack", "heal"]) == "attack":
        targets = random.choice([warrior, rouge])
        wizard.attack(targets)
    else:
        wizard.heal(random.randint(5, 15))

    if warrior.hp <=0 and rouge.hp <= 0:
        print(f"{warrior.name} и {rouge.name} пали! {wizard.name} победил!")
        break
    elif warrior.hp <= 0:
        print(f"{warrior.name} пал! {wizard.name} победил!")
        break
    elif rouge.hp <= 0:
        print(f"{rouge.name} пал! {wizard.name} победил!")
        break
    time.sleep(1)
    # ход Rouge:
    if random.choice(["attack", "heal"]) == "attack":
        targets = random.choice([warrior, wizard])
        rouge.attack(targets)
    else:
        rouge.heal(random.randint(5, 20))

    if wizard.hp <=0 and warrior.hp <= 0:
        print(f"{warrior.name} и {wizard.name} пали! {rouge.name} победил!")
        break
    elif warrior.hp <= 0:
        print(f"{warrior.name} пал! {rouge.name} победил!")
        break
    elif wizard.hp <= 0:
        print(f"{wizard.name} пал! {rouge.name} победил!")
        break
    time.sleep(1)