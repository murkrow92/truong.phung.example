from Bai_tap.Champions.Champion import Champion
from Bai_tap.Items.Kiem_BF import Kiem_bf
from Bai_tap.Skills.Sylas.Abscond import Abscond
from Bai_tap.Skills.Sylas.Hijack import Hijack
from Bai_tap.Skills.Sylas.Kingslayer import Kingslayer
from Bai_tap.Skills.Sylas.ChaimLash import ChaimLash


class Sylas(Champion):
    def __init__(self):
        chain_lash = ChaimLash()
        king_slayer = Kingslayer()
        abscond = Abscond()
        hijack = Hijack()
        kiem_bf = Kiem_bf()
        super().__init__(name="Sylas", items= kiem_bf,
                         button_q=chain_lash,
                         button_w=king_slayer,
                         button_e=abscond,
                         button_r=hijack)
