import os
import random
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import translate


def crop_image(image):
    """
    image: ndarray[][][int] -> ndarray[][int]

    Gets binary pixels in first non-white column, cropping pixels at the top
    and bottom.
    """
    return(image[35:252, 54, 0])


train_data_file = open("data/train_data.txt", "w")
train_chord_root_labels_file = open("data/train_chord_root_labels.txt", "w")
train_chord_type_labels_file = open("data/train_chord_type_labels.txt", "w")
train_root_note_labels_file = open("data/train_root_note_labels.txt", "w")
test_data_file = open("data/test_data.txt", "w")
test_chord_root_labels_file = open("data/test_chord_root_labels.txt", "w")
test_chord_type_labels_file = open("data/test_chord_type_labels.txt", "w")
test_root_note_labels_file = open("data/test_root_note_labels.txt", "w")

directories_list = ["major_root/", "major_first_inversion/", "major_second_inversion/", "minor_root/", "minor_first_inversion/", "minor_second_inversion/",
                    "dominant_seventh_root/","dominant_seventh_first_inversion/", "dominant_seventh_second_inversion/", "dominant_seventh_third_inversion/"]

figure = plt.figure(figsize=(6, 3.92), dpi=72)
ax = figure.add_subplot(111)

for directory in directories_list:
    print("Current directory:", directory)
    audio_files = os.listdir("chord_wavs/" + directory)
    for file in audio_files:
        sample_rate, samples = wavfile.read("chord_wavs/" + directory + file)
        samples = samples[:, 0]  # get mono samples

        frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nperseg=2048)
        plt.pcolormesh(times, frequencies, spectrogram, cmap="binary")

        start = 256/11025
        increment = 64/1575

        for i in range(6):
            plt.axis([start + i*increment, start + (i + 1)*increment, 0, 5000])
            plt.axis("off")

            figure.canvas.draw()
            image = np.frombuffer(figure.canvas.tostring_rgb(), dtype=np.uint8)
            image = image.reshape(figure.canvas.get_width_height()[::-1] + (3,))
            image = crop_image(image)
            image_data_str = " ".join([str(j) for j in image])

            random_num = random.randint(0, 9)  # for choosing if data is used for training or evaluation

            if random_num != 5:
                train_data_file.write(image_data_str + "\n")

                filename_components = file.split("_")[:-2]

                train_chord_root_labels_file.write(str(translate.note_to_index(filename_components[0].upper())) + "\n")

                if "major" in filename_components:
                    train_chord_type_labels_file.write(str(translate.type_to_index("")) + "\n")
                elif "minor" in filename_components:
                    train_chord_type_labels_file.write(str(translate.type_to_index("m")) + "\n")
                elif "dominant" in filename_components:
                    train_chord_type_labels_file.write(str(translate.type_to_index("7")) + "\n")

                train_root_note_labels_file.write(str(translate.note_to_index(filename_components[-1].upper())) + "\n")

            else:
                test_data_file.write(image_data_str + "\n")

                filename_components = file.split("_")[:-2]

                test_chord_root_labels_file.write(str(translate.note_to_index(filename_components[0].upper())) + "\n")

                if "major" in filename_components:
                    test_chord_type_labels_file.write(str(translate.type_to_index("")) + "\n")
                elif "minor" in filename_components:
                    test_chord_type_labels_file.write(str(translate.type_to_index("m")) + "\n")
                elif "dominant" in filename_components:
                    test_chord_type_labels_file.write(str(translate.type_to_index("7")) + "\n")

                test_root_note_labels_file.write(str(translate.note_to_index(filename_components[-1].upper())) + "\n")


train_data_file.close()
train_chord_root_labels_file.close()
train_chord_type_labels_file.close()
train_root_note_labels_file.close()
test_data_file.close()
test_chord_root_labels_file.close()
test_chord_type_labels_file.close()
test_root_note_labels_file.close()
