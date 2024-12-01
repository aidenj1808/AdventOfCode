with open("in1.txt") as file:
    nums1, nums2 = [], []
    for line in file:
        num1, num2 = [int(num) for num in line.strip().split()]
        nums1.append(num1)
        nums2.append(num2)

part1 = 0
for num1, num2 in zip(sorted(nums1), sorted(nums2)):
    part1 += abs(num1 - num2)
print(f"The answer to part 1 is {part1}")

part2 = 0
for num1 in nums1:
    count = 0
    for num2 in nums2:
        if num1 == num2:
            count += 1
    part2 += num1 * count
print(f"The answer to part 2 is {part2}")
