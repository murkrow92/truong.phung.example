from Bai_tap.Champions.Champion import Champion
from Bai_tap.Skills.Sylas.Abscond import Abscond
from Bai_tap.Skills.Sylas.Hijack import Hijack
from Bai_tap.Skills.Sylas.Kingslayer import Kingslayer
from Bai_tap.Skills.Sylas.ChaimLash import ChaimLash
from Bai_tap.Utils.file_utils import read

sylas = read("sylas")

class Sylas(Champion):
    def __init__(self):
        chain_lash = ChaimLash()
        kingslayer = Kingslayer()
        abscond = Abscond()
        hijack = Hijack()
        super().__init__(name="Sylas", hp= sylas["hp"],
                         attack_damage=sylas["attack_damage"],
                         ability_power=sylas["ability_power"],
                         armor=sylas["armor"],
                         magic_armor=sylas["magic_armor"],
                         speed=sylas["speed"],
                         true_damage=sylas["true_damage"],
                         max_hp=sylas["max_hp"],
                         button_q=chain_lash,
                         button_w=kingslayer,
                         button_e=abscond,
                         button_r=hijack)
