from math import lcm


def parse(lines):
    instructions = lines.pop(0).strip()
    paths = {}
    for line in lines[1:]:
        split = line.split(' = (')
        root = split[0].strip()
        nodes = split[1].replace(')', '').strip().split(', ')
        paths[root] = nodes
    return instructions, paths


def part1(instructions, paths):
    n_instructions = len(instructions)
    current = 'AAA'
    counter = 0
    while current != 'ZZZ':
        if instructions[counter % n_instructions] == 'L':
            current = paths[current][0]
        else:
            current = paths[current][1]
        counter += 1
    return counter


def part2(instructions, paths):
    n_instructions = len(instructions)
    result = 1
    for current in [node for node in paths.keys() if node[-1] == 'A']:
        counter = 0
        while current[-1] != 'Z':
            if instructions[counter % n_instructions] == 'L':
                current = paths[current][0]
            else:
                current = paths[current][1]
            counter += 1
        result = lcm(result, counter)
    return result


if __name__ == '__main__':
    def main():
        with open('day8.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        instructions, paths = parse(lines)
        print(part1(instructions, paths))
        print(part2(instructions, paths))


    main()
