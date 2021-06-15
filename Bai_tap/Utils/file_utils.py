import json
import os


def read():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "..\Game_Data\sylas.json")
    file = open(filename)
    read_file = file.read()
    champion = json.loads(read_file)
    return champion


champiton = read()


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
        super().__init__(name=champiton['name'], hp=champiton['hp'],
                         attack_damage=champiton['attack_damage'],
                         ability_power=champiton['ability_power'],
                         armor=champiton['armor'])


sylas = Sylas()
sylas.print_champion()
