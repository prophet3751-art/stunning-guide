import time
import random
class Wizard:
    def __init__(self, name, hp, mana, spell_power):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.spell_power = spell_power
# ====================================================================
    def heal(self, amount):
        self.hp += amount
        self.hp = min(100, self.hp)
        print(f"{self.name} Лечится на {amount} HP")
        print(f"{self.name} теперь имеет {self.hp} HP")
        print("=" * 30)
# ====================================================================
    def regenerate_mana(self, amount):
        self.mana += amount
        self.mana = min(50, self.mana)
        print(f"{self.name} востоналивает ману на {amount} Mana!")
        print(f"{self.name} имеет {self.mana} Mana!")
        print("=" * 30)
# ====================================================================
    def cast_spell(self, target):
        if self.mana >= 5:
            damage = random.randint(max(1, self.spell_power - 2), self.spell_power + 2)
            target.hp -= damage
            target.hp = max(0, target.hp)
            self.mana -= 5
            self.mana = max(0, self.mana)
            print(f"{self.name} кастует заклинание 'Avada_Kedvra!' на {target.name} на {damage}")
            print(f"HP {target.name} = {target.hp}, {self.name} Mana = {self.mana}")
            print("=" * 30)
        else:
            print(f"{self.name} не хватает маны!")
            print("=" * 30)
# ====================================================================
Witcher1 = Wizard("Гендольф", 100, 20, 10)
witcher2 = Wizard("Поттер", 100, 1, 7)
# ====================================================================

while Witcher1.hp > 0 and witcher2.hp > 0:
# First witcher actions!
    action1 = random.choice(["heal", "regenerate_mana", "cast_spell"])
    if action1 == "cast_spell":
        Witcher1.cast_spell(witcher2)
    elif action1 == "regenerate_mana":
        mana_amount = random.randint(5, 10)
        Witcher1.regenerate_mana(mana_amount)
    else:
        heal_amount = random.randint(5, 8)
        Witcher1.heal(heal_amount)

    if witcher2.hp <= 0:
        print(f"{witcher2.name} проиграл!, {Witcher1.name} победил!")
        break
    time.sleep(1)
# Second witcher actions!
    action2 = random.choice(["cast_spell", "heal", "regenerate_mana"])
    if action2 == "cast_spell":
        witcher2.cast_spell(Witcher1)
    elif action2 == "regenerate_mana":
        mana_amount = random.randint(5, 10)
        witcher2.regenerate_mana(mana_amount)
    else:
        heal_amount = random.randint(5, 8)
        witcher2.heal(heal_amount)
    if Witcher1.hp <= 0:
        print(f"{Witcher1.name} проиграл!, {witcher2.name} победил!")
        break