with open("inputs/in3.txt") as file:
    all_bits = [bits for bits in file.read().splitlines()]

most_common = ""
least_common = ""
for i in range(len(all_bits[0])):
    ones, zeros = 0, 0
    for j in range(len(all_bits)):
        if all_bits[j][i] == "0":
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        most_common += "1"
        least_common += "0"
    else:
        most_common += "0"
        least_common += "1"
part1 = int(most_common, 2) * int(least_common, 2)
print(f"The answer for part 1 is: {part1}")

bits_to_search = all_bits
bit_position = 0
while len(bits_to_search) != 1:
    ones, zeros = 0, 0
    for bits in bits_to_search:
        if bits[bit_position] == "1":
            ones += 1
        else:
            zeros += 1
    if ones >= zeros:
        bits_to_search = [bits for bits in bits_to_search if bits[bit_position] == "1"]
    else:
        bits_to_search = [bits for bits in bits_to_search if bits[bit_position] == "0"]
    bit_position += 1
ogr = bits_to_search[0]

bits_to_search = all_bits
bit_position = 0
while len(bits_to_search) != 1:
    ones, zeros = 0, 0
    for bits in bits_to_search:
        if bits[bit_position] == "1":
            ones += 1
        else:
            zeros += 1
    if ones < zeros:
        bits_to_search = [bits for bits in bits_to_search if bits[bit_position] == "1"]
    else:
        bits_to_search = [bits for bits in bits_to_search if bits[bit_position] == "0"]
    bit_position += 1
co2sr = bits_to_search[0]

part2 = int(ogr, 2) * int(co2sr, 2)
print(f"The answer for part 2 is: {part2}")
