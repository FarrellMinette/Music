from scamp import Session, wait
from scamp_extensions.pitch import Scale
import math
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
scale(Scale.major(60), Scale.major(60))

# Harmonic minor scale starting on middle C
scale(Scale.harmonic_minor(60), Scale.harmonic_minor(60))

# Melodic minor scale starting on middle C
scale(Scale.melodic_minor(60), Scale.harmonic_minor(60))

for i in range(0,400):
    piano.play_note(10 * math.sin(session.beat()) + mc, 0.75, 0.05)
    piano.play_note(10 * math.sin(session.beat()) + mc + 10, 0.75, 0.05)
