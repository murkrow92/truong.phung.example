from Bai_tap.Items.Item import Item


class Kiem_bf(Item):
    def __init__(self):
        super().__init__(name="KIEM BF")

    def add_item(self, champion):
        super().add_item(champion)
        print("DAMAGE CHAMPION AFTER ADD ITEM:", champion.attack_damage + 50)
        champion.attack_damage = champion.attack_damage + 50
