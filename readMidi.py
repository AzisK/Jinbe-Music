from mido import MidiFile, MidiTrack, Message
import numpy as np

mid = MidiFile('1.mid')

notes = []

time = float(0)
prev = float(0)

for msg in mid:
    time += msg.time
    if not msg.type == 'MetaMessage':
        if msg.type == 'note_on':
            # Note in vector form to train on
            note = msg.bytes()
            # Only interested in the note and velocity
            # Note message is in the form of
            # [type, note, velocity]
            note = note[1:3]
            note.append(time-prev)
            prev = time
            notes.append(note)

song = MidiFile()
track = MidiTrack()
song.tracks.append(track)

for note in notes:
    # 1 4 7  M E A N S  N O T E_O N #
    note = np.insert(note, 0, 147)
    bytesOfInt = note.astype(int)
    print(note)
    msg = Message.from_bytes(bytesOfInt[0:3])
    # Rescale to midi delta ticks. Arbitrary value for now
    time = int(note[3]/0.001025)
    msg.time = time
    track.append(msg)

song.save("1X.mid")
