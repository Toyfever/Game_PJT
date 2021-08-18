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
    suitReminder = f"Choose between {spacesuit.keys()}"
    question = ("Welcome aboard of Exebra Space Cruise Ship, you just woke up"
                "from cryo-stasis\n")
    print(question)

    
    while "spacesuit check loop":
        spacesuitPlayer = input(suitReminder)

        if spacesuitPlayer in spacesuit:
            print(f"Your armor value is now {spacesuit[spacesuitPlayer]}")
            break
        else:
            print(f"This spacesuit doesn't exist! {suitReminder}")

    print("time to choose your weapon")
    weaponReminder = f"Pick one of these: {weapon.keys()}"

    while "weapon check loop":
        weaponPlayer = input(weaponReminder)

        if weaponPlayer in weapon:
            if (weapon[weaponPlayer] >= 100):
                print(f"Big and deadly! Your attack value raised to {weapon[weaponPlayer]}")
                break
            elif (weapon[weaponPlayer] <= 40):
                print(f"Small but efficient! Your attack value raised to {weapon[weaponPlayer]}")
                break
            else:
                print(f"Your attack value raised to {weapon[weaponPlayer]}")
                break

        else:
            print(f"this weapon is not on the rack! choose between : {weapon.keys()}")

    print("It seems that you are ready to go!")

