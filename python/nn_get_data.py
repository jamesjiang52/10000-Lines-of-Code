import numpy as np
import translate


def next_batch(batch_size, data, labels):
    """
    batch_size: int,
    data: ndarray[][float],
    labels: ndarray[][int] -> Tuple(ndarray[][float], ndarray[][int]

    Gets the next random batch of training data and labels.
    """
    a = np.arange(0, len(data))
    np.random.shuffle(a)
    a = a[:batch_size]
    return(data[a], labels[a])


def generate_label(num_labels, correct_label):
    """
    num_labels: int, correct_label: int -> List[int]

    Returns a one-hot label.
    """
    label = [0]*num_labels
    label[correct_label] = 1
    return(label)


len_data = 217

train_data = []
with open("data/train_data.txt") as f:
    for line in f:
        data = line.rstrip("\n").split(" ")
        train_data.append(list(map(int, data)))

test_data = []
with open("data/test_data.txt") as f:
    for line in f:
        data = line.rstrip("\n").split(" ")
        test_data.append(list(map(int, data)))

train_chord_roots = []
train_chord_types = []
train_root_notes = []
train_chord_roots_read = [line.rstrip("\n") for line in open("data/train_chord_root_labels.txt")]
train_chord_types_read = [line.rstrip("\n") for line in open("data/train_chord_type_labels.txt")]
train_root_notes_read = [line.rstrip("\n") for line in open("data/train_root_note_labels.txt")]

for i in range(len(train_data)):
    chord_root_label = generate_label(12, int(train_chord_roots_read[i]))
    chord_type_label = generate_label(translate.NUM_CHORD_TYPES, int(train_chord_types_read[i]))
    root_note_label = generate_label(12, int(train_root_notes_read[i]))
    train_chord_roots.append(chord_root_label)
    train_chord_types.append(chord_type_label)
    train_root_notes.append(root_note_label)

test_chord_roots = []
test_chord_types = []
test_root_notes = []
test_chord_roots_read = [line.rstrip("\n") for line in open("data/test_chord_root_labels.txt")]
test_chord_types_read = [line.rstrip("\n") for line in open("data/test_chord_type_labels.txt")]
test_root_notes_read = [line.rstrip("\n") for line in open("data/test_root_note_labels.txt")]

for i in range(len(test_data)):
    chord_root_label = generate_label(12, int(test_chord_roots_read[i]))
    chord_type_label = generate_label(translate.NUM_CHORD_TYPES, int(test_chord_types_read[i]))
    root_note_label = generate_label(12, int(test_root_notes_read[i]))
    test_chord_roots.append(chord_root_label)
    test_chord_types.append(chord_type_label)
    test_root_notes.append(root_note_label)

train_data = np.array(train_data)/255
train_chord_roots = np.array(train_chord_roots)
train_chord_types = np.array(train_chord_types)
train_root_notes = np.array(train_root_notes)

test_data = np.array(test_data)/255
test_chord_roots = np.array(test_chord_roots)
test_chord_types = np.array(test_chord_types)
test_root_notes = np.array(test_root_notes)
