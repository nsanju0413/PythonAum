player_stats = {
    "Elizabeth": {"Wins": 41, "Losses": 3, "Ties": 22},
    "Joel": {"Wins": 32, "Losses": 14, "Ties": 17},
    "Mike": {"Wins": 8, "Losses": 19, "Ties": 11}
}

print("Welcome to the Game Stats program!")
print("Available players:", ", ".join(player_stats.keys()))

while True:
    player_name = input("Enter a player name: ").title()
    if player_name in player_stats:
        print(f"\n{player_name}'s Stats:")
        for stat, value in player_stats[player_name].items():
            print(f"{stat}: {value}")
    else:
        print(f"There is no player named {player_name}.")

    choice = input("Continue? (y/n): ").lower()
    if choice != "y":
        break

print("\nBye!")
