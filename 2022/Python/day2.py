file = open("inputs/in2.txt")
guide = [line.split() for line in file]
file.close()

rules = {
    "CY": 0,
    "BY": 3,
    "AY": 6,
    "BX": 0,
    "AX": 3,
    "CX": 6,
    "AZ": 0,
    "CZ": 3,
    "BZ": 6
}

choice = {
    "X": 1,
    "Y": 2,
    "Z": 3 
}

part1 = 0
part2 = 0
for opp, you in guide:
    if you == 'X':
        part1 += 1
        for plays, points in rules.items():
            if plays.startswith(opp) and points == 0:
                part2 += choice[plays[-1]]
    elif you == 'Y':
        part1 += 2
        for plays, points in rules.items():
            if plays.startswith(opp) and points == 3:
                part2 += choice[plays[-1]]
                part2 += 3
    elif you == 'Z':
        part1 += 3
        for plays, points in rules.items():
            if plays.startswith(opp) and points == 6:
                part2 += choice[plays[-1]]
                part2 += 6
    game = opp + you
    part1 += rules[game]

print(f"The answer for part 1 is: {part1}")
print(f"The answer for part 2 is: {part2}")