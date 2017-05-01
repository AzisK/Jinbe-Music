from mido import MidiFile, MidiTrack, Message
import numpy as np

import random as r

notes = []
x = []
y = []
z = []

for i in range(100):
    x = r.randint(40, 80)
    y = r.randint(50, 70)
    z = 0.5 + r.random()*2

    notes.append([x] + [y] + [z])
    print(notes)

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

for note in notes:
    # 1 4 7  M E A N S  N O T E_O N #
    note = np.insert(note, 0, 147)
    bytesOfInt = note.astype(int)
    print(note)
    msg = Message.from_bytes(bytesOfInt[0:3])
    # Rescale to midi delta ticks. Arbitrary value for now
    time = int(note[3] / 0.001025)
    msg.time = time
    track.append(msg)

mid.save('rSong.mid')
