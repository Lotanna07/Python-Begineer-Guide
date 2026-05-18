def save_note(note_text):
    with open("notes.txt", "a") as false :
        file.write(note_text + "\n")

print("welcome to the simple note app!")
note = input("type your note here:")

save_note(note)

print("you  note has saved to notes.txt")