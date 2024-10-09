from midiutil import MIDIFile

notes = [
    ('E4', 4),  # 'E' at octave 4, whole note
    ('C4', 4),  # 'C' at octave 4, whole note
    ('D4', 2),  # 'D' at octave 4, half note
    ('G3', 4),  # 'G' at octave 3, whole note
    ('F4', 4),  # 'F' at octave 4, whole note
    ('C4', 2),  # 'C' at octave 4, half note
    ('A3', 2),  # 'A' at octave 3, half note
    ('C4', 2),  # 'C' at octave 4, half note
    ('D4', 2),  # 'D' at octave 4, half note
    ('E4', 2),  # 'E' at octave 4, half note
    ('F4', 1),  # 'F' at octave 4, quarter note
    ('G4', 1),  # 'G' at octave 4, quarter note
    ('C4', 4)   # 'C' at octave 4, whole note
]

tempo = 60
track = 0
channel = 0
volume = 100
time = 0

midi = MIDIFile(1)
midi.addTempo(track, time, tempo)

note_dict = {
    'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65,
    'F#': 66, 'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71
}

def get_midi_pitch(note):
    note_name, octave = note[:-1], int(note[-1])
    return note_dict[note_name] + (octave - 4) * 12

for note, duration in notes:
    midi_pitch = get_midi_pitch(note)
    midi.addNote(track, channel, midi_pitch, time, duration, volume)
    time += duration

with open("out.mid", "wb") as output_file:
    midi.writeFile(output_file)
