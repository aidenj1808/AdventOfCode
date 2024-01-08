file = open("inputs/in6.txt")
times = [int(time) for time in file.readline().strip().split()[1:]]
record_distances = [int(dist) for dist in file.readline().strip().split()[1:]]
file.close()

part2_time = int("".join([str(time) for time in times]))
part2_dist = int("".join([str(dist) for dist in record_distances]))

def calc_ways(time, record_distance):
    ways = 0
    for i in range(1, time):
        went = i * (time - i)
        if went > record_distance:
            ways += 1
    return ways

part1 = 1
for time, record_distance in zip(times, record_distances):
    part1 *= calc_ways(time, record_distance)
part2 = calc_ways(part2_time, part2_dist)
print(f"The answer to part 1 is: {part1}")
print(f"The answer to part 2 is: {part2}")
