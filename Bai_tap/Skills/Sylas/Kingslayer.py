from Bai_tap.Skills.Skill import Skill


class Kingslayer(Skill):
    def __init__(self):
        super().__init__(name="Kingslayer")

    def activate(self, champion, opponent):
        super().activate(champion, opponent)
        magic_damage_deal = opponent.calculate_magic_damage(champion) + 100
        champion.recover(120)
        print("%s AFTER SKILL_W %s" %(champion.name , opponent.name))
        opponent.calculate_hp_after_taken_damage(champion, is_physical_damage=False,
                                                 is_magic_damage=magic_damage_deal,
                                                 is_true_damage=True)
