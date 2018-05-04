import time
import sys

def print_char(char):
    print(char, end='')
    time.sleep(0.03)
    sys.stdout.flush()

def end_text(start, num_problems):
    elapsed = time.time() - start
    elapsed_str = str(elapsed)[:10]
    time_components = elapsed_str.split('.')
    time_components[1].ljust(3, '0')
    milliseconds = time_components[1][:3]
    seconds = str(int(time_components[0]) % 60).zfill(2)
    minutes = str(int(time_components[0])//60).zfill(2)
    elapsed_display = minutes + ':' + seconds + '.' + milliseconds

    time.sleep(0.8)

    print("\n")
    num_problem_info = str(num_problems) + " problems were solved."
    for i in num_problem_info:
        print_char(i)

    time.sleep(0.5)

    time_info = " The total elapsed time was " + elapsed_display + '.'
    for i in time_info:
        print_char(i)

    time.sleep(0.5)

    exit_prompt = "Press ENTER to exit."

    print('')
    for i in exit_prompt:
        print_char(i)
    print('\n')

    input()
