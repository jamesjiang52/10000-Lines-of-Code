import numpy as np
import matplotlib.pyplot as plt
import python_chars
import c_chars
import html_chars


def get_key_percentages(char_count):
    chars = list("abcdefghijklmnopqrstuvwxyz`1234567890-=[];'\,./")
    chars.extend(["Shift", "Enter", "Spacebar", "Tab"])
    counts = [0]*len(chars)
    symbols = list("~!@#$%^&*()_+{}:\"|<>?")
    symbols_orig = list("`1234567890-=[];'\,./")
    for i in char_count:
        char = i[0]
        count = i[1]
        if char in chars:
            counts[chars.index(char)] += count
        elif char in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            counts[chars.index(char.lower())] += count
            counts[chars.index("Shift")] += count
        elif char in symbols:
            counts[chars.index(symbols_orig[symbols.index(char)])] += count
            counts[chars.index("Shift")] += count
        elif char == "\n":
            counts[chars.index("Enter")] += count
        elif char == " ":
            counts[chars.index("Spacebar")] += count
        elif char == "\t":
            counts[chars.index("Tab")] += count
        else:
            pass  # ignore special characters like €
    total = sum(counts)
    percentages = [100*count/total for count in counts]
    return(sorted(percentages, reverse=True),
           [char for _, char in sorted(zip(percentages, chars), reverse=True)])


def bar_graph_char_percentages(char_tuple, title=None):
    char_percentages = char_tuple[0]
    chars = char_tuple[1]
    N = len(chars)
    width = 0.8
    i = np.arange(N)
    title_font = {"fontname": "Georgia", "fontsize": 16}
    labels_font = {"fontname": "Georgia", "fontsize": 10}
    axis_font = {"fontname": "Georgia", "fontsize": 12}
    plt.figure(figsize=(16, 9))
    plt.bar(i, char_percentages, width, color="#A0A0A0")
    plt.title(title, **title_font)
    plt.xticks(i, chars, rotation="vertical", **labels_font)
    plt.yticks(np.arange(0, 13.001, 1), **labels_font)
    plt.xlabel("Keys", **axis_font)
    plt.ylabel("Percentage of total", **axis_font)
    plt.xlim([-1, N])
    plt.ylim([0, 13])
    plt.tight_layout()
    plt.savefig("images/" + title.lower() + ".pdf", bbox_inches="tight", format="pdf")


char_count_python = python_chars.char_count.items()
char_count_c = c_chars.char_count.items()
char_count_html = html_chars.char_count.items()


if __name__ == "__main__":
    bar_graph_char_percentages(get_key_percentages(char_count_python), title="Python")
    bar_graph_char_percentages(get_key_percentages(char_count_c), title="C")
    bar_graph_char_percentages(get_key_percentages(char_count_html), title="HTML")
