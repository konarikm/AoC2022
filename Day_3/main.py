rucksacks = open("src.txt").read().split("\n")

values_lower = range(1, 27)
keys_lower = [chr(i) for i in range(97, 123)]
lower = dict(zip(keys_lower, values_lower))

values_upper = range(27, 53)
keys_upper = [chr(i) for i in range(65, 91)]
upper = dict(zip(keys_upper, values_upper))

priorities = lower | upper


def part_one():
    shared = []
    for rucksack in rucksacks:
        first_comp = rucksack[0:len(rucksack)//2]
        second_comp = rucksack[len(rucksack)//2:]

        for char in first_comp:
            if char in second_comp:
                shared.append(char)
                break
    return shared


def part_two():
    shared = []
    groups = []
    start = 0
    end = 3

    for _ in range(len(rucksacks)//3):
        groups.append(rucksacks[start:end])
        start += 3
        end += 3

    for group in groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                shared.append(char)
                break
    return shared


print("Part 1:", sum(priorities[i] for i in part_one()))
print("Part 2:", sum(priorities[i] for i in part_two()))
