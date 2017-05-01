import mido
import random
from mido import Message, MidiFile, MidiTrack

notes = [64 - 12, 64 - 7, 64, 64 + 7, 64 + 12]

outfile = MidiFile()

track = MidiTrack()
outfile.tracks.append(track)

track.append(Message('program_change', program=12))

for i in range(10):
    note = random.choice(notes)
    track.append(Message('note_on', note=note, velocity=100, time=20))
    track.append(Message('note_off', note=note, velocity=100, time=64))
    track.append(Message('note_off', note=note, velocity=100, time=43))
    track.append(Message('note_off', note=note, velocity=100, time=78))
    track.append(Message('note_off', note=note, velocity=100, time=100))
    track.append(Message('note_off', note=note, velocity=100, time=50))

songName = 'newSong.mid'

outfile.save(songName)

## P L A Y  T H E  S O N G ##

port = mido.open_output()

for msg in MidiFile(songName).play():
    port.send(msg)
