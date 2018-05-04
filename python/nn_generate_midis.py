from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq


def note_above(note, interval):
    """
    note: str, interval: int -> str

    Returns the note the specified number of semitones above the given
    note. If interval is positive, the returned note is higher than the given
    note.
    """
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_index = notes.index(note[:-1])
    new_note = notes[(note_index + interval) % 12]
    new_octave = int(note[-1]) + (note_index + interval)//12
    return(new_note + str(new_octave))


def note_to_int(note_str):
    """
    note_str: str -> int

    Returns the integer value of a note.
    """
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return(notes.index(note_str[:-1]))


def int_to_note(index):
    """
    index: int -> str

    Returns the note string at index.
    """
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return(notes[index])


filepath = "chord_midis/"

# major root
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 3) and (octave == 8):  # end on D8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                    note2_str = note_above(int_to_note(note) + str(octave), 4)
                    note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                    note3_str = note_above(int_to_note(note) + str(octave), 7)
                    note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                    midi = Midi(number_tracks=3, tempo=60, instrument=0)

                    midi.seq_notes(note1, track=0)
                    midi.seq_notes(note2, track=1)
                    midi.seq_notes(note3, track=2)

                    midi.write(filepath + "major_root/" + int_to_note(note).lower() + "_major_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + ".mid")

    if done == 1:
        break


# major first inversion
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 2) and (octave == 8):  # end on C#8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                    note2_str = note_above(int_to_note(note) + str(octave), 3)
                    note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                    note3_str = note_above(int_to_note(note) + str(octave), 8)
                    note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                    midi = Midi(number_tracks=3, tempo=60, instrument=0)

                    midi.seq_notes(note1, track=0)
                    midi.seq_notes(note2, track=1)
                    midi.seq_notes(note3, track=2)

                    midi.write(filepath + "major_first_inversion/" + note3_str[:-1].lower() + "_major_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + ".mid")

    if done == 1:
        break


# major second inversion
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 1) and (octave == 8):  # end on C8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                    note2_str = note_above(int_to_note(note) + str(octave), 5)
                    note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                    note3_str = note_above(int_to_note(note) + str(octave), 9)
                    note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                    midi = Midi(number_tracks=3, tempo=60, instrument=0)

                    midi.seq_notes(note1, track=0)
                    midi.seq_notes(note2, track=1)
                    midi.seq_notes(note3, track=2)

                    midi.write(filepath + "major_second_inversion/" + note2_str[:-1].lower() + "_major_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + ".mid")

    if done == 1:
        break


# minor root
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 3) and (octave == 8):  # end on D8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                    note2_str = note_above(int_to_note(note) + str(octave), 3)
                    note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                    note3_str = note_above(int_to_note(note) + str(octave), 7)
                    note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                    midi = Midi(number_tracks=3, tempo=60, instrument=0)

                    midi.seq_notes(note1, track=0)
                    midi.seq_notes(note2, track=1)
                    midi.seq_notes(note3, track=2)

                    midi.write(filepath + "minor_root/" + int_to_note(note).lower() + "_minor_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + ".mid")

    if done == 1:
        break


# minor first inversion
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 1) and (octave == 8):  # end on C8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                    note2_str = note_above(int_to_note(note) + str(octave), 4)
                    note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                    note3_str = note_above(int_to_note(note) + str(octave), 9)
                    note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                    midi = Midi(number_tracks=3, tempo=60, instrument=0)

                    midi.seq_notes(note1, track=0)
                    midi.seq_notes(note2, track=1)
                    midi.seq_notes(note3, track=2)

                    midi.write(filepath + "minor_first_inversion/" + note3_str[:-1].lower() + "_minor_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + ".mid")

    if done == 1:
        break


# minor second inversion
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 2) and (octave == 8):  # end on C#8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                    note2_str = note_above(int_to_note(note) + str(octave), 5)
                    note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                    note3_str = note_above(int_to_note(note) + str(octave), 8)
                    note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                    midi = Midi(number_tracks=3, tempo=60, instrument=0)

                    midi.seq_notes(note1, track=0)
                    midi.seq_notes(note2, track=1)
                    midi.seq_notes(note3, track=2)

                    midi.write(filepath + "minor_second_inversion/" + note2_str[:-1].lower() + "_minor_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + ".mid")

    if done == 1:
        break


# dominant seventh root
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 0) and (octave == 8):  # end on B7
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    for volume_note4 in [80, 100, 120]:
                        note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                        note2_str = note_above(int_to_note(note) + str(octave), 4)
                        note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                        note3_str = note_above(int_to_note(note) + str(octave), 7)
                        note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                        note4_str = note_above(int_to_note(note) + str(octave), 10)
                        note4 = NoteSeq([Note(value=note_to_int(note4_str), octave=int(note4_str[-1]), dur=1/16, volume=volume_note4)])

                        midi = Midi(number_tracks=4, tempo=60, instrument=0)

                        midi.seq_notes(note1, track=0)
                        midi.seq_notes(note2, track=1)
                        midi.seq_notes(note3, track=2)
                        midi.seq_notes(note4, track=2)

                        midi.write(filepath + "dominant_seventh_root/" + int_to_note(note).lower() + "_dominant_seventh_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + str(volume_note4) + ".mid")

    if done == 1:
        break


# dominant seventh first inversion
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 2) and (octave == 8):  # end on C#8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    for volume_note4 in [80, 100, 120]:
                        note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                        note2_str = note_above(int_to_note(note) + str(octave), 3)
                        note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                        note3_str = note_above(int_to_note(note) + str(octave), 6)
                        note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                        note4_str = note_above(int_to_note(note) + str(octave), 8)
                        note4 = NoteSeq([Note(value=note_to_int(note4_str), octave=int(note4_str[-1]), dur=1/16, volume=volume_note4)])

                        midi = Midi(number_tracks=4, tempo=60, instrument=0)

                        midi.seq_notes(note1, track=0)
                        midi.seq_notes(note2, track=1)
                        midi.seq_notes(note3, track=2)
                        midi.seq_notes(note4, track=2)

                        midi.write(filepath + "dominant_seventh_first_inversion/" + note4_str[:-1].lower() + "_dominant_seventh_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + str(volume_note4) + ".mid")

    if done == 1:
        break


# dominant seventh second inversion
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 1) and (octave == 8):  # end on C8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    for volume_note4 in [80, 100, 120]:
                        note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                        note2_str = note_above(int_to_note(note) + str(octave), 3)
                        note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                        note3_str = note_above(int_to_note(note) + str(octave), 5)
                        note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                        note4_str = note_above(int_to_note(note) + str(octave), 9)
                        note4 = NoteSeq([Note(value=note_to_int(note4_str), octave=int(note4_str[-1]), dur=1/16, volume=volume_note4)])

                        midi = Midi(number_tracks=4, tempo=60, instrument=0)

                        midi.seq_notes(note1, track=0)
                        midi.seq_notes(note2, track=1)
                        midi.seq_notes(note3, track=2)
                        midi.seq_notes(note4, track=2)

                        midi.write(filepath + "dominant_seventh_second_inversion/" + note3_str[:-1].lower() + "_dominant_seventh_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + str(volume_note4) + ".mid")

    if done == 1:
        break


# dominant seventh third inversion
done = 0
for octave in range(2, 9):
    for note in range(12):
        if (note == 0) and (octave == 2):  # start on C#2
            continue
        if (note == 1) and (octave == 8):  # end on C8
            done = 1
            break

        for volume_note1 in [80, 100, 120]:
            for volume_note2 in [80, 100, 120]:
                for volume_note3 in [80, 100, 120]:
                    for volume_note4 in [80, 100, 120]:
                        note1 = NoteSeq([Note(value=note, octave=octave, dur=1/16, volume=volume_note1)])

                        note2_str = note_above(int_to_note(note) + str(octave), 2)
                        note2 = NoteSeq([Note(value=note_to_int(note2_str), octave=int(note2_str[-1]), dur=1/16, volume=volume_note2)])

                        note3_str = note_above(int_to_note(note) + str(octave), 6)
                        note3 = NoteSeq([Note(value=note_to_int(note3_str), octave=int(note3_str[-1]), dur=1/16, volume=volume_note3)])

                        note4_str = note_above(int_to_note(note) + str(octave), 9)
                        note4 = NoteSeq([Note(value=note_to_int(note4_str), octave=int(note4_str[-1]), dur=1/16, volume=volume_note4)])

                        midi = Midi(number_tracks=4, tempo=60, instrument=0)

                        midi.seq_notes(note1, track=0)
                        midi.seq_notes(note2, track=1)
                        midi.seq_notes(note3, track=2)
                        midi.seq_notes(note4, track=2)

                        midi.write(filepath + "dominant_seventh_third_inversion/" + note2_str[:-1].lower() + "_dominant_seventh_" + int_to_note(note).lower() + "_" + str(octave) + "_" + str(volume_note1) + str(volume_note2) + str(volume_note3) + str(volume_note4) + ".mid")

    if done == 1:
        break
