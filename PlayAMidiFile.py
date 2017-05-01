import mido

port = mido.open_output()

mid = mido.MidiFile('1.mid')
for msg in mid.play():
    port.send(msg)