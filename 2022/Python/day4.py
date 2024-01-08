file = open("inputs/in4.txt")
part1 = 0
part2 = 0
for line in file:
    start1, stop1 = line.strip().split(",")[0].split("-")
    start2, stop2 = line.strip().split(",")[1].split("-")
    start1, stop1, start2, stop2 = [int(x) for x in [start1, stop1, start2, stop2]]
    if stop1 <= stop2 and start2 <= start1 or start1 <= start2 and stop2 <= stop1:
        part1 += 1
    if not (stop2 < start1 or stop1 < start2):
        part2 += 1
file.close()
print(f"The answer for part 1 is: {part1}")
print(f"The answer for part 2 is: {part2}")