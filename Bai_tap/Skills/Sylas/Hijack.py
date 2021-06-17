from Bai_tap.Skills.Skill import Skill


class Hijack(Skill):

    def __init__(self):
        super().__init__(name="Hijack")

    def activate(self, champion, opponent):
        super().activate(champion, opponent)
        champion.button_r = opponent.button_r
        print("Champion Rob Skill_R of Opponent")
        champion.use_r(opponent)
