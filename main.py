class Character:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.armor = 100

    def attack(self, target, amount):
        print(f"{self.name} attacked {target.name}")
        target.armor -= amount
        if target.armor - amount > 0:
            print(f'{target.name} blocked, remaining armor {target.armor}')
        else:
            target.health -= amount
            print(f"{target.name} no longer has armor and has taken {self.attack_power} damage, hp{target.health}")

    def heal(self, amount):
        if self.health + amount > 100:
            print("Cannot heal, will exceed max hp:")
        elif self.health >= 30:
            print("Cannot heal")
        elif self.health <= 29:
            self.health += amount
            print(f"Healed, current hp {self.health}")



class Warrior(Character):
    def inc_attack(self, target):
        damage = self.attack_power + 5
        print(f"{self.name} used skill, attack power increased to {damage}")
        print(f"Attacking {target.name}")
        target.health -= damage
        print(f"{target.name}, current health {target.health}")


class Mage(Character):
    def magic(self, target):
        m = self.attack_power + 20
        print(f"{self.name} used skill, abilities have gained {m} increase")
        print(f"Attacking {target.name}")
        target.health -= m
        print(f"{target.name}, current health {target.health}")


class Archer(Character):
    def arc(self, target):
        arch = self.attack_power + 10
        print(f"{self.name} used skill, abilities have gained {m} increase")
        print(f"Attacking {target.name}")
        target.health -= arch
        print(f"{target.name}, current health {target.health}")


warrior = Warrior("warrior", 95, 100)
mage = Mage("mage", 80, 100)
archer = Archer("archer", 90, 100)


warrior.attack(mage,100)
mage.heal(50)