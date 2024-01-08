file = open("inputs/in3.txt")
part1 = 0
group = []
groups = []
for i, line in enumerate(file):
    line = line.strip()
    half = len(line) // 2
    for item in line[:half]:
        if item in line[half:]:
            if item.islower():
                part1 += ord(item) - 96
                break
            else:
                part1 += ord(item) - 38
                break

    group.append(line)
    if len(group) == 3:
        groups.append(group)
        group = []
file.close()

part2 = 0
for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            if char.islower():
                part2 += ord(char) - 96
                break
            else:
                part2 += ord(char) - 38
                break

print(f"The answer for part1 is: {part1}")
print(f"The answer for part2 is: {part2}")