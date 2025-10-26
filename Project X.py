import random
import tkinter as tk
from tkinter.messagebox import showinfo, askyesno

# Tkinter window
root = tk.Tk()
root.title("Battle Log")
root.configure(bg="floralwhite")

log = tk.Text(root, width=80, height=40)
log.configure(bg="lightyellow")
log.pack()

def write(text):
    log.insert(tk.END, text + "\n")
    log.see(tk.END)
    if int(log.index('end-1c').split('.')[0]) > 300:
        log.delete("1.0", "end")
# Hp Bar
hp_bars = {}
# Heroes Frame===============================
heroes_frame = tk.Frame(root)
heroes_frame.configure(background="floralwhite")
heroes_label = tk.Label(heroes_frame, text="Heroes HP:", foreground="green", font=("Arial", 12, "italic" , "bold"), background="floralwhite")
heroes_label.pack(fill=tk.X, anchor="center")
heroes_frame.pack(pady=10, fill=tk.X)


# Enemy frame===============================
enemies_frame = tk.Frame(root)
enemies_frame.configure(background="floralwhite")
enemies_label= tk.Label(enemies_frame, text="Enemies HP:", foreground="red", font=("Arial", 12, "italic" , "bold"), background="floralwhite")
enemies_label.pack(fill=tk.X, anchor="center")
enemies_frame.pack(pady=10, fill=tk.X)
# HP bars===========================================
def create_hp_bar(character, frame):
    bar_frame = tk.Frame(frame, background="floralwhite")
    bar_frame.columnconfigure(1, weight=1)
    bar_frame.pack(pady=2)

    label = tk.Label(bar_frame, text=f"{character.name} HP:", background="floralwhite", anchor="w", width=12)
    label.grid(row=0, column=0, padx=5)
    
    canvas = tk.Canvas(bar_frame, width=200, height=20, bg="gray")
    canvas.grid(row=0, column=1, padx=5, sticky="we")
    
    bar = canvas.create_rectangle(0, 0, 200, 20, fill="green")

    text = canvas.create_text(100, 10, text=f"{character.hp}HP", fill="#000000")

    hp_bars[character] = (canvas, bar, text)

def update_hp_bar(character):
    canvas, bar, text = hp_bars[character]
    canvas.delete(bar)
    
    ratio = max(0, character.hp / character.max_hp)
    bar_width = int(200 * ratio)

    if ratio > 0.5:
        color = "green"
    elif ratio > 0.2:
        color = "yellow"
    else:
        color = "red"

    new_bar = canvas.create_rectangle(0, 0, bar_width, 20, fill=color)

    canvas.itemconfig(text, text=f"{character.hp}/{character.max_hp}HP")
    canvas.tag_raise(text)

    hp_bars[character] = (canvas, new_bar, text)


        
# Шаг 1: Классы
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power

    def alive_targets_only(self, *targets):
        alive_targets = [e for e in targets if e.hp > 0]
        if alive_targets:
            return random.choice(alive_targets)
        return None
    
    def attack(self, target):
        if self.hp <= 0:
            return
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        write(f"{self.name} attacks {target.name} on {self.attack_power} HP.\n")
        update_hp_bar(target)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        write(f"{self.name} heals for {amount}HP!\n")
        update_hp_bar(self)
# ==================================_Подклассы_=================================================
class Rogue(Hero):
    def __init__(self, name):
        super().__init__(name, hp=80, attack_power=25)
        self.crit_chance = 0.3

    def attack(self, target):
        if self.hp <= 0:
            return
        miss_chance = 0.2
        if random.random() < miss_chance:
            write(f"{self.name} missed!\n")
            return
        
        damage = random.randint(max(1, self.attack_power - 5), self.attack_power + 5)
        if random.random() < self.crit_chance:
            damage *= 2
            write("Critical attack!\n")

        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        write(f"{self.name} attacks {target.name} for {damage} HP!\n")
        update_hp_bar(target)

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, hp=130, attack_power=10)

    def attack(self, target):
        if self.hp <= 0:
            return
        miss_chance = 0.4
        if random.random() < miss_chance:
            write(f"{self.name} missed!\n")
            return
        
        damage = random.randint(max(1, self.attack_power -2), self.attack_power + 2)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        write(f"{self.name} attacks {target.name} for {damage} HP!\n")
        update_hp_bar(target)
# ===================================_Клас противников_==============================================
class Enemy:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power

    def alive_targets_only(self, *targets):
        alive_targets = [e for e in targets if e.hp > 0]
        if alive_targets:
            return random.choice(alive_targets)
        return None

    def attack(self, target):
        if self.hp <= 0:
            return
        target.hp -= self.attack_power
        if target.hp <0:
            target.hp = 0
        write(f"{self.name} attacks {target.name} for {self.attack_power} HP!\n")
        update_hp_bar(target)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        write(f"{self.name} healing for {amount} HP!\n")
        update_hp_bar(self)
