player_stats = {
    "Elisabeth": {"Wins": 41, "Losses": 3, "Ties": 22},
    "Joel": {"Wins": 32, "Losses": 14, "Ties": 17},
    "Mike": {"Wins": 8, "Losses": 19, "Ties": 11}
}

print("Game Stats program\n")
print("ALL PLAYERS:")
for player_name in player_stats.keys():
    print(player_name)

while True:
    player_name = input("\nEnter a player name: ").title()
    if player_name in player_stats:
        for stat, value in player_stats[player_name].items():
            print(f"{stat:}{ value: >10}")
    else:
        print(f"There is no player named {player_name}.")

    choice = input("\nContinue? (y/n): ").lower()
    if choice != "y":
        break



print("\nBye!")
