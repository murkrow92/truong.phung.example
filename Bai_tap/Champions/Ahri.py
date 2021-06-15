from Bai_tap.Champions.Champion import Champion
from Bai_tap.Skills.Ahri.Charm import Charm
from Bai_tap.Skills.Ahri.FoxFire import FoxFire
from Bai_tap.Skills.Ahri.OrbOfDeception import OrbOfDeception
from Bai_tap.Skills.Ahri.SpritRush import SpiritRush
from Bai_tap.Utils.file_utils import read

ahri = read("ahri")


class Ahri(Champion):
    def __init__(self):
        orb_of_deception = OrbOfDeception()
        fox_fire = FoxFire()
        charm = Charm()
        spirit_rush = SpiritRush()

        super().__init__(name="Ahri",hp= ahri["hp"],
                         attack_damage=ahri["attack_damage"],
                         ability_power=ahri["ability_power"],
                         armor=ahri["armor"],
                         magic_armor=ahri["magic_armor"],
                         speed=ahri["speed"],
                         true_damage=ahri["true_damage"],
                         max_hp=ahri["max_hp"],
                         button_q=orb_of_deception,
                         button_w=fox_fire,
                         button_e=charm,
                         button_r=spirit_rush)
