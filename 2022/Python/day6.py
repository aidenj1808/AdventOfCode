file = open("inputs/in6.txt")
contents = file.read().strip()
file.close()

def hasDifferentChars(s):
    n = len(s)
    for i in range(n):
        if s[i] in s[i + 1:]:
            return False
    return True

part1 = 0
part2 = 0
for i, char in enumerate(contents):
    if hasDifferentChars(contents[i: i + 4]) and part1 == 0:
        part1 = i + 4
    elif hasDifferentChars(contents[i: i + 14]) and part2 == 0:
        part2 = i + 14
    elif part1 != 0 and part2 != 0:
        break
    
print(f"The answer for part 1 is: {part1}")
print(f"The answer for part 2 is: {part2}")