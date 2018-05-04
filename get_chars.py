import os


def is_tab(index, string):
    if index + 3 > len(string) - 1:
        return False
    return(string[index]
           == string[index + 1]
           == string[index + 2]
           == string[index + 3]
           == " ")


def get_chars(language_name):
    char_counts = {"\n": 0, "\t": 0, " ": 0}
    files = os.listdir(language_name)

    for file in files:
        lines = [
            line.rstrip("\n") for line in open(language_name + "/" + file)]
        char_counts["\n"] += len(lines)
        for line in lines:
            i = 0
            while i in range(len(line)):
                if line[i] not in char_counts:
                    char_counts[line[i]] = 1
                    i += 1
                else:
                    if (line[i] == " ") and is_tab(i, line):
                        char_counts["\t"] += 1
                        i += 4
                    else:
                        char_counts[line[i]] += 1
                        i += 1

    char_percentages = {}
    total = sum(char_counts.values())
    for char in char_counts:
        char_percentages[char] = 100*char_counts[char]/total

    return(char_counts, char_percentages)
