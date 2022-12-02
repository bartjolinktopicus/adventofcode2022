import time

class SolutionTimer:

    def run(self, function):
        starttime = time.time()
        function()
        endtime = time.time()
        print(f'Took {endtime - starttime} seconds!')