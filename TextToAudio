from scamp import Session, wait

session = Session()
piano = session.new_part("piano")

# Text to audio
# Idea is to translate worlds into sounds. 
# Each character's ASCII representation is used to encode the characters as pitches.
# Input: String
# Output: audio representation of the String
def text_to_audio(text):
    for char in text:
        if char == " ":
            wait(0.5)
        elif char.isalnum():
            piano.play_note(ord(char)-20, 0.5, 0.25)
        else:   
            wait(0.5)
            piano.play_note(ord(char), 0.5, 0.25)

text_to_audio("Hello World :)")