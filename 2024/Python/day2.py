with open("in2.txt") as file:
    all_nums = []
    for line in file:
        all_nums.append([int(x) for x in line.strip().split()])

def is_safe(nums):
    ascending_or_descending = nums == sorted(nums) or nums == sorted(nums, reverse=True)
    safe = 1
    for i in range(len(nums) - 1):
        difference = abs(nums[i] - nums[i + 1])
        if not ascending_or_descending or not 1 <= difference <= 3:
            safe = 0
    return safe

part1 = 0
part2 = 0
for nums in all_nums:
    if is_safe(nums):
        part1 += 1

    safe = 0
    for j in range(len(nums)):
        nums_without_one = nums[:j] + nums[j + 1:]
        if is_safe(nums_without_one):
            safe = 1
    if safe:
        part2 += 1
        
print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")
