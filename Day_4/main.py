f = open("src.txt").read().split("\n")


def part_one(file):
    res = 0

    for pair in file:
        pair = pair.split(sep=',')
        
        for i in range(len(pair)):
            index = pair[i].index("-")

            if i == 0:
                first_start = int(pair[i][0:index])
                first_end = int(pair[i][index + 1:])
            else:
                second_start = int(pair[i][0:index])
                second_end = int(pair[i][index + 1:])

        first_elf_sections = [i for i in range(first_start, first_end + 1)]
        second_elf_sections = [j for j in range(second_start, second_end + 1)]
        if set(first_elf_sections + second_elf_sections) == set(first_elf_sections) or set(first_elf_sections + second_elf_sections) == set(second_elf_sections):
            res += 1

    return res


def part_two(file):
    res = 0

    for pair in file:
        pair = pair.split(sep=',')

        for i in range(len(pair)):
            index = pair[i].index("-")

            if i == 0:
                first_start = int(pair[i][0:index])
                first_end = int(pair[i][index + 1:])
            else:
                second_start = int(pair[i][0:index])
                second_end = int(pair[i][index + 1:])

        first_elf_sections = [i for i in range(first_start, first_end + 1)]
        second_elf_sections = [j for j in range(second_start, second_end + 1)]
        for i in first_elf_sections:
            if i in second_elf_sections:
                res += 1
                break

    return res


print("Part 1:", part_one(f), "Part 2:", part_two(f))

