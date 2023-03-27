def playerInput() -> str:
    spell_choice: str = input("Which spell to cast? [fire/frost]").lower()
    valid_input: bool = False

    while not valid_input:
        if spell_choice == 'fire' or spell_choice == 'frost':
            valid_input = True
        else:
            print(f'Answer needs to be fire or frost, your answer was {spell_choice}')
            spell_choice = input("Which spell to cast? [fire/frost]").lower()

    return spell_choice