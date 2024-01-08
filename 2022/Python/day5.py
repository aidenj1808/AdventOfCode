file = open("inputs/in5.txt")
contents = file.read()
file.close()
crates, all_directions = contents.split("\n\n")

stacks1 = [[] for _ in range(9)]
stacks2 = [[] for _ in range(9)]
for line in crates.split("\n")[:-1]:
    for j, char in enumerate(line):
        if char.isalpha():
            stack_idx = int(crates.split("\n")[-1][j]) - 1
            stacks1[stack_idx].append(char)
            stacks2[stack_idx].append(char)
for stack1, stack2 in zip(stacks1, stacks2):
    stack1.reverse()
    stack2.reverse()

directions = []
for direction in all_directions.split("\n"):
    _, move, _, frm, _, to = direction.split(" ")
    directions.append([int(x) for x in [move, frm, to]])

# for move, frm, to in directions:
#     load = []
#     for _ in range(move):
#         stacks1[to - 1].append(stacks1[frm - 1].pop())
#         load.append(stacks2[frm - 1].pop())
#     stacks2[to - 1] = stacks2[to - 1] + list(reversed(load))

stack2 = stack1[:]
for move, frm, to in directions:
    load = []
    for _ in range(move):
        stacks1[to - 1].append(stacks1[frm - 1].pop())
        load.append(stacks2[frm - 1].pop())
    stacks2[to - 1] = stacks2[to - 1] + list(reversed(load))

part1 = ''
part2 = ''
for stack1, stack2 in zip(stacks1, stacks2):
    part1 += stack1[-1]
    part2 += stack2[-1]
print(f"The answer for part 1 is: {part1}")
print(f"The answer for part 2 is: {part2}")