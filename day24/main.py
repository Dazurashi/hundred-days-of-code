'''
This program will read names from name.txt file.
Then it replaces placeholder in invitation_letter.txt
and generates unique invitation for that person which 
is stored in ready_to_send folder
'''

import os

name_file = "input/names/names.txt"
letter_file = "input/letters/invitation_letter.txt"
ready_to_send_folder = "output/ready_to_send"

def make_invitation(names_file, letter_file):
    with open (names_file, 'r') as names:
        name_list = names.read().splitlines()
        print(name_list)

    with open (letter_file, 'r') as invitation:
        template = invitation.read()
        print(template)

    for name in name_list:
        unique_invitation = template.replace('[name]', name)
        file_path = os.path.join(ready_to_send_folder, f"invitation_{name}.txt")
        with open(file_path, 'w') as new_invitation:
            new_invitation.write(unique_invitation)


make_invitation(name_file, letter_file)