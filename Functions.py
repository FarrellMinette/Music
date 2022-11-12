import numpy as np
from scamp import Session, wait
from scamp_extensions.pitch import Scale
import math
import matplotlib.pyplot as plt
mc = 60.0

session = Session()
piano = session.new_part("piano")

def scale(scale_up, scale_down):
    wait(1)
    for i in range(0,8):
        piano.play_note(scale_up[i], 0.75, 0.25)
    for i in range(6,-1, -1):
        piano.play_note(scale_down[i], 0.75, 0.25)   

# Major scale starting on middle C
# scale(Scale.major(60), Scale.major(60))

# Harmonic minor scale starting on middle C
# scale(Scale.harmonic_minor(60), Scale.harmonic_minor(60))

# Melodic minor scale starting on middle C
# scale(Scale.melodic_minor(60), Scale.harmonic_minor(60))

def sin_function():
    notes = 0.0
    i = 0

    while i < 100:
        true_c = math.sin(session.beat()) + mc/2
        true_g_2 = 5 * math.sin(session.beat()*2) + mc/2
        note = true_c + true_g_2

        piano.play_note(note, 0.75, 0.05)

sin_function()