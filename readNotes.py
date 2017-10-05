from mido import MidiFile, Message
import os
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='Azis', api_key='XPJoZ8jbZl5fjuk8DldL')

notes = [0 for i in range(128)]
noteReference = [0 for i in range(128)]

for i in range(len(notes)):
    noteReference[i] = i

def loadPieces(dirpath):

    pieces = {}

    for fname in os.listdir(dirpath):
        if fname[-4:] not in ('.mid','.MID'):
            continue

        name = fname[:-4]

        piece = os.path.join(dirpath, fname)

        pieces[name] = piece
        print "Loaded {}".format(name)

    return pieces

def readNotes(dirpath):
    for i in (loadPieces(dirpath).values()):
        mid = MidiFile(i)
        for msg in mid:
            if not msg.type == 'MetaMessage':
                if msg.type == 'note_on':
                    note = msg.bytes()
                    note = note[1]
                    notes[note] += 1

def drawGraph(dirpath, type, x ,y):
    if type == "bar":
        data = [go.Bar( x=x, y=y )]
    elif type == "line":
        data = [go.Scatter( x=x, y=y,
            mode = 'lines+markers')]

    layout = dict(title = dirpath + ' notes',
        xaxis = dict(title = 'Notes'),
        yaxis = dict(title = 'Times played')
        )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename=dirpath)

if __name__ == '__main__':
    dirpath = 'Tschai';
    readNotes(dirpath)
    noteRange = np.nonzero(notes)
    minNote = noteRange[0][0]
    maxNote = noteRange[0][-1]
    x=noteReference[minNote:maxNote]
    y=notes[minNote:maxNote]
    drawGraph(dirpath, 'bar', x ,y)
