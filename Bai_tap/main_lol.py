from threading import Timer

from Bai_tap.Champions.Ahri import Ahri
from Bai_tap.Champions.Annie import Annie
from Bai_tap.Champions.Sylas import Sylas

sylas = Sylas()
sylas.print_champion()
ahri = Ahri()
ahri.print_champion()

ahri.use_e(sylas)
sylas.use_q(ahri)


def use_q_again():
    sylas.use_q(ahri)


t = Timer(1.5, use_q_again)
t.start()
