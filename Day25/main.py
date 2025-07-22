#f = open("./Templates/LetterFormat/Invitation.txt","r")
PLACE_HOLDER = "[name]"



with open("./Templates/LetterFormat/Invitation.txt",mode="r") as invitation:
    invite = invitation.read()

with open("./Templates/InivitedList/names.txt",mode="r") as invitelist:
    names = invitelist.readlines()


    for name in names:
        name = name.strip()
        new_letter = invite.replace(PLACE_HOLDER,name)
        with open(f"./Output/ReadytoSend/{name}.txt", mode="w" ) as completed_letter:
            completed_letter.write(new_letter)