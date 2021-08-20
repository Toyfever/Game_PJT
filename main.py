from lab import getlist

player_settings = {
    "HP": 100, "armor": 0, "attack": 0
}

spacesuit = {
    "suit a": 40,
    "suit b": 80,
    "suit c": 120
}

weapon = {
    "Classic Laser Blaster": 60,
    "Destroyer of worlds": 150,
    "the Cricket": 35
}


def main():
    """Game main frame."""
    suit_reminder = f"Choose between : {getlist(spacesuit)}\n"
    question = ("Welcome aboard of Exebra Space Cruise Ship, you just woke up"
                " from cryo-stasis \n")
    print(question)

    while "spacesuit check loop":
        spacesuit_player = input(suit_reminder)

        if spacesuit_player in spacesuit:
            print(f"Your armor value is now {spacesuit[spacesuit_player]}")
            break
        else:
            print(f"{spacesuit_player} spacesuit does not exist!")

    print("time to choose your weapon")
    weapon_reminder = f"Pick one of these: {getlist(weapon)}\n"

    while "weapon check loop":
        weapon_player = input(weapon_reminder)

        if weapon_player in weapon:
            if weapon[weapon_player] >= 100:
                print(f"Big and deadly! Your attack value raised to {weapon[weapon_player]}")
                break
            elif weapon[weapon_player] <= 40:

                print(f"Small but efficient! Your attack value raised to {weapon[weapon_player]}")
                break
            else:
                print(f"Your attack value raised to {weapon[weapon_player]}")
                break

        else:
            print(f"{weapon_player} is not on the rack! choose between")

    print("It seems that you are ready to go!")
