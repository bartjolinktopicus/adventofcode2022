import time

calories = 0
elves = []

starttime = time.time()
with open('input.txt', 'r') as file:
    for line in file.readlines():
        try:
            calories += int(line.strip())
        except ValueError:
            elves.append(calories)
            calories = 0

print(f"Part 1: {max(elves)}")
print(f"Part 2: {sum(sorted(elves)[-3:])}")
endtime = time.time()

print(f'Took {endtime - starttime} seconds!')