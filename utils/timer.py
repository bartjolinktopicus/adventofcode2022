import time

class SolutionTimer:

    def run(function):
        starttime = time.time()
        function()
        endtime = time.time()
        print(f'Took {endtime - starttime} seconds!')