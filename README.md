# Jinbe-Music
AI Music Composer

MISSION
Create an AI musical composer that everybody would love to listen to.

REQUIREMENTS
This is run on python2 as well as mido and python-rtmidi libraries https://mido.readthedocs.io/en/latest/.

TEMPORARY-VISION 
Looking forward to upgrading it to python3 as well as making it use some sort of machine learning 
algorithm to train.

SONGS OF THIS REPOSITORY

MIDI tracks 1.mid to 6.mid are of Spanish composer Albeniz take from the website 
http://www.piano-midi.de/albeniz.htm: España, Opus 165 (1890). The parts are called 
Prelude, Tango, Malaguena, Serenata, Capricho Catalan, Zortzico respectively.

Song 1X.mid is the same as 1.mid just except the meta message of midi files. It was read and 
rerendered by readMidi.py.

Song rSong.mid is a song created randomly by executing newRandomSongs.py. It generated notes 
with random pitches from 40 to 80 and random velocities(volumes) from 50 to 70 as well as random 
times from 0.5 to 2 seconds.

Song newMidi.py is a file that creates a new midi files by adding some notes

OTHER PYTHON FILES
PlayAMidiFile.mid is a python file that sends the song to the port and then the midi file is played without any other software. iterateOverMessages.py does pretty much the same.

checkTracks.py checks what tracks and messages are in the the midi files.


