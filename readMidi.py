from mido import MidiFile, MidiTrack, Message
import numpy as np

mid = MidiFile('1.mid')  # a Mozart piece

notes = []

time = float(0)
prev = float(0)

for msg in mid:
    time += msg.time
    if not msg.type == 'MetaMessage':
        if msg.type == 'note_on':
            # note in vector form to train on
            note = msg.bytes()
            # only interested in the note and velocity. note message is in the form of [type, note, velocity]
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
    time = int(note[3] / 0.001025)  # to rescale to midi's delta ticks. arbitrary value for now.
    msg.time = time
    track.append(msg)

# t = []

# for note in notes:
#     note[0] = (note[0]-24)/88
#     note[1] = note[1]/127
#     t.append(note[2])
#
# max_t = max(t)
#
# for note in notes:
# 	note[2] = note[2]/max_t

print(notes)
print(len(notes))

song.save('1X.mid')