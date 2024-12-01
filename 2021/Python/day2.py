with open("inputs/in2.txt") as file:
    x, y = 0, 0
    y2, aim = 0, 0,
    for line in file:
        line = line.strip().split(" ")
        if line[0] == "forward":
            x += int(line[1])
            y2 += int(line[1]) * aim
        elif line[0] == "down":
            y += int(line[1])
            aim += int(line[1])
        elif line[0] == "up":
            y -= int(line[1])
            aim -= int(line[1])
    part1 = x * y
    part2 = x * y2
print(f"The answer for part 1 is: {part1}")
print(f"The answer for part 2 is: {part2}")
