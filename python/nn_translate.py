"""
Provides functions and constants for translating strings representing notes
and chord types to integers, and vice versa.
"""

NUM_CHORD_TYPES = 3
notes = ["C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
chord_types = ["", "m", "7", "maj7", "min7", "mm7", "aug", "dim", "dim7", "dimm7"]

def note_to_index(note):
    """
    Returns index of note in global list variable notes
    """
    return(notes.index(note))

def type_to_index(chord_type):
    """
    Returns index of chord_type in global list variable chord_types
    """
    return(chord_types.index(chord_type))

def index_to_note(index):
    """
    Returns note at index in global list variable notes
    """
    return(notes[index])

def index_to_type(index):
    """
    Returns chord_type at index in global list variable chord_types
    """
    return(chord_types[index])

def possible_chord_roots(chord_type, root_note):
    """
    Returns a list of all possible chord roots of a chord with type chord_type
    and root (bottom) note root_note, represented as indices in global list
    variables notes and chord_types
    """
    chord_roots = [root_note]
    if chord_type == 0:  # major chord
        chord_roots.extend([(root_note + 4) % 12, (root_note + 7) % 12])  # root position
        chord_roots.extend([(root_note + 3) % 12, (root_note + 8) % 12])  # first inversion
        chord_roots.extend([(root_note + 5) % 12, (root_note + 9) % 12])  # second inversion
        return(chord_roots)
    if chord_type == 1:  # minor chord
        chord_roots.extend([(root_note + 3) % 12, (root_note + 7) % 12])  # root position
        chord_roots.extend([(root_note + 4) % 12, (root_note + 9) % 12])  # first inversion
        chord_roots.extend([(root_note + 5) % 12, (root_note + 8) % 12])  # second inversion
        return(chord_roots)
    if chord_type == 2:  # dominant seventh chord
        chord_roots.extend([(root_note + 4) % 12, (root_note + 7) % 12, (root_note + 10) % 12])  # root position
        chord_roots.extend([(root_note + 3) % 12, (root_note + 6) % 12, (root_note + 8) % 12])  # first inversion
        chord_roots.extend([(root_note + 3) % 12, (root_note + 5) % 12, (root_note + 9) % 12])  # second inversion
        chord_roots.extend([(root_note + 2) % 12, (root_note + 6) % 12, (root_note + 9) % 12])  # third inversion
        return(chord_roots)

def possible_chord_types(chord_root, root_note):
    """
    Returns a list of all possible chord types of a chord with chord root
    chord_root and root (bottom) note root_note, represented as indices in
    global list variable notes
    """
    semitone_difference = abs(chord_root - root_note)
    if semitone_difference > 6:
        semitone_difference = 12 - semitone_difference
    if semitone_difference == 0:
        return([0, 1, 2])
    if semitone_difference == 1:
        return([])  # minor second not a possible interval between chord root and any chord note, regardless of chord type
    if semitone_difference == 2:
        return([2])
    if semitone_difference == 3:
        return([1])
    if semitone_difference == 4:
        return([0, 2])
    if semitone_difference == 5:
        return([0, 1, 2])
    if semitone_difference == 6:
        return([])  # tritone not a possible interval between chord root and any chord note, regardless of chord type

def possible_root_notes(chord_root, chord_type):
    """
    Returns a list of all possible root notes of a chord with chord root
    chord_root and type chord_type, represented as indices in global list
    variables notes and chord_types
    """
    if chord_type == 0:  # major chord
        return([chord_root, (chord_root + 4) % 12, (chord_root + 7) % 12])
    if chord_type == 1:  # minor chord
        return([chord_root, (chord_root + 3) % 12, (chord_root + 7) % 12])
    if chord_type == 2:  # dominant seventh chord
        return([chord_root, (chord_root + 4) % 12, (chord_root + 7) % 12, (chord_root + 10) % 12])

def is_possible_chord(chord_root, chord_type, root_note):
    """
    Checks if the chord with the given properties is a possible chord.
    """
    chord_roots_possible = possible_chord_roots(chord_type, root_note)
    chord_types_possible = possible_chord_types(chord_root, root_note)
    root_notes_possible = possible_root_notes(chord_root, chord_type)
    if (chord_root in chord_roots_possible) and (chord_type in chord_types_possible) and (root_note in root_notes_possible):
        return True
    return False
