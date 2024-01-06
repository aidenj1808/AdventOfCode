file = open("in.txt")
lines = [line.strip() for line in file]
ROWS = len(lines)
COLS = len(lines[0])
gears = {}

part1 = 0
for i in range(ROWS):
    num = 0
    part = False
    has_star = False
    
    for j in range(COLS + 1):
        if j < COLS and lines[i][j].isdigit():
            num = num * 10 + int(lines[i][j])
            for x_dir in [-1, 0, 1]:
                for y_dir in [-1, 0, 1]:
                    # if element surrounding direction is in the range of its proper surrounding
                    if 0 <= i + x_dir < ROWS and 0 <= j + y_dir < COLS:
                        char = lines[i + x_dir][j + y_dir]
                        if not char.isdigit() and char != '.':
                            part = True
                        if char == '*':
                            has_star = True
                            gear_cords = (i + x_dir, j + y_dir)
                            if gear_cords not in gears:
                                gears.update({gear_cords: []})
        elif num > 0:
            if part:
                part1 += num
            if has_star:
                gears[gear_cords].append(num)
            num = 0
            part = False
            has_star = False
part2 = 0
for cords, parts in gears.items():
    if len(parts) == 2:
        part2 += parts[0] * parts[1]

print(f"The answer for part 1 is {part1}")
print(f"The answer for part 2 is {part2}")