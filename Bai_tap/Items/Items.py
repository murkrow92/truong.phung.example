class Items:
    def __init__(self, name=""):
        self.name = name

    def add_item(self, champion):
        print("CHAMPION %s ADD ITEM %s" % (champion.name, self.name))
