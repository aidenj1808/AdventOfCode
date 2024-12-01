with open("inputs/in1.txt") as file:
    nums = [int(num) for num in file.read().splitlines()]

part1 = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        part1 += 1
print(f"The answer for part 1 is: {part1}")

part2 = 0
old_sum = sum(nums[0:3])
for i in range(len(nums)):
    l, r = i, i + 3
    new_sum = sum(nums[l:r])
    if new_sum > old_sum:
        part2 += 1
    old_sum = new_sum
print(f"The answer for part 1 is: {part2}")

