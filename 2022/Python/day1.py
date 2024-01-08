file = open("inputs/in1.txt")
cals = []
current_cal = 0
for line in file:
    line = line.strip()
    if line == '':
        cals.append(current_cal)
        current_cal = 0
    else:
        current_cal += int(line)
file.close()

print(f"The answer for part 1 is: {max(cals)}")
print(f"The answer for part 2 is: {sum(sorted(cals)[::-1][:3])}")
    