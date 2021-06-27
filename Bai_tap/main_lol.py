from Bai_tap.ChampionFactory import create_all_champions

champions = create_all_champions()

for champion in champions:
    print("CHAMPIONS CREATED:", champion)
    # champion.print_champion()
sylas = champions[1]
ahri = champions[0]
sylas.print_champion()
sylas.add_items()

