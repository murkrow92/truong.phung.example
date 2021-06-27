from Bai_tap.Items.Items import Items


class Kiem_bf(Items):
    def __init__(self):
        super().__init__(name="KIEM BF")

    def add_item(self, champion):
        super().add_item(champion)
        print("DAMAGE CHAMPION AFTER ADD ITEM:", champion.attack_damage + 50)
        champion.attack_damage = champion.attack_damage + 50
