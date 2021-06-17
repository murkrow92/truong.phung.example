from Bai_tap.Skills.Skill import Skill
from threading import Timer


class Charm(Skill):

    def __init__(self):
        super().__init__(name="Charm")

    def activate(self, champion, opponent):
        super().activate(champion, opponent)
        opponent.set_disabled(True)

        def set_enabled():
            print("CHAMPION ENABLED")
            opponent.set_disabled(False)

        t = Timer(1, set_enabled)
        t.start()