# =====================Подклассы противников===========================================
class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name, hp=120, attack_power=20)

    def attack(self, target):
        if self.hp <= 0:
            return
        miss_chance = 0.4
        if random.random() < miss_chance:
            write(f"{self.name} missed!\n")
            return
        damage = random.randint(max(1, self.attack_power -2), self.attack_power + 2)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        write(f"{self.name} attacks {target.name} for {damage} HP!\n")
        update_hp_bar(target)
        
class Necromant(Enemy):
    def __init__(self, name):
        super().__init__(name, hp= 300, attack_power= 25)

    def attack(self, target):
        if self.hp <= 0:
            return
        miss_chance = 0.4
        if random.random() < miss_chance:
            write(f"{self.name} missed!\n")
            return
        damage = random.randint(max(1, self.attack_power -2), self.attack_power + 2)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        write(f"{self.name} attacks {target.name} for {damage} HP!\n")
        update_hp_bar(target)

# ======================_Создаем персов_=========================================
hero = Hero("Wizard", 100, 20)
rogue = Rogue("Shadow")
warrior = Warrior("Konan")

enemy = Enemy("Goblin", 90, 18)
orc = Orc("Lukash")
necromant = Necromant("Udod")

create_hp_bar(hero, heroes_frame)
create_hp_bar(rogue, heroes_frame)
create_hp_bar(warrior, heroes_frame)

create_hp_bar(enemy, enemies_frame)
create_hp_bar(orc, enemies_frame)
create_hp_bar(necromant, enemies_frame)

# ==========================_Функция боя_==============================================
def reset_game():
    for character in [hero, rogue, warrior, enemy, orc, necromant]:
        character.hp = character.max_hp
        update_hp_bar(character)

    log.delete("1.0", tk.END)
    write("New battle begins!\n")

def ask_restart():
    again = askyesno(title="Game Over!", message="Play againe?")
    if again:
        reset_game()

def battle_round():
# ===============================Бой Hero==========================================================
    alive = hero.alive_targets_only(enemy, orc, necromant)

    action0 = random.choice(["attack", "heal"])

    if action0 == "attack":
        if alive is not None:
            hero.attack(alive)
        
    else:
        temp_heal = random.randint(10, 12)
        hero.heal(temp_heal)
        
# ==========================Бой Rogue=====================================================
    alive = rogue.alive_targets_only(enemy, orc, necromant)

    action1 = random.choice(["attack", "heal"])
    
    if action1 == "attack":
        if alive is not None:
            rogue.attack(alive)
        
    else:
        temp_heal = random.randint(15, 20)
        rogue.heal(temp_heal)
        
# =====================================Бой Warrior============================================================
    alive = warrior.alive_targets_only(enemy, orc, necromant)

    action2 = random.choice(["attack", "heal"])

    if action2 == "attack":
        if alive is not None:
            warrior.attack(alive)
        
    else:
        temp_heal = random.randint(3, 6)
        warrior.heal(temp_heal)
    
        
# ===========================Бой Orc===========================================
    alive = orc.alive_targets_only(hero, rogue, warrior)

    action3 = random.choice(["attack", "heal"])

    if action3 == "attack":
        if alive is not None:
            orc.attack(alive)
        
    else:
        temp_heal = random.randint(10, 20)
        orc.heal(temp_heal)

        

# ==========================================Бой Enemy===============================================================
    alive = enemy.alive_targets_only(hero, rogue, warrior)

    action4 = random.choice(["attack", "heal"])

    if action4 == "attack":
        if alive is not None:
            enemy.attack(alive)
        
    else:
        temp_heal = random.randint(4, 8)
        enemy.heal(temp_heal)
# ==========================Бой Necromant====================================================================================
    alive = necromant.alive_targets_only(hero, rogue, warrior)
    action5 = random.choice(["attack", "heal"])
    if action5 == "attack":
        if alive is not None:
            necromant.attack(alive)

    else:
        temp_heal = random.randint(5, 15)
        necromant.heal(temp_heal)
            

    heroes_alive = hero.hp > 0  or rogue.hp > 0 or warrior.hp > 0
    enemies_alive = enemy.hp > 0 or orc.hp > 0 or necromant.hp > 0

    if heroes_alive and enemies_alive:
        root.after(500, battle_round)
    else:
        if heroes_alive:
            write("🏆 Heroes won!")
        else:
            write("💀 Enemies won!")

        root.after(2000, lambda: ask_restart())

def click ():
    result = askyesno(title="Confirm the operation", message="Want to play?")

    if result:
        battle_round()
    else:
        showinfo("Result", "Operation canceled!\nMaybe later.")
       

# Кнопка боя======================================
btn = tk.Button(
    root,
    text="Start Action",
    font=("Arial", 15, "bold"), 
    background="#C0C0C0", 
    foreground="black", 
    command=click, 
    cursor="hand2",
    activebackground="#000000",
    activeforeground="#FFFAFA",
    relief="flat",
    bd=5
    )
btn.pack(anchor="center", fill= tk.Y)
btn.bind("<Return>", lambda event : click())
btn.focus_set()

root.mainloop()   