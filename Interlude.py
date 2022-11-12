import numpy as np
import matplotlib.pyplot as plt
from scamp import Session, wait
import random

session = Session()
piano = session.new_part("piano")
cello = session.new_part("cello")
pitch = 55

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

# Random Walk to Audio
# Random walk is a stochastic process well known and studied in statistics.
# The idea behind it is that a person can randomly choose to walk left or right.
# A radnom number is generated between [0,1] and a threshold is used to decide 
# whether the walk is to the right(+1) or left(-1). 
# Statistically, if the threshold is above 0.5, then the accumulated distance
# will strive towards infinity. And if it is below 0.5, to negative infinity.
# Two plots are plotted, to show how the accumalated distances changes for 
# different threshold values.
# Input: pitch (integer), iterations(integer), threshold(float)
# Output: Audio signal of the generated random walk, plot of each random instance
# and accumalated distance plot.
def random_walk_to_audio(pitch, iterations, threshold):
    random_walk = list()
    i = 0
    while i < iterations:
        rand = random.uniform(a=0.0, b=1.0)
        if (rand < threshold):
            new_note = -1
        else:
            new_note = 1
        cello.play_note(pitch, 0.5, 0.05)
        random_walk.append(new_note)
        pitch += new_note
        i += 1

    plt.subplot(1,2,1)
    plt.plot(random_walk)
    plt.subplot(1,2,2)
    plt.plot(np.cumsum(random_walk))
    plt.show()

    print(sum(random_walk))

text_to_audio("Hello World :)")
random_walk_to_audio(pitch, 100, 0.55)
random_walk_to_audio(pitch, 100, 0.45)

