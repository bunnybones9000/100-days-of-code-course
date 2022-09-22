
place_holder = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as Names:
    list_of_names = Names.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letters:
    letter = letters.read()
    for name in list_of_names:
        stripped = name.strip()
        new_letter = letter.replace(place_holder, stripped)
        with open(f"./Output/ReadyToSend/letter_to_{stripped}", mode="w") as let:
            let.write(f"{new_letter}")

