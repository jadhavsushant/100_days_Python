
with open(file="input\\Name\\Invited_names.txt") as inv_names:
    names = inv_names.readlines()
    new_names = []
    for i in names:
        new_names.append(i.rstrip())


for name in range(len(new_names)):
    with open(file="input\\Letters\\Starting_letters.txt") as s_letter:
        letter = s_letter.read().replace("[name]", new_names[name])
        file_out = ".\\output\\ReadyToSend\\letter_for_%s.txt" % new_names[name]

        with open(file=file_out, mode="w") as file_out:
            file_out.write(letter)


