with open ("day1.txt") as f:
    elfs = [0]
    position = 0
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if line.isdecimal():
            elfs[position] += int(line)
        else:
            elfs.append(0)
            position += 1

elfs.sort(reverse=True)
print(elfs[0], elfs[0] + elfs[1] + elfs[2])
