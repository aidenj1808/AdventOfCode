file = open("in.txt")
all_numbers = [line.split() for line in file]
all_numbers = [list(map(int, numbers)) for numbers in all_numbers]
file.close()

def solution(all_numbers, part):
    total = 0
    for numbers in all_numbers:
        if part == 2:
            numbers = numbers[::-1]
            
        calc = [numbers]
        current = numbers
        while True:
            nxt = []
            for i in range(len(current) - 1):
                nxt.append(current[i + 1] - current[i])
            calc.append(nxt)
            current = nxt
            if all(x == 0 for x in nxt):
                break

        res = 0
        for lst in calc:
            res += lst[-1]
        total += res
    return total

print(f"The answer for part 1 is: {solution(all_numbers, 1)}")
print(f"The answer for part 2 is: {solution(all_numbers, 2)}")