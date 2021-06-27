from Bai_tap.Champions.Ahri import Ahri
from Bai_tap.Champions.Sylas import Sylas
from Bai_tap.Utils.file_utils import read_all_champion_config

selector = {
    "Ahri": Ahri,
    "Sylas": Sylas
}


def create_all_champions():
    champions_data_from_file = read_all_champion_config()
    print("DATA FROM FILE:", champions_data_from_file)
    print(champions_data_from_file)
    champions = []
    for champion_config in champions_data_from_file:
        print("CHAMPION CONFIG:", champion_config)
        print("NAME:", champion_config['name'])
        new_champion = selector[champion_config['name']]() if champion_config['name'] in selector else Sylas()
        # new_champion.print_champion()
        champions.append(new_champion)
    return champions
