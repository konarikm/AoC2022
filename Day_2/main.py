possible_outcomes = {"A X": 4, "A Y": 8, "A Z": 3,
                     "B X": 1, "B Y": 5, "B Z": 9,
                     "C X": 7, "C Y": 2, "C Z": 6}

possible_outcomes_two = {"A X": "A Z", "A Y": "A X", "A Z": "A Y",
                         "B X": "B X", "B Y": "B Y", "B Z": "B Z",
                         "C X": "C Y", "C Y": "C Z", "C Z": "C X"}

outcomes = []

f = open("src.txt")
for line in f.readlines():
    outcomes.append(line.rstrip())


def part_one(outcomes):
    sum_one = 0

    for i in range(len(outcomes)):
        sum_one += possible_outcomes[outcomes[i]]

    return sum_one


def part_two(outcomes):
    sum_two = 0

    for i in range(len(outcomes)):
        sum_two += possible_outcomes[possible_outcomes_two[outcomes[i]]]

    return sum_two


print(part_one(outcomes), part_two(outcomes))
