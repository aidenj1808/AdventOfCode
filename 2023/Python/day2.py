import numpy as np

file = open("inputs/in2.txt")
part1 = 0
part2 = 0

for line in file:
    my_dict = {}
    game = int(line.split(":")[0][5:])
    info = line.strip().split(" ", 2)[2].split(";")

    my_dict.update({game: []})
    for reveals in info:
        for reveal in reveals.split(","):
            my_dict[game].append(reveal.strip().split(" "))
    
    for game, reveals in my_dict.items():
        maxs = [0, 0, 0]
        invalid = False
        for count, colour in reveals:
            count = int(count)
            if colour == "red":
                if count > 12:
                    invalid = True
                    
                if maxs[0] < count:
                    maxs[0] = count
                
            if colour == "green":
                if count > 13:
                    invalid = True

                if maxs[1] < count:
                    maxs[1] = count

            if colour == "blue":
                if count > 14:
                    invalid = True

                if maxs[2] < count:
                    maxs[2] = count

        if not invalid:
            part1 += game
        part2 += np.prod(np.array(maxs)) # increment sum with the multiplication of all maxs
file.close()

print(f"The answer to part 1 is {part1}")
print(f"The answer to part 2 is {part2}")