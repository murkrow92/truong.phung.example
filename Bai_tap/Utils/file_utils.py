import json
import os


# dirname = os.path.dirname(__file__)
# filename_sylas = os.path.join(dirname, "..\Game_Data\sylas.json")

def read(filename):
    file = open(filename)
    read_file = file.read()
    champion = json.loads(read_file)
    return champion


class Champion():
    def __init__(self, name, hp, attack_damage, ability_power, armor):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage
        self.ability_power = ability_power
        self.armor = armor

    def print_champion(self):
        print("Name:", self.name)
        print("Hp:", self.hp)
        print("Attack Damage:", self.attack_damage)
        print("Ability Power:", self.ability_power)
        print("Armor:", self.armor)


class Sylas(Champion):
    def __init__(self):
        super().__init__(name=champion_sylas['name'], hp=champion_sylas['hp'],
                         attack_damage=champion_sylas['attack_damage'],
                         ability_power=champion_sylas['ability_power'],
                         armor=champion_sylas['armor'])


class Ahri(Champion):
    def __init__(self):
        super().__init__(name=champion_ahri['name'], hp=champion_ahri['hp'],
                         attack_damage=champion_ahri['attack_damage'],
                         ability_power=champion_ahri['ability_power'],
                         armor=champion_ahri['armor'])


champion_sylas = read("..\Game_Data\sylas.json")
champion_ahri = read("..\Game_Data\\ahri.json")

sylas = Sylas()
sylas.print_champion()

ahri = Ahri()
ahri.print_champion()
