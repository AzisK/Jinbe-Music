import mido
from mido import MidiFile

port = mido.open_output()

for msg in MidiFile('1.mid').play():
    port.send(msg)