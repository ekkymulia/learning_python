PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt') as names:
    new_names = names.readlines()

with open('Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read();

    for name in new_names:
        new_letter = letter.replace(PLACEHOLDER, name.strip())
        with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.txt', mode='w') as output:
            output.write(new_letter);

        with open(f'./Output/ReadyToSend/letter_for_{name.strip()}.txt', mode='r') as check_output:
            print(check_output.read())