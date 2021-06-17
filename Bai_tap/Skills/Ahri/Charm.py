from Bai_tap.Skills.Skill import Skill


class Charm(Skill):

    def __init__(self):
        super().__init__(name="Charm")
    def activate(self, champion, opponent):
        super().activate(champion, opponent)


