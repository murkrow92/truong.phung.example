from Bai_tap.Champions.Champion import Champion
from Bai_tap.Items.Kiem_BF import Kiem_bf
from Bai_tap.Skills.Ahri.Charm import Charm
from Bai_tap.Skills.Ahri.FoxFire import FoxFire
from Bai_tap.Skills.Ahri.OrbOfDeception import OrbOfDeception
from Bai_tap.Skills.Ahri.SpritRush import SpiritRush


class Ahri(Champion):
    def __init__(self):
        orb_of_deception = OrbOfDeception()
        fox_fire = FoxFire()
        charm = Charm()
        spirit_rush = SpiritRush()
        kiem_bf = Kiem_bf()
        super().__init__(name="Ahri",items= kiem_bf,
                         button_q=orb_of_deception,
                         button_w=fox_fire,
                         button_e=charm,
                         button_r=spirit_rush)
