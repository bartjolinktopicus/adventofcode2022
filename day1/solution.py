# from ..utils.timer import SolutionTimer

def solution():
    calories = 0
    elves = []

    with open('input', 'r') as file:
        for line in file.readlines():
            try:
                calories += int(line.strip())
            except ValueError:
                elves.append(calories)
                calories = 0

    print(f"Part 1: {max(elves)}")
    print(f"Part 2: {sum(sorted(elves)[-3:])}")

def main():
    # SolutionTimer().run(solution)
    solution()

if __name__ == '__main__':
    main()
