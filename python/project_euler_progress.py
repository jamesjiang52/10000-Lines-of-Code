import time

class Progress:
    def __init__(self, problem_number_and_name, count, total):
        self.problem_number_and_name = problem_number_and_name
        self.count = count
        self.total = total
        self.start_time = time.time()

    bar_len = 20

    def progress(self):
        filled_len = int(round(self.bar_len*self.count/self.total))

        percent = str(round(100*self.count/self.total, 1)) + '%'
        bar = '[' + '#'*filled_len + ' '*(self.bar_len - filled_len) + ']'

        elapsed_time = str(time.time() - self.start_time)[:10]
        time_components = elapsed_time.split('.')
        if round(1000*int(time_components[1])) == 0:
            time_bar = "[00:00.000]"
        else:
            time_components[1].ljust(3, '0')
            milliseconds = time_components[1][:3]
            seconds = str(int(time_components[0]) % 60).zfill(2)
            minutes = str(int(time_components[0])//60).zfill(2)
            time_bar = '[' + minutes + ':' + seconds + '.' + milliseconds + ']'

        print(time_bar, bar, percent.rjust(6), ' | ', self.problem_number_and_name.ljust(54), '=', self.count, ' '*5, end='\r')

