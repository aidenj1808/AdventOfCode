import re


with open("inputs/in3.txt") as file:
    part1 = 0
    part2 = 0
    enabled = True
    for line in file:
        valid_muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)
        for mul in valid_muls:
            if mul == "do()":
                enabled = True
            elif mul == "don't()":
                enabled = False
            else:
                num1, num2 = [int(num) for num in mul.lstrip("mul(").rstrip(")").split(",")]
                part1 += num1 * num2
                if enabled:
                    part2 += num1 * num2
print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")
