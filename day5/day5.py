def parse(lines):
    seeds = [int(seed) for seed in lines.pop(0).split(": ")[1].split()]

    maps = {}
    current_map = []
    for line in lines:
        if line.isspace():
            continue

        if 'map' in line:
            current_map = []
            maps[line.split()[0]] = current_map
            continue

        current_map.append(tuple(map(int, line.split())))

    return seeds, maps


def part1(seeds, maps):
    for mappings in maps.values():
        remapped_seeds = [seed for seed in seeds]
        for dest_start, source_start, length in mappings:
            for i, seed in enumerate(seeds):
                if source_start <= seed < source_start + length:
                    remapped_seeds[i] = dest_start + (seed - source_start)
        seeds = remapped_seeds
    return min(seeds)


def part2(seeds, maps):
    smallest = float('inf')
    for seed_start, seed_length in zip(seeds[::2], seeds[1::2]):
        ranges_to_remap = [(seed_start, seed_start + seed_length)]
        for mappings in maps.values():
            remapped_ranges = []

            while ranges_to_remap:
                current_start, current_end = ranges_to_remap.pop()  # algorytm sztosowy
                for dest_start, source_start, length in mappings:
                    new_start = max(source_start, current_start)
                    new_end = min(source_start + length, current_end)

                    if new_start < new_end:
                        offset = dest_start - source_start
                        remapped_ranges.append((new_start + offset, new_end + offset))

                        if new_start > current_start:
                            ranges_to_remap.append((current_start, new_start))

                        if new_end < current_end:
                            ranges_to_remap.append((new_end, current_end))

                        break  # overlap found
                else:  # no overlaps
                    remapped_ranges.append((current_start, current_end))
            ranges_to_remap = remapped_ranges
        smallest = min(smallest, min([r[0] for r in ranges_to_remap]))

    return smallest


if __name__ == '__main__':
    def main():
        with open('day5.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        seeds, maps = parse(lines)
        print(part1(seeds, maps))
        print(part2(seeds, maps))


    main()
