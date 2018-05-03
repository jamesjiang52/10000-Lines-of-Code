import os


def is_tab(index, string):
    if index + 3 > len(string) - 1:
        return False
    return(string[index]
           == string[index + 1]
           == string[index + 2]
           == string[index + 3]
           == " ")


char_count = {"\n": 0, "\t": 0, " ": 0}

root = "../APS105-Labs/"
directories = os.listdir(root)
directories = [directory for directory in directories if directory[:3] == "Lab"]

for directory in directories:
    files = os.listdir(root + directory)
    for file in files:
        if file[-2:] in [".c", ".h"]:
            lines = [line.rstrip("\n") for line in open(root + directory + "/" + file)]
            char_count["\n"] += len(lines)
            for line in lines:
                i = 0
                while i in range(len(line)):
                    if line[i] not in char_count:
                        char_count[line[i]] = 1
                        i += 1
                    else:
                        if (line[i] == " ") and is_tab(i, line):
                            char_count["\t"] += 1
                            i += 4
                        else:
                            char_count[line[i]] += 1
                            i += 1

char_percentages = {}
total = sum(char_count.values())
for char in char_count:
    char_percentages[char] = 100*char_count[char]/total
