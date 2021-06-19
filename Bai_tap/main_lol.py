from Bai_tap.ChampionFactory import create_all_champions

champions = create_all_champions()

for champion in champions:
    print("CHAMPIONS CREATED:", champion)
    champion.print_champion()
