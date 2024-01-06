file = open("in.txt")
total1 = 0
total2 = 0
number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in file:
    part1 = []
    part2 = []

    for i, char in enumerate(line.strip()):
        if char.isdigit():
            part1.append(char)
            part2.append(char)

        for j, num in enumerate(number_strings):
            if line[i:].startswith(num):
                part2.append(str(j + 1))

    total1 += int(part1[0] + part1[-1])
    total2 += int(part2[0] + part2[-1])
file.close()

print(f"The answer to part 1 is {total1}")
print(f"The answer to part 2 is {total2}")