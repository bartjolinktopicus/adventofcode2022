import sys

sys.path.append('../')
from utils.timer import SolutionTimer


def main():
    SolutionTimer().run(solution)


int_map = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}

options = ['A', 'B', 'C']
outcomes = {
    'X': 0,  # X = Lose
    'Y': 1,  # Y = Draw
    'Z': -1  # Z = Win
}


def solution():
    score = 0
    with open('input', 'r') as file:
        for line in file.readlines():
            opponent, response = line.strip().split(' ')
            score += outcome(opponent, response)
    print(f"score 1: {score}")

    score = 0
    with open('input', 'r') as file:
        for line in file.readlines():
            opponent, desired_outcome = line.strip().split(' ')
            if desired_outcome == 'X':
                # Go back 1 spot in options
                response = options[int_map[opponent] - 2]
            elif desired_outcome == 'Y':
                # return same response
                response = opponent
            elif desired_outcome == 'Z':
                # Go back 2 spots in options
                response = options[int_map[opponent] - 3]
            score += outcome(opponent, response)
    print(f"score 2: {score}")


# Lose = 0
# Draw = 3
# Win = 6
def outcome(opponent, response):
    # Same = draw
    if int_map[opponent] == int_map[response]:
        return 3 + int_map[response]
    # If opponent 1 lower, win
    # If opponent 2 lower, lose
    if int_map[opponent] < int_map[response]:
        if int_map[opponent] + 1 < int_map[response]:
            return 0 + int_map[response]
        return 6 + int_map[response]
    # If opponent 1 higher, win
    # If opponent 2 higher, lose
    if int_map[opponent] > int_map[response]:
        if int_map[opponent] > int_map[response] + 1:
            return 6 + int_map[response]
        return 0 + int_map[response]


if __name__ == '__main__':
    main()
