file = open("inputs/in4.txt")
part1 = 0
part2 = []
for i, line in enumerate(file):
    all_numbers = line.strip().split(":")[1].strip().split(" | ")
    numbers_have, winning_numbers = [numbers.split() for numbers in all_numbers]
    points = 0
    winners = 0
    for number_have in numbers_have:
        if number_have in winning_numbers:
            winners += 1
            if points == 0:
                points += 1
            else:
                points *= 2
    part1 += points
    part2.append([i + 1, winners])

count = len(part2)
for game, winners in part2:
    for i in range(1, winners + 1):
        if game + i <= count:
            part2.append([game + i, part2[game + i - 1][1]])
file.close()
print(f"The answer to part 1 is: {part1}")
print(f"The answer to part 2 is: {len(part2)}")