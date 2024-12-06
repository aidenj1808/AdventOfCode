with open("inputs/in4.txt") as file:
    grid = file.read().splitlines()

ROWS = len(grid)
COLS = len(grid[0])

def has_next_letter(grid, cur_pos, x_dir, y_dir, next_letter):
    x, y = cur_pos
    if 0 <= x + x_dir < ROWS and 0 <= y + y_dir < COLS and \
        grid[x + x_dir][y + y_dir] == next_letter:
        return True
    return False

part1 = 0
for x in range(ROWS):
    for y in range(COLS):
        if grid[x][y] != 'X':
            continue

        for x_dir in [-1, 0, 1]:
            for y_dir in [-1, 0, 1]:
                cur_pos = x, y
                for letter in ['M', 'A', 'S']:
                    if has_next_letter(grid, cur_pos, x_dir, y_dir, letter):
                        cur_pos = cur_pos[0] + x_dir, cur_pos[1] + y_dir
                    else:
                        break

                    if letter == 'S':
                        part1 += 1
print(f"The answer to part 1 is {part1}")

part2 = 0
m_s_check = {'X': '', 'M': 'S', 'A': '', 'S': 'M'}
for x in range(1, ROWS - 1):
    for y in range(1, COLS - 1):
        if grid[x][y] != 'A':
            continue

        correct_m_s = 1
        dirs = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        for k in range(0, len(dirs), 2):
            x_dir, y_dir = dirs[k]
            letter = grid[x + x_dir][y + y_dir]
            if letter not in ['M', 'S']:
                correct_m_s = 0
                break

            letter_diagonal = grid[x + dirs[k + 1][0]][y + dirs[k + 1][1]]
            if letter != m_s_check[letter_diagonal]:
                correct_m_s = 0

        if correct_m_s:
            part2 += 1           
print(f"The answer to part 2 is {part2}")
