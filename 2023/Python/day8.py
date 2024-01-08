file = open("inputs/in8.txt")
directions = file.readline().strip()
file.readline()
my_dict = {}
for line in file:
    p1 = line.strip().split(" = ")[0]
    p2, p3 = line.strip(")\n").split("(")[1].split(", ")
    my_dict.update({p1 : (p2, p3)})
file.close()

def solution(current):
    steps = 0
    while True:
        for direction in directions:
            if current == "ZZZ":
                return steps
            if direction == 'L':
                current = my_dict[current][0]
            elif direction == 'R':
                current = my_dict[current][1]
            steps += 1
print(f"The answer for part 1 is: {solution("AAA")}")